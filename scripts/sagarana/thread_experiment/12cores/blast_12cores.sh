#!/bin/sh
#Author raony
#PBS -N blast_nt12
#PBS -e blast_12.err
#PBS -o blast_12.log
#PBS -q fila64
#PBS -l select=1:ncpus=12

cd $PBS_O_WORKDIR
/home/raonyguimaraes/venvs/blast_venv/bin/python blast_12cores.py
