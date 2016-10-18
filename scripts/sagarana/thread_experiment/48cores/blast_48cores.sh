#!/bin/sh
#Author raony
#PBS -N blast_nt48
#PBS -e blast_48.err
#PBS -o blast_48.log
#PBS -q fila64
#PBS -l select=1:ncpus=48

cd $PBS_O_WORKDIR
/home/raonyguimaraes/venvs/blast_venv/bin/python blast_48cores.py
