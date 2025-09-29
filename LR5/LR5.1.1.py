import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import numpy as np
from scipy.stats import gaussian_kde

# Load the dataset
df = pd.read_csv("E:/IT/AI/3/LR5/diamonds.csv")

# Define color grades in order
color_grades = ["D", "E", "F", "G", "H", "I", "J"]

# Create a custom colormap from purple to yellow to match the example
cmap = LinearSegmentedColormap.from_list(
    "custom",
    ["purple", "blue", "cyan", "green", "lime", "yellow", "gold"],
    N=len(color_grades),
)

# Create the plot
fig, ax = plt.subplots(figsize=(8, 6))
for i, color in enumerate(color_grades):
    subset = df[df["color"] == color]["carat"]
    if not subset.empty:
        subset.plot(
            kind="density",
            ax=ax,
            label=color,
            color=cmap(i / (len(color_grades) - 1)),
            linewidth=2,
        )

ax.set_xlabel("carat")
ax.set_ylabel("Density")
ax.set_title("График №5")
ax.legend(title="Color")
plt.xlim(0, 3)  # Match approximate range from example
plt.show()


