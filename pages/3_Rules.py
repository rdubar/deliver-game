import streamlit as st
from utils import load_data, download_game_board_button

st.title('Rules of the Game')

download_game_board_button()

rules = load_data('rules.md')
st.write(rules)

# Adding a clickable email address
st.markdown('**Send your feedback:** [rdubar@gmail.com](mailto:rdubar@gmail.com)', unsafe_allow_html=True)