import streamlit as st

def main():
    st.title('Home')
    name = st.text_input('Your Name: ')
    if st.button('Click here'):
        st.header(f'Happy New Year to {name}.')
        st.balloons()
        st.snow()
        st.balloons()