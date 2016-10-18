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

cd $PBS_O_WORKDIR/output

# cd /home/u/raonygui/raonygui/blast_bench/scripts/
#
# Linha de disparo de um programa com suporte a processamento
# distribuı́do (note que se o sı́mbolo ./ nao for prefixado ao nome
# do seu executável, é necessário entao fornecer o caminho absoluto
# do arquivo).
# mpiexec ./programa_mpi
# echo $PBS_O_WORKDIR 

cat /proc/cpuinfo > blah_output.txt
cat /proc/cpuinfo > output123.txt
grep -c ^processor /proc/cpuinfo
