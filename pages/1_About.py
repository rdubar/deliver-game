import streamlit as st
from tools.settings import download_game_board_button, show_gitub_repo_link

st.set_page_config(page_title="Delivery Game", page_icon=":game_die:")

st.title('About the Game')

text =f"""
This game was developed for the Open University U101 module 
*Design thinking: creativity for the 21st century* TMA03 in February 2024.

It features the ability to generate new "event" cards using OpenAI's GPT models.

Please enjoy!

Your suggestions and feedback are very welcome.

-- Roger

"""
st.markdown(text)

# Adding clickable email address
st.markdown('**Send your feedback:** [rdubar@gmail.com](mailto:rdubar@gmail.com)', unsafe_allow_html=True)

show_gitub_repo_link()

download_game_board_button()   


