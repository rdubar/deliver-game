import streamlit as st
import os
from settings import data_dir, images_dir

def load_data(filename, split=False):
    # Use the current working directory as the base
    
    file_path = os.path.join(data_dir, filename)
    
    try:
        with open(file_path, 'r') as f:
            data = f.read()
        if split:
            data = data.split('\n')
        return data
    except Exception as e:
        print(f"Error loading data from {file_path}: {e}")
        return None

def download_game_board_button():
    # download button for the PDF
    with open(os.path.join(images_dir, "Game_Board.pdf"), "rb") as file:
        st.download_button(
                label="Download Game Board",
                data=file,
                file_name="Game_Board.pdf",
                mime="application/octet-stream"
            )   