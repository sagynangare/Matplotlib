import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [5,2,4,3,2,3,5,6]
plt.scatter(x,y, label='skitscat',color='k',marker ='X',s=100)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\n check it out')
plt.legend()

plt.show()
