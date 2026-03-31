import pandas as pd
import os

# Ensure the data directory exists
os.makedirs('data', exist_ok=True)

# Creating a synthetic healthcare dataset for BMI analysis
# Higher BMI generally maps to a lower "Health Score" in this simple linear model
data = {
    'bmi': [18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],
    'health_score': [95, 98, 92, 85, 78, 70, 55, 40, 30, 20, 15, 10]
}

df = pd.DataFrame(data)
df.to_csv('data/health_data.csv', index=False)
print("✅ Dataset successfully created in data/health_data.csv")