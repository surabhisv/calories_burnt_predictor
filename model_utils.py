import joblib
import numpy as np

# Load model and scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")  # Comment this if you didn't use a scaler

def predict_from_input(input_features):
    """
    input_features: list of numeric values [Age, Height, Weight, Duration]
    """
    array = np.array(input_features).reshape(1, -1)
    array_scaled = scaler.transform(array)  # Comment this if no scaler
    prediction = model.predict(array_scaled)
    return prediction[0]
