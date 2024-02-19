import streamlit as st
from tools.settings import PROMPT, CARDS, show_gitub_repo_link

st.set_page_config(page_title="Delivery Game", page_icon=":game_die:")

st.title('Resources')

# provide link to full source code of app at https://github.com/rdubar/random-card

show_gitub_repo_link()

st.text_area("AI Prompt (combined with rules and default cards):", value=PROMPT, height=400, max_chars=1500, key='prompt')

st.text_area("Default Game Cards:", value=CARDS, height=400, max_chars=1500, key='cards')


