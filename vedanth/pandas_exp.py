import pandas as pd
import numpy as np

# read csv
df = pd.read_csv(r"C:\Vedanth_Space\Python\vedanth\people.csv")

print("\n--- original data ---")
print(df)

# fix data types
df["DOB"] = pd.to_datetime(df["DOB"])
df["score"] = pd.to_numeric(df["score"], errors="raise")

# today date
today = pd.Timestamp.today().normalize()

# age calculation
df["age"] = np.where(
    (df["DOB"].dt.month > today.month) |
    ((df["DOB"].dt.month == today.month) & (df["DOB"].dt.day > today.day)),
    today.year - df["DOB"].dt.year - 1,
    today.year - df["DOB"].dt.year
)

print("\n--- data with age ---")
print(df)

# sorting
print("\n--- sort by score (ascending) ---")
print(df.sort_values("score"))

print("\n--- sort by score (descending) ---")
print(df.sort_values("score", ascending=False))

print("\n--- sort by age (ascending) ---")
print(df.sort_values("age"))

print("\n--- sort by age (descending) ---")
print(df.sort_values("age", ascending=False))

# score stats
print("\n--- score stats ---")
print("mean   :", df["score"].mean())
print("median :", df["score"].median())
print("mode   :", df["score"].mode().tolist())
print("min    :", df["score"].min())
print("max    :", df["score"].max())
print("std    :", df["score"].std())
# Exp stats
print("\n--- Experience stats ---")
print("mean   :", df["experience"].mean())
print("median :", df["experience"].median())
print("mode   :", df["experience"].mode().tolist())
print("min    :", df["experience"].min())
print("max    :", df["experience"].max())
print("std    :", df["experience"].std())

print("\n--- describe ---")
print(df["score"].describe())
