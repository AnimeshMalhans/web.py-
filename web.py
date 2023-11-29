import streamlit as st


st.title("The Website")
st.header("I am Currently Learning Python")

name = st.text_input("Enter Your Name")

classdata = st.selectbox




button = st.button("Done")


st.markdown("The code i used for this website made in python")
st.code('''import streamlit as st
name = st.text_input("Enter Your Name")

classdata = st.selectbox

st.title("The Website")
st.header("I am Currently Learning Python")


button = st.button("Done")
if button :
    st.markdown("""f
    Name: {name}""")''')