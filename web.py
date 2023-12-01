import streamlit as st
import pandas as pd
import numpy as np


st.title("The Website")
st.header("I am Currently Learning Python")
df = pd.DataFrame(np.random.randn(800, 2) / [50, 50] + [19.07, 72.87],columns=['latitude', 'longitude'])
@st.cache

def convert_df(df):
    return df.to_csv().encode('utf-8')
csv = convert_df(df)
st.download_button( 

    label="Download data as CSV",

    data=csv,

    file_name='sample_df.csv',

    mime='text/csv',

)
name = st.text_input("Enter Your Name")

classdata = st.selectbox


button = st.button("Done")


st.markdown("The Code I Used")
st.code('''import streamlit as st
from streamlit_lottie import st_lottie

  
st.title("The Website")
st.header("I am Currently Learning Python")

name = st.text_input("Enter Your Name")

classdata = st.selectbox




button = st.button("Done")
''')
