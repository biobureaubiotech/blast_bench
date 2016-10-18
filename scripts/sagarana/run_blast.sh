#!/bin/sh
#Author raony
#PBS -N blastnt
#PBS -e blast.err
#PBS -o blast.log
#PBS -q fila64
#PBS -l select=1:ncpus=64
cd $PBS_O_WORKDIR

name=${name}
echo $name

# time blastn -db /blast/blastdb/nt -evalue 1e-05 -num_descriptions 100 -num_alignments 100 -query /blast/input/$name -out /blast/output/$name.blast_output -num_threads 8 &

# ( time blastn -db /blast/blastdb/nt -evalue 1e-05 -num_descriptions 100 -num_alignments 100 -query /blast/input/$name -out /blast/output/$name.blast_output -num_threads 8 ) 2> /blast/output/$name.time.txt

( time /home/raonyguimaraes/programs/ncbi-blast-2.3.0+/bin/blastn -db /home/raonyguimaraes/blast_db/nt -evalue 1e-05 -num_descriptions 100 -num_alignments 100 -query /home/raonyguimaraes/experiment/blast_bench/input/$name -out /tmp/$name.blast_output -num_threads 64 ) 2> /home/raonyguimaraes/experiment/blast_bench/output/$name.time.txt

cp /tmp/$name.blast_output /home/raonyguimaraes/experiment/blast_bench/output/

rm /tmp/$name.blast_output
