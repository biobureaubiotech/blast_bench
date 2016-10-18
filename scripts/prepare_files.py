import os

import math
from Bio import SeqIO


#grep -c ">" R_2013_11_30_15_23_49_user_CTL-148-Metagenoma_Mauro_Eduardo2.CTLT_PGM.IonXpress_014_Sem28S2_COI2_18S2_Q20_good.fasta



# n_entries = 308146
#split files in 

# 1) Pega 1 dos arquivos 'good', quebra ele em diferentes tamanhos: 50, 25, 12.5, 6.25, 3.125 1,5625% do original

different_sizes = [0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625]
# entries_50_percent = math.ceil(n_entries*0.5)

input_fasta = open('R_2013_11_30_15_23_49_user_CTL-148-Metagenoma_Mauro_Eduardo2.CTLT_PGM.IonXpress_014_Sem28S2_COI2_18S2_Q20_good.fasta')



records = list(SeqIO.parse(input_fasta, "fasta"))
# # print(len(records))
entries = len(records)

# # print(entries)
for size in different_sizes:
    
    max_entries = math.ceil(entries*size)
    print(max_entries)
    out_filename = "input/input_blast_%s.fasta" % (str(size).replace('.','_'))
    output_handle = open(out_filename, "w")
    SeqIO.write(records[0:max_entries], output_handle, "fasta")
    output_handle.close()


#generate 8 files with 6.25% from fasta

start = 0
end = 19260
n_entries = 19260
for i in range(1,9):

    print(start, end)
    start = end+1
    end = start + n_entries
    filename = "input/input_blast_0_0625_%s.fasta" % (i)
    output_handle = open(filename, "w")
    SeqIO.write(records[start:end], output_handle, "fasta")
    output_handle.close()
