import matplotlib.pyplot as plt

data = [1, 2, 4, 66, 7, 7 , 8, 9, 7, 5, 5, 5]

plt.hist(data, bins = 5, color='blue', edgecolor="black")
plt.title("fruits")
plt.xlabel("veg")
plt.ylabel("non-veg")
plt.show()