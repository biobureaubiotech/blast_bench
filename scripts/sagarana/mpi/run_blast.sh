#!/bin/sh
#Author raony
#PBS -N blastnr
#PBS -e blast.err
#PBS -o blast.log
#PBS -q fila64
#PBS -l select=3:ncpus=72
##PBS -l nodes=1:ppn=24

cd $PBS_O_WORKDIR

# export MPI_DIR=/opt/mpi/gnu/openmpi
# export PATH=/opt/mpi/gnu/openmpi/bin:$PATH
# export LD_LIBRARY_PATH=/opt/mpi/gnu/openmpi/lib:$LD_LIBRARY_PATH

# Unable to read mpiBLAST shared storage path from either .ncbirc or the MPIBLAST_SHARED environment variable.
# The mpiBLAST configuration in .ncbirc should look like:
# [mpiBLAST]
# Shared=/home/u/raonygui/raonygui/blast_db/shared
# Local=/tmp/
 # zcat nt.gz | /opt/local/blast/bin/mpiformatdb -i stdin -N 5 -t nt -p F
#Yeah!

# time /dados/raonygui/programs/ncbi-blast-2.3.0+/bin/blastn -db /dados/raonygui/blast/nt -evalue 1e-05 -query /home/u/raonygui/raonygui/blast_bench/input/input_blast_0_015625.fasta -out output_blast_0_015625_12cores.blast_output -num_threads 24
#mpiformatdb -N 16 -i nt -o T
# zcat nt.gz | /opt/local/blast/bin/mpiformatdb -i stdin -N 5 -t nt -p F

time mpiexec -n 3 /home/raonyguimaraes/programs/mpiblast/bin/mpiblast -p blastn -d /home/raonyguimaraes/blast_db/mpi/nt -i ../thread_experiment/input_blast_0_015625.fasta -o blast_results.txt