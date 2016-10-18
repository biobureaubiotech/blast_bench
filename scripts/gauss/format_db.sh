#!/bin/sh
#PBS -S /bin/sh
#PBS -N blastrun
#PBS -l nodes=1:ppn=24

# cd $PBS_O_WORKDIR
cd /home/u/raonygui/raonygui/blast_db
zcat nt.gz | /opt/local/blast/bin/mpiformatdb -i stdin -N 18 -t nt -p F