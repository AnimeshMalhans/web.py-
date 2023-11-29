import streamlit as st
from streamlit_lottie import st_lottie
import json

def load_lottiefiles(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_coding = load_lottiefiles("C:\Users\Admin\Desktop\Python\code.json")
  
st.title("The Website")
st.header("I am Currently Learning Python")

name = st.text_input("Enter Your Name")

classdata = st.selectbox




button = st.button("Done")


st.markdown("The Code I Used")
st.code('''import streamlit as st
from streamlit_lottie import st_lottie
import json

def load_lottiefiles(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_coding = load_lottiefiles("C:\Users\Admin\Desktop\Python\code.json")
  
st.title("The Website")
st.header("I am Currently Learning Python")

name = st.text_input("Enter Your Name")

classdata = st.selectbox
        
        
button = st.button("Done")
st_lottie(
    lottie_coding,
    loop = True,
    quality="high")''')


button = st.button("Done")
st_lottie(
    lottie_coding,
    loop = True,
    quality="high")
