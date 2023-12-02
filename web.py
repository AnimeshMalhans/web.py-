import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home Page", "About Me","The Code"]
    )

if selected == "Home Page":
    st.title("The Website")
    st.markdown("The Code I Used")

if selected == "About Me":
    st.header("I am Currently Learning Python")

if selected == "The Code":
    st.title(f'The Code I Used For This Website')
    st.code('''import streamlit as st
from streamlit_lottie import st_lottie

  
st.title("The Website")
st.header("I am Currently Learning Python")

name = st.text_input("Enter Your Name")

classdata = st.selectbox




button = st.button("Done")
''')
