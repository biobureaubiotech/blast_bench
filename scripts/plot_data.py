import matplotlib.pyplot as plt


# These are the "Tableau 20" colors as RGB.    
tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),    
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),    
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),    
             (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),    
             (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]    
  
# Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.    
for i in range(len(tableau20)):    
    r, g, b = tableau20[i]    
    tableau20[i] = (r / 255., g / 255., b / 255.)    


# Remove the plot frame lines. They are unnecessary chartjunk.    
ax = plt.subplot(111)    
ax.spines["top"].set_visible(False)    
# ax.spines["bottom"].set_visible(False)    
ax.spines["right"].set_visible(False)    
# ax.spines["left"].set_visible(False)    
  
# Ensure that the axis ticks only show up on the bottom and left of the plot.    
# Ticks on the right and top of the plot are generally unnecessary chartjunk.    
ax.get_xaxis().tick_bottom()    
ax.get_yaxis().tick_left()    


# Make sure your axis ticks are large enough to be easily read.    
# You don't want your viewers squinting to read your plot.    
plt.yticks(range(0, 500, 20), [str(x) for x in range(0, 500, 20)], fontsize=10)
plt.xticks(range(0, 65, 5), [str(x) for x in range(0, 65, 5)], fontsize=10)    
# plt.xticks(fontsize=10)    


plt.xlabel('Cores (cpus)')
plt.ylabel('Tempo (min)')
plt.title('Blast Cores vs Tempo')

cores_list = [4,8,12,24,32,48,64]
time_list = [457, 306, 272, 94, 125, 123, 130]
plt.plot(cores_list, time_list, color=tableau20[1], lw=2.5, linestyle='-')
plt.plot(cores_list, time_list, color=tableau20[0], lw=2.5, linestyle='None', marker='o')

plt.axis([0, 70, 0, 500])
plt.show()
plt.savefig("Blast Cores vs Tempo.png", bbox_inches="tight")  
