import matplotlib.pyplot as plt
import seaborn as sea


data = [
    [1, 2, 3],
    [6, 8, 9],
    [1, 5, 7]
]

sea.heatmap(data, annot=True)
plt.show()