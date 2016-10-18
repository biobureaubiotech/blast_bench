#!/bin/sh
#Author raony
#PBS -N blast_nt4
#PBS -e blast_4.err
#PBS -o blast_4.log
#PBS -q fila64
#PBS -l select=1:ncpus=4

cd $PBS_O_WORKDIR
/home/raonyguimaraes/venvs/blast_venv/bin/python blast_4cores.py
