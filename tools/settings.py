import streamlit as st
import os
from .wordcloud_tool import create_wordcloud

"""
Global settings & helpers for the Random Card Generator app.
"""

# Set to False to hide the experimental AI card generator feature
SHOW_GENERATED_CARD = True

BASE_DIR = os.getcwd()

DATA_DIR = os.path.join(BASE_DIR, 'data')

IMAGES_DIR = os.path.join(BASE_DIR, 'images')

WORDCLOUD_PATH = os.path.join(IMAGES_DIR, 'wordcloud.png')

"""
Helper functions for the Random Card Generator app.

Run from the command line to refresh the wordcloud image.
"""

def load_data(filename, split=False):
    # Use the current working directory as the base
    
    file_path = os.path.join(DATA_DIR, filename)
    
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
    with open(os.path.join(IMAGES_DIR, "Game_Board.pdf"), "rb") as file:
        st.download_button(
                label="Download Game Board",
                data=file,
                file_name="Game_Board.pdf",
                mime="application/octet-stream"
            )   

def make_wordcloud(text):
    # Create a word cloud from the text
    output = os.path.join(IMAGES_DIR, 'wordcloud.png')
    create_wordcloud(text, filename=output)

PROMPT = load_data('prompt.txt')
RULES = load_data('rules.md')
CARDS = load_data('delivery.txt')
FULL_PROMPT = PROMPT + RULES + CARDS



if __name__ == "__main__":
    make_wordcloud(FULL_PROMPT)
    print("Word cloud created successfully.")





