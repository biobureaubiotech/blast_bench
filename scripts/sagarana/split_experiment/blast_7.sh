#!/bin/sh
#Author raony
#PBS -N blast_nt7
#PBS -e blast_7.err
#PBS -o blast_7.log
#PBS -q fila64
#PBS -l select=1:ncpus=24

cd $PBS_O_WORKDIR

time /home/raonyguimaraes/programs/ncbi-blast-2.3.0+/bin/blastn -db /home/raonyguimaraes/blast_db/nt -evalue 1e-5 -query splits/R_2013_11_30_15_23_49_user_CTL-148-Metagenoma_Mauro_Eduardo2.CTLT_PGM.IonXpress_014_Sem28S2_COI2_18S2_Q20_good.06.fasta -out /home/raonyguimaraes/experiment/blast_bench/output/blast_output_7.out -num_threads 24