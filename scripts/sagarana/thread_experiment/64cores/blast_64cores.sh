#!/bin/sh
#Author raony
#PBS -N blast_nt64
#PBS -e blast_64.err
#PBS -o blast_64.log
#PBS -q fila64
#PBS -l select=1:ncpus=64

cd $PBS_O_WORKDIR
/home/raonyguimaraes/venvs/blast_venv/bin/python blast_64cores.py
