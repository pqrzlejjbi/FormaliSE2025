import math
import threading
from enum import Enum
from functools import partial
from threading import Condition
from typing import Callable, Iterable

import numpy as np
from PyQt6 import QtWidgets
import pyqtgraph as pq

from Utils.OpenScenario.KPIs import StatefulKPI
from Utils.OpenScenario.Simulation.SmallStepBigStepSUL import SmallStepBigStepSUL

class ConditionSwitch:  # TODO move to utils
  def __init__(self, state: bool, on_change: Callable = None):
    self.condition_ = Condition()
    self.state_ = None  # such that we get an initial trigger
    self.on_change = on_change

    self.set(state)

  def set_and_await(self, set_val, wait_val):
    with self.condition_:
      self.set(set_val)
      self.await_state(wait_val)

  def await_state(self, value):
    with self.condition_:
      self.condition_.wait_for(lambda: self.state_ == value)

  def get(self):
    return self.state_

  def set(self, running: bool):
    with self.condition_:
      if self.state_ == running:
        return
      self.state_ = running
      if self.on_change is not None:
        self.on_change(running)
      self.condition_.notify_all()

  def toggle(self):
    with self.condition_:
      self.set(not self.state_)
      return self.state_


class SimulationStepType(Enum):
  small_step = 0  # Single simulation step
  big_step = 1  # Single action step
  full_run = 2  # Full simulation run

