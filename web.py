import streamlit as st
  
st.title("The Website")
st.header("I am Currently Learning Python")

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
