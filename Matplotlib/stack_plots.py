import matplotlib.pyplot as plt
days= [1,2,3,4,5]
sleeping = [6,7,8,9,3]
eating = [2,3,4,3,2]
working = [7,8,9,10,3]
playing = [8,6,7,5,4]

plt.plot([],[],color='m', label='Sleeping',linewidth=5)
plt.plot([],[],color='c', label='Eating',linewidth=5)
plt.plot([],[],color='r', label='Working',linewidth=5)
plt.plot([],[],color='k', label='Playing',linewidth=5)

plt.stackplot(days,sleeping,eating,working,playing,colors=['m','c','r','k'])

#plt.scatter(x,y, label='skitscat',color='k',marker ='X',s=100)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\n check it out')
plt.legend()

plt.show()
