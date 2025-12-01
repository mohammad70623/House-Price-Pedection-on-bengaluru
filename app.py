import pandas as pd 
import pickle as pk 
import streamlit as st 

model = pk.load(open('C:/Users/moham/House Price Prediction/House_prediction_model.pkl', 'rb'))
 
st.header('Bangalore House Price Prediction') 
data = pd.read_csv(r'C:\Users\moham\House Price Prediction\Cleaned_data.csv') 

loc = st.selectbox('Choose The Location', data['location'].unique())
sqft = st.number_input("Enter Total Sqft")
beds = st.number_input("Enter Number of Bedrooms")
bath = st.number_input("Enter Number of Bathrooms")
balc = st.number_input("Enter number of Balconies")

input = pd.DataFrame([[loc, sqft, beds, bath, balc]], 
                     columns=['location', 'total_sqft', 'Bedroom', 'bath', 'balcony']) 

if st.button("Predict Price"): 
    output = model.predict(input)
    out_str = 'Price of the house is ₹' + str(output[0] * 100000)
    st.success(out_str)