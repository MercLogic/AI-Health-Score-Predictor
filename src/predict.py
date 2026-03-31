import joblib
import pandas as pd
import numpy as np
import os

def run_predictor():
    model_path = 'models/health_model.pkl'
    
    if not os.path.exists(model_path):
        print("❌ Error: Model file not found! Run src/train_model.py first.")
        return

    # Load the pre-trained "brain"
    model = joblib.load(model_path)
    
    print("\n" + "="*40)
    print("   🏥 AI HEALTH RISK PREDICTOR (BYOP)   ")
    print("   Author: Ayush Singh (25BHI10059)     ")
    print("="*40)

    try:
        val = input("\nEnter BMI (or 'q' to quit): ")
        if val.lower() == 'q': return
        
        user_bmi = float(val)
        
        # Create DataFrame to avoid 'UserWarning' about feature names
        input_df = pd.DataFrame([[user_bmi]], columns=['bmi'])
        
        # Make Prediction
        prediction = model.predict(input_df)
        score = max(0, min(100, prediction[0])) # Clamp score between 0-100
        
        print(f"\n>>> Predicted Health Score: {score:.2f}/100")
        
        # Health Informatics logic
        if score > 80:
            print("Status: Optimal/Low Risk")
        elif score > 50:
            print("Status: Moderate Risk - Monitor Diet")
        else:
            print("Status: High Risk - Medical Consultation Advised")

    except ValueError:
        print("Invalid input. Please enter a numerical BMI value.")

if __name__ == "__main__":
    run_predictor()