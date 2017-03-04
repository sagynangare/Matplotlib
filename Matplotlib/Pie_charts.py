import matplotlib.pyplot as plt
days= [1,2,3,4,5]
sleeping = [6,7,8,9,3]
eating = [2,3,4,3,2]
working = [7,8,9,10,3]
playing = [8,6,7,5,4]

slices=[7,2,2,13]
activities = ['sleeping', 'eating','working','playing']
cols = ['c','m','r','b']
plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow= True,
        explode=(0,0.1,0,0),
        autopct='%1.1f%%')

#plt.xlabel('x')
#plt.ylabel('y')
plt.title('Interesting Graph\n check it out')
plt.legend()

plt.show()
