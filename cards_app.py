import streamlit as st
import random
import os

# streamlit run cards_app.py

fortune_file = "delivery.txt"
fortune_path = os.path.join(os.path.dirname(__file__), fortune_file)

st.set_page_config(page_title="Random Card", page_icon=":game_die:")

def load_fortunes(filename):
    with open(filename, 'r') as file:
        fortunes = file.readlines()
    return [fortune.strip() for fortune in fortunes]

fortunes = load_fortunes(fortune_path)
        
# Title of the app
st.title('The Delivery Game')

# When the button is pressed
if st.button('Show me my card'):
    if not fortunes:
        fortunes = load_fortunes(fortune_path)
    # Select a random fortune
    fortune = random.choice(fortunes)
    # Remove the fortune from the list
    fortunes.remove(fortune)
    # Display the selected fortune
    st.write(fortune)
