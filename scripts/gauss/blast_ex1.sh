#!/bin/sh
#PBS -S /bin/sh
#PBS -N blastrun

#PBS -l select=1:ncpus=24

cd $PBS_O_WORKDIR

time /dados/raonygui/programs/ncbi-blast-2.3.0+/bin/blastn -db /dados/raonygui/blast/nt -evalue 1e-05 -query /home/u/raonygui/raonygui/blast_bench/input/input_blast_0_015625.fasta -out output_blast_0_015625_12cores.blast_output -num_threads 24
