import numpy as np
import pickle
import streamlit as st
import os

# Load the saved model with error handling
model_path = r'C:\Users\chali\OneDrive\Desktop\New folder\c++\trained_model.sav'

if not os.path.exists(model_path):
    st.error(f"Model file not found at {model_path}. Please check the path.")
    st.stop()

with open(model_path, 'rb') as file:
    loaded_model = pickle.load(file)


def diabetes_prediction(input_data):
    # Convert input data to numpy array and reshape
    input_data_as_nparray = np.asarray(input_data, dtype=float)
    input_data_reshaped = input_data_as_nparray.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)

    if prediction[0] == 0:
        return 'Non Diabetic'
    else:
        return 'Diabetic'


def main():
    st.title('Diabetes Prediction Web App')

    # Get input from user with validation
    try:
        Pregnancies = st.text_input('No. of Pregnancies:')
        Glucose = st.text_input('Glucose level:')
        BloodPressure = st.text_input('Blood Pressure value:')
        SkinThickness = st.text_input('Skin thickness value:')
        Insulin = st.text_input('Insulin level:')
        BMI = st.text_input('BMI value:')
        DiabetesPedigreeFunction = st.text_input('Diabetes pedigree function value:')
        Age = st.text_input('Age:')

        diagnosis = ''

        if st.button('Predict'):
            # Convert inputs to floats
            input_features = [
                float(Pregnancies), float(Glucose), float(BloodPressure),
                float(SkinThickness), float(Insulin), float(BMI),
                float(DiabetesPedigreeFunction), float(Age)
            ]
            diagnosis = diabetes_prediction(input_features)
            st.success(diagnosis)

    except ValueError:
        st.error("Please enter valid numeric input in all fields.")


if __name__ == '__main__':
    main()
