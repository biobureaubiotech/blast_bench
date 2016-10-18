#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time

aws_key = "/home/raony/dev/biobureau/aws/biobureu01.pem"

output_folder = "/home/raony/dev/biobureau/blast_bench/output/"

IPS = ['54.210.120.167', '54.210.120.182', '54.210.120.200', '54.210.120.226', '54.210.120.231', '54.210.120.34', '54.210.120.38', '54.210.120.55', '54.210.120.56', '54.210.120.74', '54.210.120.81', '54.210.120.84', '54.210.17.175', '54.210.30.224', '54.210.4.10', '54.210.4.50', '54.210.40.225', '54.210.72.232', '54.210.79.27', '54.88.135.164']

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
			