import streamlit as st
import numpy as np 
import pickle
import sklearn

# loading the model

with open('studentperformance.pkl', 'rb') as file:
    model = pickle.load(file)

# streamlit application user interface

st.title('Student Performance Predictor 📚')
st.markdown("""
### **📖 Get your child performance with my prediction app!**
This app predicts your child's performance, whether he?she will pass or not.
fill in the details and click **Predict** to get your child's result. 
""")

# input form

study_hours_per_week = st.number_input("Study Hours Per Week", min_value=0, max_value=40, value=0, step=1)
attendance_rate = st.number_input("Attendance Rate", min_value=0, max_value=150, value=0, step=1)
previous_grades = st.number_input("Previous Grade", min_value=0, max_value=150, value=0, step=1)
participation_in_extracurricular_activities = st.selectbox("Participation in Extracurricular Activites", ["Yes", "No"])
parent_education_level = st.selectbox("Parents Education Level",["High School", "Bachelor", "Master", "Associate", "Doctorate"])

# converting categorical data into numerical values

participation_in_extracurricular_activities = 1 if participation_in_extracurricular_activities == "Yes" else 0
parent_mapping = {"High School": 1, "Bachelor": 2, "Master": 3, "Associate": 4, "Doctorate": 5}
parent_education_level = parent_mapping[parent_education_level]

# preparing the input data

input_data = np.array([[study_hours_per_week, attendance_rate, previous_grades, participation_in_extracurricular_activities, parent_education_level]])

# prediction

if st.button("Predict"):
    prediction = model.predict(input_data)
    
    # Output
    if prediction == 1:
        st.success("Student has high probability of PASSING")
    else:
        st.error("Student has high probability of FAILING")

# footer
st.write('This aplication was created for the technical deepdive 2.0 final assessment')

st.write('BY Hikma Yahya')

