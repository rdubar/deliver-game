import streamlit as st
from tools.settings import PROMPT, CARDS

st.title('Resources')

# provide link to full source code of app at https://github.com/rdubar/random-card

# Link to your GitHub repository
github_repo_url = "https://github.com/rdubar/random-card"

download_text =  f'''
The full source code for this app is available on [GitHib]({github_repo_url}).
'''

st.markdown(download_text, unsafe_allow_html=True)

st.text_area("AI Prompt (combined with rules and default cards):", value=PROMPT, height=400, max_chars=1500, key='prompt')

st.text_area("Default Game Cards:", value=CARDS, height=400, max_chars=1500, key='cards')


