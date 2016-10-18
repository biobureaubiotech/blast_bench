#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time

aws_key = "/home/raony/dev/biobureau/aws/biobureu01.pem"

output_folder = "/home/raony/dev/biobureau/blast_bench/output/"

IPS = ['52.207.218.32']

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
		time.sleep(300)
	else:
		send_email("HURRY UP BLAST IS OVER")
		blast_running = False
		# print("Recovering Results")
		# #get results
		# for i, ip in enumerate(IPS):
		# 	print(i,ip)
			# command = "scp -i %s -r ubuntu@%s:/blast/output %s" % (aws_key, ip, output_folder)
			