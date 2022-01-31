import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
langs = ['C', 'C++', 'Java', 'Python', 'PHP']
students = [9,8,7,6,5]
ax.bar(langs,students)
plt.xlabel('x - axis') 
plt.show()
