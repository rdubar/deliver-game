import streamlit as st
from tools.settings import CARDS, SHOW_GENERATED_CARD
from tools.settings import download_game_board_button, show_gitub_repo_link

# streamlit run Home.py

st.set_page_config(page_title="Delivery Game", page_icon=":game_die:")

# Title of the app
st.title('The Delivery Game')

"""
Welcome to **Deliverance**, a fun game for 1-5 players aged 8 and up.

It was developed for the Open University U101 module *Design thinking: creativity for the 21st century* TMA03 in February 2024.

You can [print the game board](pages/2_Board.py) and read the [game rules](pages/3_Rules.py) here.

Most exciting, you can [generate new game "event" cards](pages/1_Card_Generator.py) using OpenAI's GPT models!

Each player can use this web app to roll dice and draw cards while playing.

"""

# Adding clickable email address
st.markdown('**Send your feedback:** [rdubar@gmail.com](mailto:rdubar@gmail.com)', unsafe_allow_html=True)

show_gitub_repo_link()

download_game_board_button()   