class SimulationControlGUI:
  def __init__(self, kpis: list[StatefulKPI], sim_mode: SimulationStepType = SimulationStepType.big_step):
    self.kpis = kpis

    # create app and main container
    main_widget = QtWidgets.QWidget()
    main_widget.setWindowTitle("Simulation Control")

    # create play button
    play_button = QtWidgets.QPushButton()
    self.play_button = play_button

    # create mode buttons. silly me, this is what radio buttons are for!
    mode_buttons = []
    for mode in SimulationStepType:
      btn = QtWidgets.QPushButton(mode.name.replace("_", " "))
      btn.clicked.connect(partial(self.set_mode, mode))
      mode_buttons.append(btn)
    self.mode_buttons = mode_buttons

    # create status bar
    status_widget = QtWidgets.QLabel()
    self.status_widget = status_widget

    # create plot area
    plot_widgets = [pq.PlotWidget() for _ in kpis]
    plot_items = [pw.getPlotItem() for pw in plot_widgets]

    def update_x_range(src):
      range = src.getViewBox().viewRange()[0]
      for item in plot_items:
        item.setXRange(*range, padding=0)

    def enable_autorange():
      for item in plot_items:
        item.enableAutoRange()

    plot_curves = []
    for desc, plot_item in zip(kpis, plot_items):
      plot_item.setTitle(desc.name)
      plot_item.setLabel("left", desc.name, desc.unit)
      plot_item.setLabel("bottom", "time", "s")
      plot_item.getViewBox().sigRangeChangedManually.connect(partial(update_x_range, plot_item))
      curve = plot_item.plot(pen="y")
      plot_curves.append(curve)
    self.plot_curves = plot_curves

    # layout components
    main_layout = QtWidgets.QVBoxLayout()
    main_widget.setLayout(main_layout)

    # layout button bar
    top_layout = QtWidgets.QHBoxLayout()
    top_layout.addWidget(play_button)
    for btn in mode_buttons:
      top_layout.addWidget(btn)

    # TODO this button maybe a bit out of place.
    self.autorange_button = QtWidgets.QPushButton("Autorange")
    self.autorange_button.clicked.connect(enable_autorange)
    top_layout.addWidget(self.autorange_button)

    # layout plot grid
    plot_layout = QtWidgets.QGridLayout()
    target_area = len(plot_widgets)
    aspect_ratio = 3 / 2

    def get_optimal_cols(nr_items, target_aspect_ratio):
      if nr_items == 0:
        return 0
      cols_float = math.sqrt(nr_items / target_aspect_ratio) * target_aspect_ratio
      options = {math.floor(cols_float), math.ceil(cols_float)}
      options = [(math.ceil(nr_items / cols), cols) for cols in options if cols != 0]
      best_idx = \
      min([(rows * cols, abs(cols / rows - target_aspect_ratio), idx) for idx, (rows, cols) in enumerate(options)])[-1]
      rows, cols = options[best_idx]
      return cols

    nr_cols = get_optimal_cols(target_area, aspect_ratio)
    for idx, widget in enumerate(plot_widgets):
      plot_layout.addWidget(widget, int(idx / nr_cols), idx % nr_cols)

    # main layout
    main_layout.addLayout(top_layout)
    main_layout.addWidget(status_widget)
    main_layout.addLayout(plot_layout)

    # init and hooks
    self.sim_mode = None
    self.set_mode(sim_mode)

    self.request_close = False

    self.run_active = ConditionSwitch(None, self.play_button_update)
    self.run_condition = ConditionSwitch(None, self.play_button_update)
    self.run_active.set(False)
    self.run_condition.set(False)
    play_button.clicked.connect(self.play_button_clicked)

    # show the widget and start GUI loop
    main_widget.show()
    self.main_widget = main_widget  # reference is needed to avoid GC

  def set_mode(self, mode: SimulationStepType):
    for btn_idx, btn in enumerate(self.mode_buttons):
      btn.setFlat(btn_idx != mode.value)
    self.sim_mode = mode

  def play_button_clicked(self):
    if self.request_close:
      self.main_widget.close()
    self.run_condition.toggle()

  def play_button_update(self, _):
    style = self.play_button.style()
    pxs = style.StandardPixmap
    if not self.run_condition.get():
      px = pxs.SP_MediaPlay
    elif not self.run_active.get():
      px = pxs.SP_MediaStop
    else:
      px = pxs.SP_MediaPause
    self.play_button.setIcon(style.standardIcon(px))

  def report_small_step(self, in_sym, out_sym):
    kpi: StatefulKPI
    for kpi, curve in zip(self.kpis, self.plot_curves):
      curve.setData(kpi.time_stamps, kpi.data)

  def report_big_step(self, in_sym, out_sym):
    prev = self.status_widget.text()
    self.status_widget.setText(f"{prev} : {out_sym}")

  def report_full_run(self, in_sym, out_sym):
    self.run_active.set(False)

  def report_step(self, step_size: SimulationStepType, in_sym, out_sym, check_block=True):
    match step_size:
      case step_size.small_step:
        self.report_small_step(in_sym, out_sym)
      case step_size.big_step:
        self.report_big_step(in_sym, out_sym)
      case step_size.full_run:
        self.report_full_run(in_sym, out_sym)

    if not check_block:
      return

    if self.sim_mode.value == step_size.value:
      self.run_condition.set_and_await(False, True)
    else:
      self.run_condition.await_state(True)

  def announce_full_run(self):
    # TODO should probably also reset plot widgets.
    self.status_widget.clear()
    self.run_active.set(True)

  def announce_big_step(self, in_sym):
    prev = self.status_widget.text()
    infix = "\n" * np.sign(len(prev))
    self.status_widget.setText(f"{prev}{infix}{in_sym}")

  @staticmethod
  def run_queries(sul: SmallStepBigStepSUL, queries : Iterable):
    # TODO tried to get it working in another thread, but it didn't go well. try again.
    app = QtWidgets.QApplication([])
    gui = SimulationControlGUI(sul.kpis)

    ss = sul.small_step_sul
    bs = sul.big_step_sul

    callback_handles = [
      ss.step.register_post(lambda o, i: gui.report_step(SimulationStepType.small_step, i, o)),
      bs.pre.register_pre(gui.announce_full_run),
      bs.step.register_pre(gui.announce_big_step),
      bs.step.register_post(lambda o, i: gui.report_step(SimulationStepType.big_step, i, o)),
      bs.post.register_post(lambda: gui.report_step(SimulationStepType.full_run, None, None))
    ]

    def work():
      for query in queries:
        sul.query(query)
      gui.request_close = True

    threading.Thread(target=work).start()
    app.exec()

    for handle in callback_handles:
      handle.unregister()