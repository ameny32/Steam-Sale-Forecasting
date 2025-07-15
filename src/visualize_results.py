import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine
from config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME

# DB connection
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
df = pd.read_sql("SELECT * FROM game_discounts_cleaned", con=engine)
df['sale_date'] = pd.to_datetime(df['sale_date'])

# Create output directory
import os
os.makedirs("outputs", exist_ok=True)

# 1. Timeline of discounts
plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x="sale_date", y="discount", hue="game", marker="o")
plt.title("Game Discount Timeline")
plt.xlabel("Sale Date")
plt.ylabel("Discount (%)")
plt.legend(title="Game")
plt.tight_layout()
plt.savefig("outputs/discount_timeline.png")
plt.close()

# 2. Histogram of discounts
plt.figure(figsize=(7, 5))
sns.histplot(df["discount"], bins=10, kde=True)
plt.title("Distribution of Discount Percentages")
plt.xlabel("Discount (%)")
plt.tight_layout()
plt.savefig("outputs/discount_distribution.png")
plt.close()

# 3. Boxplot by sale type
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x="sale_type", y="discount")
plt.title("Discounts by Sale Type")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("outputs/discount_by_sale_type.png")
plt.close()

print("Visualizations saved to /outputs/")
