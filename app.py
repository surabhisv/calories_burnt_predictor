import streamlit as st
from model_utils import predict_from_input

st.set_page_config(page_title="Calories Burned Prediction")

st.title("Calorie Burn Prediction App 🏃‍♂️🔥")
st.markdown("Enter the values to predict how many calories were burned:")

# Get user input
age = st.number_input("Age", min_value=1, max_value=100, value=25)
height = st.number_input("Height (in cm)", min_value=100, max_value=250, value=170)
weight = st.number_input("Weight (in kg)", min_value=30, max_value=200, value=70)
duration = st.number_input("Duration (minutes)", min_value=1, max_value=300, value=30)
heart_rate = st.number_input("Heart Rate", min_value=40, max_value=200, value=100)



# Predict
if st.button("Predict Calories Burned"):
    features = [age, height, weight, duration, heart_rate]
    result = predict_from_input(features)
    st.success(f"Estimated Calories Burned: {result:.2f}")
