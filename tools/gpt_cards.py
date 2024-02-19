import streamlit as st
import openai
import os
from .settings import load_data, DEFAULT_AI_MODEL
from .mongo_logger import log_text

api_key = st.secrets["openai"]["openai_api_key"] if "openai" in st.secrets else os.environ.get('OPENAI_API_KEY', '')
openai.api_key = api_key
AI_MODEL = st.session_state.get('AI_MODEL', DEFAULT_AI_MODEL)

"""
Use OpenAI's models to generate random cards for the game.
"""

prompt = load_data('prompt.txt')
rules = load_data('rules.md')
cards = load_data('delivery.txt')

full_prompt = prompt + rules + cards

def query_chatgpt(prompt, model=None, history=[]):
    if not model:
        return "Error: Unable to load AI model. Please contact support."
    messages = history + [{"role": "user", "content": prompt}]
    response = openai.chat.completions.create(model=model, messages=messages)
    return response

def get_gpt_card():
    try:
        model = st.session_state.get('AI_MODEL', None)
        text = query_chatgpt(full_prompt, model=model).choices[0].message.content
        log_text(text, model=model)
        return text
    except Exception as e:
        return f"Error: {e} [{len(api_key)} {len(full_prompt)}]"

if __name__ == "__main__":
    print(get_gpt_card())
