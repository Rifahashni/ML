import streamlit as st

import joblib
model=joblib.load('model.pkl')
scaler=joblib.load('scaler.pkl')

st.title('Air Quality and Health Impact')
st.write('Enter Data Description')

AQI=st.number_input('Enter the air quality index')
PM10=st.number_input('Enter the PM10')
PM2_5=st.number_input('Enter the PM2_5')
NO2=st.number_input('Enter the N02')
SO2=st.number_input('Enter the SO2')
O3=st.number_input('Enter the O3')
Temperature=st.number_input('Enter the Temperature')
Humidity=st.number_input('Enter the humidity')
WindSpeed=st.number_input('Enter the windspeed')
RespiratoryCases=st.number_input('Enter the Respiratory cases')
CardiovascularCases=st.number_input('Enter the cardiovascular cases')
HospitalAdmissions=st.number_input('Enter the Hospital Admissions')
HealthImpactScore=st.number_input('Enter the health impact score') 

if st.button('predict'):
    result=model.predict(scaler.transform([[AQI,PM10,PM2_5,NO2,SO2,O3,Temperature,Humidity,WindSpeed,RespiratoryCases,CardiovascularCases,HospitalAdmissions,	HealthImpactScore]]))[0]
    if result==0:
        st.success('Health impact is very high')
    elif result==1:
        st.success('Health impact is high')
    elif result==2:
        st.success('Health impact is moderate')
    elif result==3:
        st.success('Health impact is low')
    elif result==4:
        st.success('Health impact is very low')
        
    