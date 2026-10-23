import streamlit as st
import joblib
import pandas as pd

model = joblib.load("heart_model.pkl")
encoders = joblib.load("encoders.pkl")

st.title("Heart Disease Prediction System")

age = st.number_input("Age", 20, 100, 50)
sex = st.selectbox("Sex", encoders["sex"].classes_)
cp = st.selectbox("Chest Pain Type", encoders["cp"].classes_)
thalach = st.number_input("Maximum Heart Rate", 60, 220, 150)

if st.button("Predict"):
    row = pd.DataFrame(
        [[age,
          encoders["sex"].transform([sex])[0],
          encoders["cp"].transform([cp])[0],
          thalach]],
        columns=["age", "sex", "cp", "thalach"])
    result = model.predict(row)[0]
    if result == 1:
        st.error("High risk of heart disease")
    else:
        st.success("Low risk of heart disease")