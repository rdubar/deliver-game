import streamlit as st
import random
import os

# streamlit run cards_app.py

def load_fortunes(filename):
    with open(filename, 'r') as file:
        fortunes = file.readlines()
    return [fortune.strip() for fortune in fortunes]

fortunes = load_fortunes(os.path.join(os.path.dirname(__file__), 'fortunes.txt'))
        
# Title of the app
st.title('The Delivery Game')

# When the button is pressed
if st.button('Show me my card'):
    # Select a random fortune
    fortune = random.choice(fortunes)
    # Display the selected fortune
    st.write(fortune)
