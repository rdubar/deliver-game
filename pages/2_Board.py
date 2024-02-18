import streamlit as st
import os
from settings import images_dir
from utils import download_game_board_button

st.title('The Game Board')

st.image(os.path.join(images_dir, 'game_board.jpg'))

download_game_board_button()   

