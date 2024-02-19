import streamlit as st
from tools.settings import PROMPT, DEFAULT_AI_MODEL, AI_MODELS

AI_MODEL = st.session_state.get('AI_MODEL', DEFAULT_AI_MODEL)

st.title('Research')



# provide link to full source code of app at https://github.com/rdubar/random-card

# Link to your GitHub repository
github_repo_url = "https://github.com/rdubar/random-card"

download_text =  f'''
The full source code for this app is available on [GitHib]({github_repo_url}).
'''

st.markdown(download_text, unsafe_allow_html=True)

"""This is the current prompt used to generate new cards in combination with the game rules and default cards:"""

st.text_area('Prompt', value=PROMPT, height=400, max_chars=1500, key='prompt')

""" You can select the AI model used to generate new cards here:"""

# streamlit selector tool

# Prepare the models list for the dropdown
models = AI_MODELS.copy()
if st.session_state.AI_MODEL not in models:
    models.append(st.session_state.AI_MODEL)
    models.sort()

# Create the dropdown and update the session state based on the selection
selected_model = st.selectbox('Model', models, index=models.index(st.session_state.AI_MODEL))
st.session_state.AI_MODEL = selected_model

# Display the current model
st.write(f'Current model: {st.session_state.AI_MODEL}')