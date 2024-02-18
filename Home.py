import streamlit as st
import random
from utils import load_data
from gpt_cards import get_gpt_card
from settings import SHOW_GENERATED_CARD

# streamlit run Home.py

st.set_page_config(page_title="Delivery Game", page_icon=":game_die:")

def load_fortunes(filename='delivery.txt'):
    return load_data(filename, split=True)

# Initialize the fortunes list in the session state if it doesn't exist
if 'fortunes' not in st.session_state:
    st.session_state.fortunes = load_fortunes()

# Title of the app
st.title('The Delivery Game')

# Throw a dice
if st.button('Throw the dice'):
    dice = random.randint(1, 6)
    st.write(f"You threw a {dice}!")

# Show a card button
if st.button('Show me my card'):
    if not st.session_state.fortunes:
        # Reload fortunes if all have been shown
        st.session_state.fortunes = load_fortunes()
    # Select a random fortune and remove it from the list to avoid duplicates
    fortune = random.choice(st.session_state.fortunes)
    st.session_state.fortunes.remove(fortune)
    # Display the selected fortune
    st.write(fortune)

if SHOW_GENERATED_CARD:
    if st.button('Experimental: Generate unique card using OpenAI GPT-3'):
        st.write(get_gpt_card())
