#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time

aws_key = "/home/raony/dev/biobureau/aws/biobureu01.pem"

output_folder = "/home/raony/dev/biobureau/blast_bench/output/"

IPS = ['52.201.247.70', '52.201.250.110', '52.207.229.105', '52.207.229.120', '52.23.247.71', '52.71.251.226', '52.71.254.209', '52.87.195.255', '52.90.124.181', '52.90.131.131', '52.90.180.183', '52.90.204.141', '52.90.211.118', '52.90.212.146', '52.90.212.57', '52.90.235.231', '52.90.240.106', '52.91.110.38', '52.91.179.83', '52.91.5.237', '54.152.61.32', '54.165.121.124', '54.165.30.11', '54.172.250.40', '54.172.68.180', '54.173.109.255', '54.173.175.241', '54.174.43.45', '54.85.0.73', '54.86.160.22', '54.88.212.41']

import smtplib

def send_email(msg):

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login("raony.cardenas@biobureau.com.br", "")
	 
	# msg = "HURRY UP BLAST IS OVER!"
	server.sendmail("raony.cardenas@biobureau.com.br", "raonyguimaraes@gmail.com", msg)
	server.quit()



blast_running = True

while(blast_running):
	#check if blast is running
	blast_finished = True
	for i, ip in enumerate(IPS):
		print(i,ip)
		command = "ssh -i %s ubuntu@%s pgrep -x blastn" % (aws_key, ip)
		result = os.system(command)
		# print("Result", result)
		# print(result)
		if result == 0:
			print("Blast is running!")
			blast_finished = False
		else:
			print("Blast is not running!")
			print("Recovering Results")
			command = 'rsync -avz --partial --progress -e "ssh -i %s" ubuntu@%s:/blast/output %s' % (aws_key, ip, output_folder)
			os.system(command)
	
		#if result == 0 means it still running

	if not blast_finished:
		print("Some instances are still running blast")
		time.sleep(600)
	else:
		send_email("HURRY UP BLAST IS OVER")
		blast_running = False
		# print("Recovering Results")
		# #get results
		# for i, ip in enumerate(IPS):
		# 	print(i,ip)
			# command = "scp -i %s -r ubuntu@%s:/blast/output %s" % (aws_key, ip, output_folder)
			