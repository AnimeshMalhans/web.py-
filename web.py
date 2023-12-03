import json

import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu


st.set_page_config(
    page_title="Animesh Malhans",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_hello = load_lottieurl("https://lottie.host/3ae4dee3-428a-44f2-b4e7-45875d07b2c1/cYLs3qG5Kd.json")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home Page", "About Me"],
        icons=["house", "book", "code-slash"],
        menu_icon="cast",
        default_index=0,
    )

if selected == "Home Page":
    st.title("Hello To Everyone.Its My Website :)")
    options=["Home Page", "About Me"]
    st_lottie(lottie_hello, key="hello")
   

if selected == "About Me":
    st.title("My Name Is Animesh Malhans")
    st.header("I Wanna Become A Game Developer")
    st.text("I Am Currently Learning Python")
    st.text("Its My First Language")
    st.write("[Social >]Instagram, https://www.instagram.com/animesh_malhansh00/")
    st.write("Github, https://github.com/AnimeshMalhans")
    
    

