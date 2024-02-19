import streamlit as st
from tools.settings import RULES, download_game_board_button

st.title('Rules of the Game')

download_game_board_button()

st.write(RULES)

# Adding a clickable email address
st.markdown('**Send your feedback:** [rdubar@gmail.com](mailto:rdubar@gmail.com)', unsafe_allow_html=True)