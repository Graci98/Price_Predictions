import streamlit as st
from dataclasses import dataclass
from typing import Any, List
import datetime as datetime
import pandas as pd
import pickle
import numpy as np
 





cols=['year','make','model','state','condition','odometer','color','mmr','sellingprice','vehicleage']
                        
                        
def main():
    st.title("Vehicle Price Predictor")
    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Car Price Prediction App </h2>
    </div>
    """
   
    st.markdown(html_temp, unsafe_allow_html = True)
    
    year= st.number_input("Year", min_value=1990, max_value=2015)
    make= st.text_input("Make")
    model= st.text_input("Model")
    odometer= st.number_input("Odometer")
    color= st.text_input("Color")
    state= st.text_input("State")
    condition = 7
    mmr = st.number_input("Listed Price", value=None, placeholder="Type Price")
    vehicleage = st. number_input("Age of Vehicle", min_value=0, max_value=25) 
        
                        
    if st.button("Predicted Value"):
        features = {"year":year, "make":make, "model" :model, "odometer":odometer, "color":color, "state":state,"mmr":mmr, "condition":condition, "vehicleage":vehicleage}
        data = {}
        for i in features.keys():
            if type(features[i]) == str:
                with open("encoder_"+str(i)+".pkl", 'rb') as encoder:
                    label_encoder = pickle.load(encoder)
                print(label_encoder,i)
                data[str(i)] = label_encoder.transform(np.array(features[i]).reshape(1,-1))

            elif type(features[i]) != str:
                      data[str(i)] = features[i]
            with open(str(i)+"_scaler.pkl", 'rb') as scaler_file:
                scaler = pickle.load(scaler_file)
            data[str(i)] = scaler.transform(np.array(data[i]).reshape(1,-1))
                           
        processed_data = {key: value[0] for key, value in data.items()}
        processed_df = pd.DataFrame(processed_data)
        model = pickle.load(open('lasso_model.pkl', 'rb'))
        prediction = model.predict(processed_df.values)
        
        output = round(prediction[0],2)
        st.write(output)
if __name__ == "__main__" :  
    main()
        