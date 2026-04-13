import joblib
import pandas as pd
import numpy as np

# 1. Load the model from the file
loaded_model = joblib.load('heart_disease_model.joblib')

print("Model loaded successfully!")

# 2. Prepare NEW data for prediction (NORMALIZED VALUES 0.0 - 1.0)
# These values are converted from the raw clinical numbers (e.g., Age 55 -> 0.54)
new_data = pd.DataFrame([{
    'oldpeak': 0.24,
    'exang': 0,
    'thalach': 0.60,
    'cp': 2,
    'ca': 0,
    'thal': 2,
    'slope': 1,
    'sex': 1,
    'age': 0.54,
    'restecg': 1,
    'chol': 0.38,
    'trestbps': 0.45
}])

# Ensure columns match the exact order the model expects
# (Based on your heart_Cleaned data.csv columns)
feature_order = ['oldpeak', 'exang', 'thalach', 'cp', 'ca', 'thal', 
                 'slope', 'sex', 'age', 'restecg', 'chol', 'trestbps']
new_data = new_data[feature_order]

# 3. Make a prediction
prediction = loaded_model.predict(new_data)

print(f"Status: {'Heart Disease' if prediction[0] == 1 else 'No Heart Disease'}")
