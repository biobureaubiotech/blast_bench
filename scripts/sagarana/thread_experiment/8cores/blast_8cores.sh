#!/bin/sh
#Author raony
#PBS -N blast_nt8
#PBS -e blast_8.err
#PBS -o blast_8.log
#PBS -q fila64
#PBS -l select=1:ncpus=8

cd $PBS_O_WORKDIR
/home/raonyguimaraes/venvs/blast_venv/bin/python blast_8cores.py
