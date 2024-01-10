#! /bin/bash

source activate pangeo
conda list | grep jup
conda env list
env | grep CONDA | grep _ENV
echo $CONDA_DEFAULT_ENV
python simple_sq.py
