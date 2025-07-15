# streamlit run src/main_dashboard.py

import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME

# DB connection
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
df = pd.read_sql("SELECT * FROM game_discounts_cleaned", con=engine)
df['sale_date'] = pd.to_datetime(df['sale_date'])

st.title("Steam Sale Forecasting Dashboard")

# Game selector
game = st.selectbox("Choose a Game:", df['game'].unique())
df_game = df[df['game'] == game]

# Timeline
st.subheader("Discount Timeline")
st.line_chart(df_game.set_index("sale_date")["discount"])

# Summary stats
st.subheader("Discount Stats")
st.write(df_game.describe()[["discount", "days_since_last_sale"]])

# Sale type frequency
st.subheader("Sales by Type")
st.bar_chart(df_game["sale_type"].value_counts())

# Recommendation logic
st.subheader("Recommendation: Buy or Wait?")
latest_sale = df_game.sort_values("sale_date", ascending=False).iloc[0]
predicted_discount = latest_sale['discount']
days_since = latest_sale['days_since_last_sale']

if predicted_discount >= 40 or days_since > 90:
    st.success("Wait - a bigger sale is likely soon!")
else:
    st.info("Safe to buy now - no big sale expected soon.")
