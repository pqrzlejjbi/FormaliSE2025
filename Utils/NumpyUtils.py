from __future__ import annotations
from abc import abstractmethod

import numpy as np

from Utils.IndentedStringBuffer import IndentedStringBuffer

def rot_2d(theta):
  s, c = np.sin(theta), np.cos(theta)
  return np.array([[c, -s], [s, c]])

class TreeNode:
  def __init__(self, children : list[TreeNode] = None):
    self.children : list[TreeNode] = children or []

  def __str__(self, buffer=None):
    has_buffer = buffer is not None
    if not has_buffer:
      buffer = IndentedStringBuffer()
    buffer.add(self.local_str())
    buffer.indent()
    for child in self.children:
      child.__str__(buffer)
    buffer.unindent()
    if has_buffer:
      return
    return str(buffer)

  def local_str(self):
    return "Bare TreeNode"

class MMCSTreeNode(TreeNode):
  def __init__(self, distance : float, nodes : set, children : list[TreeNode] = None):
    super().__init__(children)
    self.distance : float = distance
    self.nodes : set = nodes

  def local_str(self):
    return f"({self.distance}, {self.nodes})"

def minimal_maximal_cost_structure(distance_matrix) -> MMCSTreeNode:
  # Thinking about it, this should be the same as
  # Agglomerative Hierarchical Clustering with Single Linkage
  # See https://scikit-learn.org/stable/modules/clustering.html#hierarchical-clustering

  # sort transitions by distance. use list of transitions since distance need not be unique
  distance_dict = dict[float, list[tuple[int, int]]]()
  n = distance_matrix.shape[0]
  for row_idx in range(n):
    for col_idx in range(row_idx+1, n):
      idx = (row_idx, col_idx)
      d = distance_matrix[idx]
      if d not in distance_dict:
        distance_dict[d] = [idx]
      else:
        distance_dict[d].append(idx)

  # high level partition map
  node_map = [MMCSTreeNode(distance_matrix[idx, idx], {idx}) for idx in range(n)]

  # by looping over transitions in ascending order, each transition could potentially connect
  # some previously unconnected regions.
  for d, indices in sorted(distance_dict.items(), key = lambda x: x[0]):
    # calculate new partition that results from merging clusters
    for idx1, idx2 in indices:
      tn1 = node_map[idx1]
      tn2 = node_map[idx2]
      if tn1 is tn2:
        continue # a cheaper transition (chain) connected the two nodes.

      # obtain a partition corresponding to the current region of the primary node
      is_new_tn1, is_new_tn2 = [t.distance == d for t in (tn1, tn2)]
      if is_new_tn1 and is_new_tn2:
        tn1.nodes.update(tn2.nodes)
        tn1.children.extend(tn2.children)
        for node in tn2.nodes:
          node_map[node] = tn1
      elif not is_new_tn1 and not is_new_tn2:
        tn_new = MMCSTreeNode(d, set.union(tn1.nodes, tn2.nodes), [tn1, tn2])
        for node in tn_new.nodes:
          node_map[node] = tn_new
      else:
        if not is_new_tn1:
          tn1, tn2 = [tn2, tn1]
        tn1.nodes.update(tn2.nodes)
        tn1.children.append(tn2)
        for node in tn2.nodes:
          node_map[node] = tn1

  assert len(set(node_map)) == 1
  return node_map[0]

class SDF:
  """
  Much of this is adapted from Inigo Quilez
  https://iquilezles.org/
  """
  @abstractmethod
  def sdf(self, p):
    """
    Computes the signed distance between the object and a point / set of points
    :param p: point or array thereof in which case the coordinates are given as the last axis
    :return: signed distance to the object
    """
    raise NotImplementedError()

  @staticmethod
  def colorize(dd, falloff = 1., frequ=1):
    col = np.sign(dd)
    col *= 1.0 - np.exp(-np.abs(dd)/falloff)
    col *= 0.8 + 0.2 * np.cos(frequ * (np.pi*2) * dd)
    return col

class Box(SDF):
  def __init__(self, dimensions, center=None, orientation=0.):
    if center is None:
      center = [0., 0.]
    self.dim = np.asarray(dimensions)
    self.center = np.asarray(center)
    self.orientation = orientation

  def sdf(self, p):
    p = np.asarray(p)

    # coordinates of p in the local coordinates of the box
    p = (np.dot(p - self.center, rot_2d(self.orientation)))
    # exploit symmetry: only consider case where p is in the 1st quadrant
    p = np.abs(p)

    d = p - self.dim / 2
    outer = np.linalg.norm(np.maximum(d, 0),axis=-1)
    inner = np.minimum(np.max(d,axis=-1), 0)
    sdf = outer + inner
    return sdf

  def get_corners(self):
    rot_mat = rot_2d(self.orientation)
    length_off = np.dot(rot_mat, np.array([self.dim[0] / 2, 0]))
    width_off = np.dot(rot_mat, np.array([0, self.dim[1] / 2]))
    pairs = [(1,1),(1,-1),(-1,-1),(-1,1)]
    return [self.center + f_l * length_off + f_w * width_off for f_l,f_w in pairs]

  def distance_to_other(self, other : 'Box'):
    # 1. at least one corner is involved in the shortest distance between rectangles
    # 2. sdf of rectangles is known
    # -> check all valid combinations of sdf(box,corner)
    def inner_dist(o1: Box, o2: Box):
      return min(o1.sdf(o2.get_corners()))
    d1, d2 = inner_dist(self, other), inner_dist(other, self)
    return min(d1,d2)
