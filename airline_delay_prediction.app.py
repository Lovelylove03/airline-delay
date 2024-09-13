# app.py
import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('flight_delay_model.pkl')

# Streamlit app layout
st.title("Flight Delay Prediction System")
st.write("Enter flight details to predict delay status.")

# Input fields for user data
feature_1 = st.number_input('Feature 1', min_value=0, max_value=100)  # Replace with actual features
feature_2 = st.number_input('Feature 2', min_value=0, max_value=100)
# Add more input fields based on your dataset features

# When the user clicks the button
if st.button('Predict Delay'):
    # Create a DataFrame for the input features
    input_data = pd.DataFrame([[feature_1, feature_2]], columns=['Feature1', 'Feature2'])  # Replace with actual columns
    
    # Predict using the trained model
    prediction = model.predict(input_data)
    
    # Display the prediction
    if prediction == 1:
        st.write("The flight is predicted to be delayed.")
    else:
        st.write("The flight is predicted to be on time.")
