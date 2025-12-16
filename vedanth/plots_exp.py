import matplotlib.pyplot as plt

# Example data (must exist)
customers = ["Alice", "Bob", "Charlie", "Diana"]
transaction_amounts = [250, 400, 150, 200]

plt.figure(figsize=(6, 6))

plt.pie(
    transaction_amounts,
    labels=customers,
    autopct="%1.1f%%",
    startangle=90,
    shadow=True
)

plt.title("Transaction Amount Distribution")

plt.show()
plt.pie()


import pandas as pd
import matplotlib.pyplot as plt
 
data = {
    "month": ["jan", "feb", "mar", "apr", "may", "june"],
    "sales": [20000, 12000, 23000, 63322, 5000, 5700]
}
 
df = pd.DataFrame(data)
print(df)
 
plt.pie(
    df["sales"],
    labels=df["month"],
    autopct="%1.1f%%",
    startangle=90
)
 
plt.title("Monthly Sales Distribution")
plt.show()
 