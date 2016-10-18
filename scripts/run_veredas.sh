#!/bin/bash -x

#SBATCH --job-name="Blast_Bench"
###SBATCH --ntasks 8
####SBATCH --nodes 1
#SBATCH --partition long
#SBATCH --mail-type=ALL
#SBATCH --mail-user=raonyguimaraes@gmail.com

time /home_cluster/bio712/spena/projetos/programs/ncbi-blast-2.3.0+/bin/blastn -db /home_cluster/bio712/spena/projetos/blast/nt -evalue 1e-05 -query /home_cluster/bio712/spena/projetos/blast_bench/input/input_blast_0_015625.fasta -out output_blast_0_015625.blast_output -num_threads 8
