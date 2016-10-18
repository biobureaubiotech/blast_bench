#!/usr/bin/env python
# -*- coding: utf-8 -*-
from threading import Thread, Event
import time
# import threading
import psutil
import datetime
import os
import subprocess
from subprocess import PIPE,Popen


# sizes = [0.015625, 0.03125, 0.0625, 0.125, 0.25, 0.5]
size = 0.015625
n_cores = 32

# command = "blastn -db nt -evalue 1e-05 -query arquivo.fasta -out arquivoblast"

#monitor cpu and memory
# [1:09 PM, 3/14/2016] Mauro: Monitorar o desempenho das máquinas (se alcançam o máximo de CPU ou memória; se travam)
# [1:10 PM, 3/14/2016] Mauro: E verificar a relação (tamanho, no de reads, no de hits) entre os arquivos de entrada e saída. 

# Raony, sugiro:
# 1) Pega 1 dos arquivos 'good', quebra ele em diferentes tamanhos: 50, 25, 12.5, 6.25, 3.125 1,5625% do original
# 2) Roda cada um em um webservice diferente, em instâncias padrão da AWS de aproximadamente 8, 20 e 50 Gb de RAM, com o processamento correspondente.
# 3) monitore: tempo de processamento em cada instância, uso médio da CPU e da RAM, tamanho do arquivo de saída. 
# 4) quando fragmentar o arquivo inicial em pedaços de 6,25% do total, coloque 8 deles (~50%) na fila do mesmo webservice pra monitorar o tempo de execução e comparar com 1 arquivo de 50%



file_prefix = str(size).replace('.','_')

output = open("monitor_%s.%s_cores.log" % (file_prefix, n_cores), "w")

def monitor(arg1, stop_event):
    
    while(not stop_event.is_set()):

        time.sleep(60)
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
# for size in sizes:
    
print("Running BLAST for %s \n" % (size))

output.writelines("Running BLAST for %s \n" % (size))

filename = "input_blast_%s.fasta" % (file_prefix)
output_file = "/tmp/output_%s.%s_cores.blast_output" % (file_prefix, n_cores)

command = "time /home/raonyguimaraes/programs/ncbi-blast-2.3.0+/bin/blastn -db /home/raonyguimaraes/blast_db/nt -evalue 1e-05 -query ../%s -out %s -num_threads %s" % (filename, output_file, n_cores)


proc = Popen(command.split(), stdout=PIPE)
out = proc.communicate()[0]
print(out)
output.writelines(out)

command = "cp %s ." % (output_file)
proc = Popen(command.split(), stdout=PIPE)
out = proc.communicate()[0]

command = "rm %s" % (output_file)
proc = Popen(command.split(), stdout=PIPE)
out = proc.communicate()[0]

#stop monitor
t2_stop.set()
monitor.join()
output.close()