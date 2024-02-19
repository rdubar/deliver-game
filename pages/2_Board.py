import streamlit as st
import os
from tools.settings import IMAGES_DIR, download_game_board_button 

st.set_page_config(page_title="Delivery Game", page_icon=":game_die:")

st.title('The Game Board')

st.image(os.path.join(IMAGES_DIR, 'game_board.jpg'))

download_game_board_button()   

