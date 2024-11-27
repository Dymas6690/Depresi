import pickle
import streamlit as st

depresi = pickle.load(open('depresi_model.sav', 'rb'))

st.logo('depresi.png')
st.title('Data Mining Prediksi Depresi')
st.caption('Input angka 1-10')

Age = st.number_input ('Input nilai Age/Umur')

WorkPressure = st.number_input ('Input nilai Work Pressure/Tekanan Kerja')

JobSatisfaction = st.number_input ('Input nilai Job Satisfaction/Kepuasan Kerja')

Haveyoueverhadsuicidalthoughts = st.number_input ('Input nilai Have you ever had suicidal thoughts?/Pernahkah Anda memiliki pikiran untuk bunuh diri?')

WorkHours = st.number_input ('Input nilai Work Hours/Jam Kerja')

FinancialStress = st.number_input ('Input nilai Financial Stress/Tekanan Keuangan')

dep_diagnosis = ''
  
if st.button('Test Prediksi Depresi'):
    prediction = depresi.predict([[Age, WorkPressure, JobSatisfaction, Haveyoueverhadsuicidalthoughts, WorkHours, FinancialStress]])

    if (prediction[0] == 0):
        dep_diagnosis = 'Depresi'
    else :   
        dep_diagnosis = 'Tidak depresi'

    st.success(dep_diagnosis) 