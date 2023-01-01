import streamlit as st

def main():
    st.title('Home')
    name = st.text_input('Your Name: ')
    name_cap = name.capitalize()
    if st.button('Click here'):
        st.header(f'Happy New Year to {name_cap}.')
        st.balloons()
        st.snow()
        st.balloons()
        st.header('This is the time to ....')
        st.write('This is the time to be a new person')
        st.write('This is the time to achive something new')
        st.write('This is the time to make new memories')
        st.write('This is the time to make new friends or strengthen old friendships')
        st.write('This is the time to try something new')
        st.write('And most of all ...')
        st.write('This is the time of new beginnings')

if __name__ == "__main__":
  main()