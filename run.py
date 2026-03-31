import os
import subprocess
import sys
import time

def run_step(step_name, script_path):
    print(f"\n--- 🚀 Step: {step_name} ---")
    try:
        # Runs the script using the current Python interpreter
        result = subprocess.run([sys.executable, script_path], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during {step_name}: {e}")
        return False

def main():
    print("==============================================")
    print("   AI HEALTH RISK PREDICTOR - MASTER RUNNER   ")
    print("   Author: Ayush Singh (25BHI10059)           ")
    print("==============================================\n")

    # 1. Setup Data
    if not run_step("Generating Healthcare Dataset", "data/data_setup.py"):
        return

    # 2. Train Model
    if not run_step("Training Linear Regression Model", "src/train_model.py"):
        return

    # 3. Launch Predictor
    print("\n✅ All systems ready. Launching Predictor Interface...")
    time.sleep(1) # Small pause for better UX
    run_step("User Prediction Interface", "src/predict.py")

if __name__ == "__main__":
    main()