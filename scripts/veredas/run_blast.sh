#!/bin/bash -x

#SBATCH --job-name="Blast nt"
#SBATCH --ntasks 8
#SBATCH --nodes 1
#SBATCH --partition long
#SBATCH --mail-type=ALL
#SBATCH --mail-user=raonyguimaraes@gmail.com

name=$1

(time /home_cluster/bio712/spena/projetos/programs/blast/bin/blastn -db /home_cluster/bio712/spena/projetos/blast_db/nt -evalue 1e-05 -num_descriptions 100 -num_alignments 100 -query /home_cluster/bio712/spena/projetos/blast_bench/input/$name -out /tmp/$name.blast_output -num_threads 8) 2> /home_cluster/bio712/spena/projetos/blast_bench/output/$name.time.txt

cp /tmp/$name.blast_output /home_cluster/bio712/spena/projetos/blast_bench/output/

rm /tmp/$name.blast_output
