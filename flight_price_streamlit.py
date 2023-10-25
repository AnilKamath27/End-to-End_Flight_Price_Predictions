# To run use : streamlit run flight_price_streamlit.py

import streamlit as st
import pandas as pd
import pickle

st.title("Flight Price Prediction")

airline = st.selectbox("airline", ("SpiceJet","AirAsia","Vistara","GO_FIRST","Indigo","Air_India"))
source_city = st.selectbox("source_city",("Delhi","Mumbai","Bangalore","Kolkata","Hyderabad","Chennai"))
departure_time = st.selectbox("departure_time",("Evening","Early_Morning","Morning","Afternoon","Night","Late_Night"))
stops = st.selectbox("stops",("zero","one","two_or_more"))
arrival_time = st.selectbox("arrival_time",("Evening","Early_Morning","Morning","Afternoon","Night","Late_Night"))
destination_city = st.selectbox("destination_city",("Delhi","Mumbai","Bangalore","Kolkata","Hyderabad","Chennai"))
class_= st.selectbox("class",("Economy","Business"))
duration = st.number_input("duration")
days_left = st.number_input("days_left")

if st.button("Predict price"):
    with open("XGBoost_model.pkl",'rb') as model_file:
        model = pickle.load(model_file)

    data ={
            "airline":airline,
             "source_city":source_city,
             "departure_time":departure_time,
             "stops": stops,
             "arrival_time": arrival_time,
             "destination_city":destination_city,
             "class":class_,
             "duration":duration,
             "days_left":days_left,
    }                     

    input_data = pd.DataFrame(data,index=[0])
    predictions = model.predict(input_data)[0]
    st.write("The Predicted Price is:", predictions)

