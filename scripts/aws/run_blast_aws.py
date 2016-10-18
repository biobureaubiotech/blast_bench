#!/usr/bin/env python
# -*- coding: utf-8 -*-

#get a fasta file, split in n=10 parts and submit each part to a different host

import os
import argparse

aws_key = "/home/raony/dev/biobureau/aws/biobureu01.pem"

# IPS = ['52.207.229.105', '52.71.254.209', '52.201.247.70', '52.87.195.255', '52.91.5.237', '52.91.179.83', '52.90.212.146', '52.71.251.226', '52.201.250.110', '52.90.211.118']

# IPS = ['52.90.235.231', '54.152.61.32', '52.90.212.57', '52.90.240.106', '54.85.0.73', '52.90.180.183']

# IPS = ['52.207.229.105', '52.71.254.209', '52.201.247.70', '52.87.195.255', '52.91.5.237', '52.91.179.83', '52.90.212.146', '52.71.251.226', '52.201.250.110', '52.90.211.118', '52.90.235.231', '54.152.61.32', '52.90.212.57', '52.90.240.106', '54.85.0.73', '52.90.180.183']


IPS = ['54.208.248.8', '54.210.108.234', '54.210.113.123', '54.210.116.233', '54.210.117.57', '54.210.118.207', '54.210.118.209', '54.210.118.216', '54.210.118.221', '54.210.119.114', '54.210.119.125', '54.210.119.130', '54.210.119.154', '54.210.119.163', '54.210.119.78', '54.210.120.106', '54.210.120.111', '54.210.120.137', '54.210.120.143', '54.210.120.158'] 

parser = argparse.ArgumentParser()
parser.add_argument("-i", "-input", help="FASTA input file")
# parser.add_argument("-o", "-output", help="Output folder")

args = parser.parse_args()

# print(args.i)

input_file = args.i.replace(" ", "\ ")

dir_path = os.path.dirname(input_file)#.replace(" ", "\ ")
# print(dir_path)

nparts = len(IPS)

base_name = os.path.basename(input_file)

#split files
command = "pyfasta split -n %s %s" % (nparts, input_file)
os.system(command)

command = "rm -rf %s/splits" % (dir_path)
os.system(command)

command = "mkdir %s/splits" % (dir_path)
os.system(command)
#move files to folder splits
command = "mv %s.* %s/splits/" % (input_file, dir_path)
os.system(command)


input_folder = "%s/splits" % (dir_path)
file_prefix = "%s." % (base_name)

for i, ip in enumerate(IPS):
	
	print(i,ip)
	
	if nparts > 11:
		input_file = "%s%02d" % (file_prefix, i)
	else:
		input_file = "%s%01d" % (file_prefix, i)
	# print(input_file)

	#create folder
	command = "ssh -i %s ubuntu@%s sudo mkdir /blast/input" % (aws_key, ip)
	os.system(command)
	command = "ssh -i %s ubuntu@%s sudo chown ubuntu:root /blast/input" % (aws_key, ip)
	os.system(command)

	command = "ssh -i %s ubuntu@%s sudo mkdir /blast/output" % (aws_key, ip)
	os.system(command)
	
	command = "ssh -i %s ubuntu@%s sudo chown ubuntu:root /blast/output" % (aws_key, ip)
	os.system(command)
	
	#transfer files to instance
	command = "scp -i %s %s/%s ubuntu@%s:/blast/input" % (aws_key, input_folder, input_file, ip)
	# print(command)
	os.system(command)
	
	#copy script
	command = "scp -i %s run_blast.sh ubuntu@%s:/blast/input" % (aws_key, ip)
	os.system(command)

	#run it
	command = 'ssh -i %s ubuntu@%s bash /blast/input/run_blast.sh %s &' % (aws_key, ip, input_file)
	# print(command)
	os.system(command)
	# die()