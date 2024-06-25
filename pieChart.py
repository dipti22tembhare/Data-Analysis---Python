import matplotlib.pyplot as plt


size=[22, 56, 78, 67]
labels = ["dipu", "chun", "khushi", "gudiya"]
colors = ["red", "blue", "green", "pink"]

plt.figure(figsize=(4,4))
plt.pie(size, labels=labels, colors=colors, autopct = '%1.1f%%', startangle=140)

plt.show()