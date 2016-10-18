
from os import listdir
from os.path import isfile, join
from collections import OrderedDict

path = '/home/raony/dev/biobureau/blast_bench/output/output/time'


onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

# print onlyfiles


times = OrderedDict()

for file in onlyfiles:
	read_file = open("%s/%s" % (path, file))
	for line in read_file:
		# print line
		if line.startswith("real"):
			time = line.split('\t')[1].strip()
			# print time
			times[file] = time

for file in sorted(times.keys()):
	print file, times[file]	