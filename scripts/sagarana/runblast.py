#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author raony
#PBS -N blastnr
#PBS -e blast.err
#PBS -o blast.log
#PBS -q fila64
#PBS -l select=1:ncpus=64


from threading import Thread, Event
import time
# import threading
import psutil
import datetime
import os
import subprocess
from subprocess import PIPE,Popen

# command = "blastn -db nt -evalue 1e-05 -query arquivo.fasta -out arquivoblast"

#monitor cpu and memory
# [1:09 PM, 3/14/2016] Mauro: Monitorar o desempenho das máquinas (se alcançam o máximo de CPU ou memória; se travam)
# [1:10 PM, 3/14/2016] Mauro: E verificar a relação (tamanho, no de reads, no de hits) entre os arquivos de entrada e saída. 

# Raony, sugiro:
# 1) Pega 1 dos arquivos 'good', quebra ele em diferentes tamanhos: 50, 25, 12.5, 6.25, 3.125 1,5625% do original
# 2) Roda cada um em um webservice diferente, em instâncias padrão da AWS de aproximadamente 8, 20 e 50 Gb de RAM, com o processamento correspondente.
# 3) monitore: tempo de processamento em cada instância, uso médio da CPU e da RAM, tamanho do arquivo de saída. 
# 4) quando fragmentar o arquivo inicial em pedaços de 6,25% do total, coloque 8 deles (~50%) na fila do mesmo webservice pra monitorar o tempo de execução e comparar com 1 arquivo de 50%

output = open("monitor.log", "w")

def monitor(arg1, stop_event):
    
    while(not stop_event.is_set()):
        cpu = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory()

        output_list = []
        output_list.append("DATE:"+str(datetime.datetime.now()))
        used = mem.total - mem.available
        output_list.append("CPU:"+str(cpu))
        output_list.append("MEMORY:"+str(int(used / 1024 / 1024))+" MB")
        output.writelines("\t".join(output_list)+"\n")

        print(output_list)



t2_stop= Event()
monitor = Thread(target=monitor,  args=(2, t2_stop))

monitor.start()

#run blasts
sizes = [0.015625, 0.03125, 0.0625, 0.125, 0.25, 0.5]

for size in sizes:
    
    print("Running BLAST for %s \n" % (size))

    output.writelines("Running BLAST for %s \n" % (size))

    file_prefix = str(size).replace('.','_')
    filename = "input_blast_%s.fasta" % (file_prefix)
    command = "time blastn -db nt -evalue 1e-05 -query %s -out blast_output_%s.fasta" % (filename, file_prefix)
    command = "time /home/raonyguimaraes/programs/ncbi-blast-2.3.0+/bin/blastn -db /home/raonyguimaraes/blast_db/nt -evalue 1e-05 -query /home/raonyguimaraes/experiment/blast_bench/input/input_blast_0_015625.fasta -out /tmp/output_blast_0_015625.blast_output -num_threads 64"
    # command = """echo "blast" """
    command = "sleep 2"
    #out = subprocess.check_output(command.split())
    proc = Popen(['ls', '-l'], stdout=PIPE)
    out = proc.communicate()[0].split()
    print out
    #print(out.decode("utf-8") )
    output.writelines(out)


#teste com 8 arquivos 0.0625
size = 0.0625
print("Running 8 BLASTS for %s \n" % (size))
output.writelines("Running 8 BLASTS for %s \n" % (size))

for i in range(1,9):
    print(i)
    output.writelines(str(i)+"\n")
    file_prefix = str(size).replace('.','_')
    filename = "test_blast_%s.fasta" % (file_prefix)
    command = "time blastn -db nt -evalue 1e-05 -query %s -out blast_output_%s.fasta" % (filename, file_prefix)
    command = "sleep 2"
    #out = subprocess.check_output(command.split())
    #print(out.decode("utf-8") )
    #output.writelines(out)

#stop monitor
t2_stop.set()
monitor.join()
output.close()


