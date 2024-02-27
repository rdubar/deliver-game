import streamlit as st
from tools.settings import CARDS, SHOW_GENERATED_CARD
from tools.settings import download_game_board_button, show_gitub_repo_link

# streamlit run Home.py

st.set_page_config(page_title="Delivery Game", page_icon=":game_die:")

# Title of the app
st.title('The Delivery Game')

"""
Welcome to **Deliverance**, a fun game for 1-5 players aged 8 and up.

This page can use AI to generate unique game cards every time you play!

You can find the game board, rules, card generator, and feedback form in the menu.

Please enjoy!

-- Rog
"""