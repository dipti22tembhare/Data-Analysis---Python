import matplotlib.pyplot as plt


group1 = [20, 10, 28, 78]
group2 = [30, 12, 66, 23]
group3 = [15, 18, 28, 30]

plt.boxplot([group1, group2, group3], labels=["Teju", "dipu","khushi" ])

plt.show()