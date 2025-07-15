import pandas as pd
from sqlalchemy import create_engine
from config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME

# Load the new larger CSV file
df = pd.read_csv('data/large_mock_steam_sales.csv')

# Transformations
df['sale_date'] = pd.to_datetime(df['sale_date'])
df['game'] = df['game'].str.strip()
df['sale_type'] = df['sale_type'].str.strip()

# Database connection
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# Load to PostgreSQL
df.to_sql('game_discounts', con=engine, if_exists='replace', index=False)
print("Data loaded into PostgreSQL successfully!")
