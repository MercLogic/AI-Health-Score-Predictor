import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os

# Ensure the models directory exists
os.makedirs('models', exist_ok=True)

# 1. Load the data created by data_setup.py
if not os.path.exists('data/health_data.csv'):
    print("❌ Error: data/health_data.csv not found. Run data/data_setup.py first!")
else:
    df = pd.read_csv('data/health_data.csv')

    # 2. Initialize and Train the Linear Regression Model
    # Features (X) must be a 2D array for sklearn
    X = df[['bmi']] 
    y = df['health_score'] 
    
    model = LinearRegression()
    model.fit(X, y)

    # 3. Save the trained model for persistence (BYOP requirement)
    joblib.dump(model, 'models/health_model.pkl')
    print("✅ AI Model trained and saved to models/health_model.pkl")