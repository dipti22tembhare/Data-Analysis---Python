import matplotlib.pyplot as plt
import seaborn as sea

x = [1, 2, 5, 7]
y = [3, 9, 7, 5]
# sea.scatterplot(x=x, y=y)
# sea.histplot(x=x, y=y)
# sea.lineplot(x=x, y=y)
# sea.barplot(x=x, y=y)
# plt.title("school")
# plt.xlabel("marks")
# plt.ylabel("marks")
# plt.show()

# line chart
plt.plot(x, y, marker='o', linestyle=':', color = 'red')
plt.title("school")
plt.xlabel("marks")
plt.ylabel("marks")
plt.show()


