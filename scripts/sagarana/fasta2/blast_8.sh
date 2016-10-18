#!/bin/sh
#Author raony
#PBS -N blast_nt8
#PBS -e blast_8.err
#PBS -o blast_8.log
#PBS -q fila64
#PBS -l select=1:ncpus=24

cd $PBS_O_WORKDIR

time /home/raonyguimaraes/programs/ncbi-blast-2.3.0+/bin/blastn -db /home/raonyguimaraes/blast_db/nt -evalue 1e-5 -query input/R_2013_11_30_15_23_49_user_CTL-148-Metagenoma_Mauro_Eduardo2.CTLT_PGM.IonXpress_002_Q20_TrimRL_AT_80pb_cdhit97.07 -out output/R_2013_11_30_15_23_49_user_CTL-148-Metagenoma_Mauro_Eduardo2.CTLT_PGM.IonXpress_002_Q20_TrimRL_AT_80pb_cdhit97.07.blast_output -num_threads 24