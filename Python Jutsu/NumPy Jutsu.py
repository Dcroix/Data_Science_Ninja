# NumPy Jutsu
# A demonstration of useful Numpy functions for Data Science
import pandas as pd
import numpy as np

# --- Create a sample DataFrame where we can apply Numpy ---
data = {
    "Ninja": ["Ryu", "Ken", "Akira", "Yumi", "Hiro"],
    "Speed": [8.5, 7.2, 9.1, 6.8, 8.0],
    "Strength": [7.0, 8.5, 6.5, 7.8, 9.0],
    "Agility": [8.2, 7.8, 9.0, 6.5, 8.3]
}

df = pd.DataFrame(data)
print("\n--- Ninja Scores ---")
print(df)

# --- Useful NumPy Function 1: Convert numerical columns to NumPy array ---
scores = df[["Speed", "Strength", "Agility"]].values

# --- Useful NumPy Function 2: Mean, Median, Std, Max, Min ---
mean_scores = np.mean(scores, axis=0)
median_scores = np.median(scores, axis=0)
std_scores = np.std(scores, axis=0)
best_scores = np.max(scores, axis=0)
weakest_scores = np.min(scores, axis=0)

print("\nMean Scores:", np.round(mean_scores, 2))
print("Median Scores:", median_scores)
print("Standard Deviation:", np.round(std_scores,2))
print("Best Scores:", best_scores)
print("Weakest Scores:", weakest_scores)

# --- Useful NumPy Function 3: Identify Top Ninjas Per Skill ---
fastest_idx = np.argmax(scores[:,0])
strongest_idx = np.argmax(scores[:,1])
most_agile_idx = np.argmax(scores[:,2])

print("\nFastest Ninja:", df['Ninja'][fastest_idx])
print("Strongest Ninja:", df['Ninja'][strongest_idx])
print("Most Agile Ninja:", df['Ninja'][most_agile_idx])

# --- Useful NumPy Function 4: Total Score Per Ninja ---
df["Total"] = np.sum(scores, axis=1)
print("\n--- Ninja Total Scores ---")
print(df)

# --- Useful NumPy Function 7: Conditional Selection Using np.where ---
top_ninjas_idx = np.where(df["Total"] > 24)[0]
print("\nTop Ninjas (Total > 24):", df["Ninja"][top_ninjas_idx].tolist())
