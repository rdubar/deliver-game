import streamlit as st
import os
from tools.settings import IMAGES_DIR, download_game_board_button 

st.title('The Game Board')

st.image(os.path.join(IMAGES_DIR, 'game_board.jpg'))

download_game_board_button()   

