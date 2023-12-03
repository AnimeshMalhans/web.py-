import json
import streamlit as st
from streamlit_option_menu import option_menu

hide_menu_style = """
          <style>
          #MainMenu {visibility: hidden; }
          footer {visibility: hidden:}
          </style> 
"""
st.markdown(hide_menu_style, unsafe_allow_html=True)

with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home Page", "About Me","The Code"],
        icons=["house", "book", "code-slash"],
        menu_icon="cast",
        default_index=0,
    )    


if selected == "Home Page":
    st.title("Hello To Everyone.Its My Website :)")
)
    options=["Home Page", "About Me","The Code"]


if selected == "About Me":
    st.title("My Name Is Animesh Malhans")
    st.header("I Wanna Become A Game Developer")
    st.text("I Am Currently Learning Python")
    st.text("Its My First Language")
    st.write("[Social >] https://www.instagram.com/animesh_malhansh00/")
    

if selected == "The Code":
    st.title(f'The Code I Used For This Website')
    st.code('''import json
import streamlit as st
from streamlit_option_menu import option_menu

hide_menu_style = """
          <style>
          #MainMenu {visibility: hidden; }
          footer {visibility: hidden:}
          </style> 
"""
st.markdown(hide_menu_style, unsafe_allow_html=True)

with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home Page", "About Me","The Code"],
        icons=["house", "book", "code-slash"],
        menu_icon="cast",
        default_index=0,
    )    


if selected == "Home Page":
    st.title("Hello To Everyone.Its My Website :)")
)
    options=["Home Page", "About Me","The Code"]


if selected == "About Me":
    st.title("My Name Is Animesh Malhans")
    st.header("I Wanna Become A Game Developer")
    st.text("I Am Currently Learning Python")
    st.text("Its My First Language")
    

if selected == "The Code":
    st.title(f'The Code I Used For This Website')
    st.code(
''')
