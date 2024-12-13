# Automated ADAS Testing using Automata Learning - A Case Study in Learning-Based Testing

This repository contains the evaluation code for the paper "Automated ADAS Testing using Automata Learning - A Case Study in Learning-Based Testing". We evaluated three testing methods for an adaptive cruise control. 

## Setup
The provided setup script `setup.sh` can be used to install the dependencies necessary for running the evaluation code. It assumes an existing python 3.10 installation. In short it 
- downloads and builds version 2.31.7 of the [esmini](https://github.com/esmini) simulator
- creates links for the resulting shared libraries and other resources
- creates a virtual environment in the folder `venv` and installs the python requirements.

## Running 
The file `main.py` provides methods for running experiments and provides an example for their use. In particular, the method `run_method(method, seed)` runs the specified `method` using default parameters and the given random `seed`. It returns a triple `sul, model, stats`, where `sul` is the interface to the system under learning, `model` is the behavioral model learned during testing and `stats` is a dictionary containing various KPIs. The test cases that were used in the run are contained in `sul.io_sequences`.

## Acknowledgements
This work uses the [esmini](https://github.com/esmini) simulator for OpenSCENARIO XML and the [AALpy](https://github.com/DES-Lab/AALpy) automata learning library. The python bindings for esmini are generated based on [ctypesgen](https://github.com/ctypesgen/ctypesgen).