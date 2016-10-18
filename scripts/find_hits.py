import os
import subprocess

blast_results = [
'R_2013_11_30_15_23_49_user_CTL-148-Metagenoma_Mauro_Eduardo2.CTLT_PGM.IonXpress_001_Q20_TrimRL_AT_80pb_cdhit97.blast_output', 
'R_2013_11_30_15_23_49_user_CTL-148-Metagenoma_Mauro_Eduardo2.CTLT_PGM.IonXpress_002_Q20_TrimRL_AT_80pb_cdhit97.blast_output', 
'R_2013_11_30_15_23_49_user_CTL-148-Metagenoma_Mauro_Eduardo2.CTLT_PGM.IonXpress_003_Q20_TrimRL_AT_80pb_cdhit97.blast_output', 
'R_2013_11_30_15_23_49_user_CTL-148-Metagenoma_Mauro_Eduardo2.CTLT_PGM.IonXpress_004_Q20_TrimRL_AT_80pb_cdhit97.blast_output', 
'R_2013_11_30_15_23_49_user_CTL-148-Metagenoma_Mauro_Eduardo2.CTLT_PGM.IonXpress_010_Q20_TrimRL_AT_80pb_cdhit97.blast_output', 
'R_2013_11_30_15_23_49_user_CTL-148-Metagenoma_Mauro_Eduardo2.CTLT_PGM.IonXpress_011_Q20_TrimRL_AT_80pb_cdhit97.blast_output', 
'R_2013_11_30_15_23_49_user_CTL-148-Metagenoma_Mauro_Eduardo2.CTLT_PGM.IonXpress_012_Q20_TrimRL_AT_80pb_cdhit97.blast_output', 
'R_2013_11_30_15_23_49_user_CTL-148-Metagenoma_Mauro_Eduardo2.CTLT_PGM.IonXpress_013_Q20_TrimRL_AT_80pb_cdhit97.blast_output']

print blast_results

species_file = open('../EspeciesBuscaHitsBlast.csv')
# for line in species_file:
#         print line

species = {}
for specie in species_file:
        species[specie.strip()]=0

for file in blast_results:
    print file
    for specie in species:
        command = 'grep -c "%s" ../input/%s' % (specie, file)
        counter=os.popen(command).read()
        print specie, counter
        #species[specie]+=int(counter)

for specie in species:
        print specie, species[specie]
