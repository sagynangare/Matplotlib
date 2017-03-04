import matplotlib.pyplot as plt

population_ages= [22,33,55,43,45,78,54,66,85,66,54,23,11,23,12,21,32]
#ids = [x for x in range(len(population_ages))]
bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]
plt.hist(population_ages,bins,histtype='bar',rwidth=0.8,color='c')
#plt.bar(ids, population_ages)
#plt.bar(x2, y2, label='Bar2',color='c')

plt.xlabel('x')
plt.ylabel('y')
plt.title('hahahah\n check it out')
plt.legend()

plt.show()
