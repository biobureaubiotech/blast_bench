#!/bin/sh
#PBS -S /bin/sh
#PBS -N blastrun


##PBS -mae               # send an email if the job aborts (a) and when it ends (e)      
##PBS -M raonyguimaraes@gmail.com   # send the email to this address


#filas small.q, quantum.q, mid.q, siesta.q
#24 cores

#
# Digamos que seu executável esteja em /dados/$user/tmp e que seu
# script é submetido a partir desta pasta. Mesmo adotando-a como
# pasta de trabalho, o PBS nao transfere a ela a execuçao do
# script, senao pela invocaçao do comando abaixo

cd $PBS_O_WORKDIR

#Run BLAST FIRST SEQUENCE
#time /dados/raonygui/programs/ncbi-blast-2.3.0+/bin/blastn -db /dados/raonygui/blast/nt -evalue 1e-05 -query /home/u/raonygui/raonygui/blast_bench/input/input_blast_0_015625.fasta -out output_blast_0_015625.blast_output -num_threads 24

time /dados/raonygui/programs/ncbi-blast-2.3.0+/bin/blastn -db /dados/raonygui/blast/nt -evalue 1e-05 -query /home/u/raonygui/raonygui/blast_bench/input/input_blast_0_015625.fasta -out output_blast_0_015625_12cores.blast_output -num_threads 12

#time /dados/raonygui/programs/ncbi-blast-2.3.0+/bin/blastn -db /dados/raonygui/blast/nt -evalue 1e-05 -query /home/u/raonygui/raonygui/blast_bench/input/input_blast_0_03125.fasta -out output_blast_0_03125.fasta.blast_output -num_threads 24

