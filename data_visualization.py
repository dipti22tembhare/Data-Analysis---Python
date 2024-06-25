import matplotlib.pyplot as plt
# %matplotlib inline

# ******* used to create stastics**********

# plt.plot([1,2,3],[2,7,9])


plt.title("MyPage")
plt.xlabel("Students")
plt.ylabel("Marks")

x = [20,0, 70, 88]
y = [11, 7, 80, 60]
x1 = [1, 4, 2, 9]
y1 = [44, 9, 2, 5]
plt.plot(x,y)
plt.plot(x1,y1)
plt.show()