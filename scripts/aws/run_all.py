#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

aws_key = "/home/raony/dev/biobureau/aws/biobureu01.pem"

# IPS = ['52.207.229.105', '52.71.254.209', '52.201.247.70', '52.87.195.255', '52.91.5.237', '52.91.179.83', '52.90.212.146', '52.71.251.226', '52.201.250.110', '52.90.211.118']

IPS = ['54.208.248.8', '54.210.108.234', '54.210.113.123', '54.210.116.233', '54.210.117.57', '54.210.118.207', '54.210.118.209', '54.210.118.216', '54.210.118.221', '54.210.119.114', '54.210.119.125', '54.210.119.130', '54.210.119.154', '54.210.119.163', '54.210.119.78', '54.210.120.106', '54.210.120.111', '54.210.120.137', '54.210.120.143', '54.210.120.158'] 



input_folder = "/home/raony/dev/biobureau/blast_bench/input/Arquivos\ prontos\ pro\ Blast/splits"

output_folder = "/home/raony/dev/biobureau/blast_bench/output/"

file_prefix = "R_2013_11_30_15_23_49_user_CTL-148-Metagenoma_Mauro_Eduardo2.CTLT_PGM.IonXpress_003_Q20_TrimRL_AT_80pb_cdhit97.0"

for i, ip in enumerate(IPS):
	
	print(i,ip)

	# command = 'rsync -avz --partial --progress -e "ssh -i %s" ubuntu@%s:/blast/output %s' % (aws_key, ip, output_folder)
	command = "ssh -i %s ubuntu@%s pkill blastn" % (aws_key, ip)
	command = """ssh -o "StrictHostKeyChecking no" -i %s ubuntu@%s rm /blast/output/*""" % (aws_key, ip)

	os.system(command)
	