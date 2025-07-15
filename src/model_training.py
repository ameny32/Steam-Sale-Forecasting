import pandas as pd
from sqlalchemy import create_engine
from config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_absolute_error, accuracy_score, classification_report

# Connect to DB
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
df = pd.read_sql("SELECT * FROM game_discounts_cleaned", con=engine)

# Encode categorical features
df_encoded = pd.get_dummies(df, columns=["game", "sale_type", "discount_bin"], drop_first=True)

# Regression
print("\nREGRESSION: Predicting Discount %")
X_reg = df_encoded.drop(columns=["discount", "sale_price", "sale_date"])
y_reg = df_encoded["discount"]
X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)
reg_model = RandomForestRegressor(n_estimators=100, random_state=42)
reg_model.fit(X_train_r, y_train_r)
y_pred_r = reg_model.predict(X_test_r)
print(f"MAE (Discount %): {mean_absolute_error(y_test_r, y_pred_r):.2f}")

# Classification
print("\nCLASSIFICATION: Predicting High Discount (>=40%)")
df_encoded['is_high_discount'] = (df['discount'] >= 40).astype(int)
X_clf = df_encoded.drop(columns=["discount", "sale_price", "sale_date", "is_high_discount"])
y_clf = df_encoded["is_high_discount"]
X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(X_clf, y_clf, test_size=0.2, random_state=42)
clf_model = RandomForestClassifier(n_estimators=100, random_state=42)
clf_model.fit(X_train_c, y_train_c)
y_pred_c = clf_model.predict(X_test_c)
print(f"Accuracy: {accuracy_score(y_test_c, y_pred_c):.2f}")
print("\nClassification Report:")
print(classification_report(y_test_c, y_pred_c))
