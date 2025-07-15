Steam Sale Forecasting

CS210: Data Management for Data Science - Final Project

Author: Andrew Menyhert

Semester: Summer 20253

School: Rutgers University - New Brunswick


Project Overview
    
    This project analyzes historical video game pricing data to predict the best time to purchase games on Steam. 
    It uses a synthetic but realistic dataset of sales events for 12 popular games. 
    The application performs data cleaning, feature engineering, machine learning modeling, and dashboard visualization to support consumer decision-making.


Objectives
    
    Forecast future discount percentages using regression
    Predict whether a game will receive a high discount (≥40%) using classification
    Visualize price trends, sales cycles, and event-driven discounts
    Provide a user-friendly dashboard to help users decide whether to buy or wait


Features
    
    PostgreSQL database for structured data storage
    ETL pipeline with Pandas and SQLAlchemy
    Feature engineering: days_since_last_sale, discount_bin, is_major_event
    Machine learning models: Random Forest for regression and classification
    Streamlit dashboard with discount timeline and "Buy or Wait" recommendations
    Visualizations using Matplotlib and Seaborn


File Structure
.

├── data/

│   └── large_mock_steam_sales.csv

├── outputs/

│   ├── discount_timeline.png

│   ├── discount_distribution.png

│   └── discount_by_sale_type.png

├── src/

│   ├── config.py

│   ├── etl_pipeline.py

│   ├── data_cleaning.py

│   ├── model_training.py

│   ├── visualize_results.py

│   └── main_dashboard.py

└── README.md


Setup Instructions
1. Install Requirements

   pip install pandas sqlalchemy psycopg2-binary scikit-learn matplotlib seaborn streamlit

3. Configure PostgreSQL

   Update src/config.py with your PostgreSQL credentials and ensure a database named steam_sales is created.

    DB_USER = 'your_username'
    DB_PASSWORD = 'your_password'
    DB_HOST = 'localhost'
    DB_PORT = '5432'
    DB_NAME = 'steam_sales'


5. Run Project Scripts in Order

   python src/etl_pipeline.py         # Loads CSV into the database
    python src/data_cleaning.py        # Performs feature engineering
    python src/model_training.py       # Trains models and prints metrics
    python src/visualize_results.py    # Generates static charts
    streamlit run src/main_dashboard.py  # Launches the dashboard


Project Demo
    
    Watch the full demo video explaining the project setup, model training, and dashboard functionality:
    (https://drive.google.com/file/d/1IkX5CBJltmMfke2Qq7VImVb37a8fA8Y3/view?usp=sharing) 

License
    
    This project is developed for educational purposes only and is not intended for commercial use.
