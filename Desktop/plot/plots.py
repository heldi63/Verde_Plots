import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Verde Survey.csv")

#age distribution
age_counts = df["What is your age range?"].value_counts()

#shopping frequency distribution
shopping_freq = df["How often do you shop for new clothes?"].value_counts()

#most popular clothing colors
color_counts = df["Favorite color for clothing:"].value_counts()

#percentage considering environmental factors
eco_friendly_counts = df["Does a product being environmentally friendly affect your purchase decision?"].value_counts(normalize=True) * 100


#plot results
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

#age distribution
age_counts.plot(kind="bar", ax=axes[0, 0], color="skyblue", edgecolor="black")
axes[0, 0].set_title("Age Distribution of Respondents")
axes[0, 0].set_ylabel("Count")


#shopping frequency
shopping_freq.plot(kind="bar", ax=axes[0, 1], color="lightcoral", edgecolor="black")
axes[0, 1].set_title("Shopping Frequency")
axes[0, 1].set_ylabel("Count")

#clothing color preference
color_counts.plot(kind="bar", ax=axes[1, 0], color="mediumseagreen", edgecolor="black")
axes[1, 0].set_title("Most Popular Clothing Colors")
axes[1, 0].set_ylabel("Count")

#environmental considerations
eco_friendly_counts.plot(kind="pie", autopct='%1.1f%%', ax=axes[1, 1], colors=["gold", "lightgray"], startangle=90)
axes[1, 1].set_title("Environmental Considerations in Purchasing")

plt.tight_layout()
plt.show()
