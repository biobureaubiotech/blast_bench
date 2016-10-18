#!/bin/sh
#Author raony
#PBS -N blastnr
#PBS -e blast.err
#PBS -o blast.log
#PBS -q fila64
#PBS -l select=1:ncpus=4
cd $PBS_O_WORKDIR

# source /home/raonyguimaraes/venvs/blast_venv/bin/activate
/home/raonyguimaraes/venvs/blast_venv/bin/python blast_4cores.py
#time /home/raonyguimaraes/programs/ncbi-blast-2.3.0+/bin/blastn -db /home/raonyguimaraes/blast/nt -evalue 1e-05 -query /home/raonyguimaraes/experiment/blast_bench/input/input_blast_0_015625.fasta -out /tmp/output_blast_0_015625.blast_output -num_threads 64

#mv /tmp/output_blast_0_015625.blast_output /home/raonyguimaraes/experiment/blast_bench/output/