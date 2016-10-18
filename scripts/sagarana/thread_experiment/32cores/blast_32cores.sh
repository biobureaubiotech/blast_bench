#!/bin/sh
#Author raony
#PBS -N blast_nt32
#PBS -e blast_32.err
#PBS -o blast_32.log
#PBS -q fila64
#PBS -l select=1:ncpus=32

cd $PBS_O_WORKDIR
/home/raonyguimaraes/venvs/blast_venv/bin/python blast_32cores.py
