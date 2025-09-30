import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("E:/IT/AI/3/LR5/iris.csv")
sns.boxplot(x="Species", y="Petal.Length", data=df, palette="Set2")
plt.title("Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

sns.scatterplot(
    x="Sepal.Length",
    y="Sepal.Width",
    hue="Species",
    data=df,
    palette="Dark2",
    marker="o",
)
plt.title("Sepal Length vs Width by Species")
plt.show()

df["Petal.Width"].hist(by=df["Species"], bins=10, color="skyblue", edgecolor="black")
plt.suptitle("Petal Width Distribution by Species")
plt.show()

sns.violinplot(x="Species", y="Sepal.Width", data=df, palette="Pastel1")
plt.title("Sepal Width Density by Species")
plt.show()

means = df.groupby("Species").mean()
means.plot(kind="bar", color=["lightblue", "lightgreen", "salmon"])
plt.title("Average Measurements by Species")
plt.ylabel("Mean Value (cm)")
plt.show()

sns.pairplot(df, hue="Species", palette="husl")
plt.suptitle("Pairwise Relationships")
plt.show()

corr = df.drop("Species", axis=1).corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.show()
