import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("E:/IT/AI/3/LR5/mtcars.csv")

# Convert categorical variables
df["gear"] = df["gear"].astype("category")
df["cyl"] = df["cyl"].astype("category")

# Map sizes based on cyl (e.g., 4=100, 6=200, 8=300)
size_map = {4: 100, 6: 200, 8: 300}
df["size"] = df["cyl"].map(size_map)

# Color map for gears
color_map = {3: "red", 4: "green", 5: "blue"}

# Create the plot
fig, ax = plt.subplots(figsize=(8, 6))
for gear_val in df["gear"].unique():
    subset = df[df["gear"] == gear_val]
    ax.scatter(
        subset["wt"],
        subset["mpg"],
        s=subset["size"],
        color=color_map[gear_val],
        label=f"gear={gear_val}",
        alpha=0.7,
    )

# Add legends (separate for cyl and gear)
cyl_legend = [
    plt.Line2D(
        [0],
        [0],
        marker="o",
        color="w",
        label=f"cyl={c}",
        markersize=10,
        markerfacecolor="black",
    )
    for c in [4, 6, 8]
]
gear_legend = [
    plt.Line2D(
        [0],
        [0],
        marker="o",
        color="w",
        label=f"gear={g}",
        markersize=10,
        markerfacecolor=color_map[g],
    )
    for g in [3, 4, 5]
]

ax.legend(
    handles=cyl_legend + gear_legend, title="cyl / factor(gear)", loc="upper right"
)
ax.set_xlabel("wt")
ax.set_ylabel("mpg")
ax.set_title("График №9")
plt.show()
