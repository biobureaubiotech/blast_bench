#!/bin/sh
#Author raony
#PBS -N blast
#PBS -e blast.err
#PBS -o blast.log
##PBS -q fila64
##PBS -l select=1:ncpus=64

echo "TESTANDO123"
cd /home/raonyguimaraes/experiment/blast_bench/scripts/
#source /home/raonyguimaraes/venvs/blast/bin/activate
source /home/raonyguimaraes/programs/virtualenv-15.0.0/blast/bin/activate
which python
python runblast.py
# /programs/blastall -p blastx -d /databases/nr -i /home/miguel/pampulha.fasta -o
# /tmp/resultado -e 1e-5 -m 8 -n F -a 64
# mv /tmp/resultado /home/miguel/resultado
