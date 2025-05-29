import streamlit as st

st.title("My First Streamlit App")
st.write("Hello, world! 👋")

if st.button("Click me!"):
    st.write("Why hello there")
else:
    st.write("Goodbye")
    
