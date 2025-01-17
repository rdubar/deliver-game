import streamlit as st
import os



"""
Global settings & helpers for the Random Card Generator app.
"""

# Set to False to hide the experimental AI card generator feature
SHOW_GENERATED_CARD = True

BASE_DIR = os.getcwd()

DATA_DIR = os.path.join(BASE_DIR, 'data')

IMAGES_DIR = os.path.join(BASE_DIR, 'images')

WORDCLOUD_PATH = os.path.join(IMAGES_DIR, 'wordcloud.png')

QR_CODE_PATH = os.path.join(IMAGES_DIR, 'qrcode_deliver-game.streamlit.app.png')

PAGE_URL = "https://deliver-game.streamlit.app"

GITHIB_REPO_URL = "https://github.com/rdubar/random-card"

BACKUP_DIR = os.path.join(BASE_DIR, 'backups')

try:
    OPEN_AI_API_KEY = api_key = st.secrets["openai"]["openai_api_key"] if "openai" in st.secrets else os.environ.get('OPENAI_API_KEY', '')
except:
    OPEN_AI_API_KEY = False

if not OPEN_AI_API_KEY:
    print("OpenAI API key not found. Please setup in secrets.toml.")
    SHOW_GENERATED_CARD = False

"""
Helper functions for the Random Card Generator app.

Run from the command line to refresh the wordcloud image.
"""

def show_gitub_repo_link():
    download_text =  f'The full source code for this app is available on [GitHub]({GITHIB_REPO_URL}).'
    st.markdown(download_text, unsafe_allow_html=True)

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

def download_game_board_buttons():
# Provide download buttons for all the JPG in the images directory
    image_files = [f for f in os.listdir(IMAGES_DIR) if f.endswith('.jpg')]  
    for image_file in sorted(image_files):
        with open(os.path.join(IMAGES_DIR, image_file), "rb") as file:
            display_name = image_file.replace("_", " ").replace(".jpg", "").title()
            st.download_button(
                    label=f"Download {display_name}",
                    data=file,
                    file_name=image_file,
                    mime="application/octet-stream"
            )
            
def is_running_locally():
    # fix as needed to ensure this works in your environment
    # This is important to prevent showing feedback received publicly
    return "opt" in BASE_DIR


PROMPT = load_data('prompt.txt')
RULES = load_data('rules.md')
CARDS = load_data('delivery.txt')
SPECIAL = load_data('special.md')
FULL_PROMPT = PROMPT + RULES + CARDS





