import pickle
import streamlit as st

depresi = pickle.load(open('depresi_model.sav', 'rb'))

st.logo('depresi.png')
st.title('Data Mining Prediksi Depresi')

Age = st.slider ("Input nilai Age/Umur",0,100)

WorkPressure = st.slider ("Input nilai Work Pressure/Tekanan Kerja",0,10)

JobSatisfaction = st.slider ("Input nilai Job Satisfaction/Kepuasan Kerja",0,10)

st.caption('0 = Ya Jika 1 = Tidak')
Haveyoueverhadsuicidalthoughts = st.slider ("Input nilai Have you ever had suicidal thoughts?/Pernahkah Anda memiliki pikiran untuk bunuh diri?",0,1)

WorkHours = st.slider ("Input nilai Work Hours/Jam Kerja",0,10)

FinancialStress = st.slider ("Input nilai Financial Stress/Tekanan Keuangan",0,10)

dep_diagnosis = ''
  
if st.button('Test Prediksi Depresi'):
    prediction = depresi.predict([[Age, WorkPressure, JobSatisfaction, Haveyoueverhadsuicidalthoughts, WorkHours, FinancialStress]])

    if (prediction[0] == 0):
        dep_diagnosis = 'Depresi'
    else :   
        dep_diagnosis = 'Tidak depresi'

    st.success(dep_diagnosis) 
    st.balloons() 
