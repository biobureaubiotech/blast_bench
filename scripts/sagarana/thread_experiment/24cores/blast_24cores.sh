#!/bin/sh
#Author raony
#PBS -N blast_nt24
#PBS -e blast_24.err
#PBS -o blast_24.log
#PBS -q fila64
#PBS -l select=1:ncpus=24

cd $PBS_O_WORKDIR
/home/raonyguimaraes/venvs/blast_venv/bin/python blast_24cores.py
