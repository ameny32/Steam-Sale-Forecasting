import pandas as pd
from sqlalchemy import create_engine
from config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME

# Connect to the database
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# Load data from the database
df = pd.read_sql("SELECT * FROM game_discounts", con=engine)

# Ensure date formatting
df['sale_date'] = pd.to_datetime(df['sale_date'])
df.sort_values(by=['game', 'sale_date'], inplace=True)

# Feature engineering
df['days_since_last_sale'] = df.groupby('game')['sale_date'].diff().dt.days
df['days_since_last_sale'] = df['days_since_last_sale'].fillna(-1)

df['is_major_event'] = df['sale_type'].isin(['Steam Summer Sale', 'Winter Sale', 'Game Awards']).astype(int)

def bin_discount(d):
    if d < 20:
        return 'Low'
    elif d < 40:
        return 'Medium'
    else:
        return 'High'

df['discount_bin'] = df['discount'].apply(bin_discount)

# Save cleaned data
df.to_sql('game_discounts_cleaned', con=engine, if_exists='replace', index=False)
print("Cleaned data written to PostgreSQL as 'game_discounts_cleaned'")
