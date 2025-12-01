import pandas as pd 
import pickle as pk 
import streamlit as st 

model = pk.load('C:\Users\moham\House Price Prediction\House_prediction_model.pkl', 'rb') 

st.header ('Baglore House Price Predction') 
data = pd.read_csv('C:\Users\moham\House Price Prediction\Cleaned_data.csv')
input = pd.DataFrame([['Electronic City Phase II',1500.0, 3.0,2.0,2]], columns=['location','total_sqft','bath','balcony','Bedroom'])