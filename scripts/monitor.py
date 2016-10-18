#monitor cpu usage and memory
# import psutil
# for x in range(3):
#     print(psutil.cpu_percent(interval=1, percpu=True))

import psutil
import time
import datetime

output = open("monitor.log", "w")
while True:
    # time.sleep(1)
    cpu = psutil.cpu_percent(interval=5)
    mem = psutil.virtual_memory()

    output_list = []
    output_list.append("DATE:"+str(datetime.datetime.now()))
    # print()
    # print "Clock"
    used = mem.total - mem.available
    output_list.append("CPU:"+str(cpu))
    # out_string += 
        # print("CPU:"+str(cpu))
    # out_string += 
    output_list.append("MEMORY:"+str(int(used / 1024 / 1024))+" MB")
    # print("MEMORY:"+str(int(used / 1024 / 1024))+"MB")
    output.writelines("\t".join(output_list)+"\n")

    print(output_list)
