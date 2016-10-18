import os

import math
from Bio import SeqIO

n = 10

different_sizes = [0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625]

# entries_50_percent = math.ceil(n_entries*0.5)

input_fasta = open('../input/R_2013_11_30_15_23_49_user_CTL-148-Metagenoma_Mauro_Eduardo2.CTLT_PGM.IonXpress_014_Sem28S2_COI2_18S2_Q20_good.fasta')

records = list(SeqIO.parse(input_fasta, "fasta"))

entries = len(records)
print(entries)
die()
for part in range(1,11):
    print(part)
# for size in different_sizes:
    
#     max_entries = math.ceil(entries*size)
#     print(max_entries)
    out_filename = "input/splits/input_blast_%s.fasta" % (part)
    output_handle = open(out_filename, "w")
    SeqIO.write(records[0:max_entries], output_handle, "fasta")
#     output_handle.close()



#generate 8 files with 6.25% from fasta
