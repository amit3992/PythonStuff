import matplotlib.pyplot as plt

# Basic plot
#plt.plot([1,2,3],[5,7,4])
#plt.show()

x = [1,2,3]
y = [5,7,4]

x2 = [1,2,3]
y2 = [10,14,8]

plt.plot(x,y, label = "First plot")
plt.plot(x2,y2, label = "Second plot")

plt.xlabel('Plot Number')
plt.ylabel('Important var')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
