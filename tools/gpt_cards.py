import streamlit as st
import openai
from .settings import load_data, OPEN_AI_API_KEY
from .mongo_logger import mongo_db

openai.api_key = OPEN_AI_API_KEY or None

"""
Use OpenAI's models to generate random cards for the game.
"""

prompt = load_data('prompt.txt')
rules = load_data('rules.md')
cards = load_data('delivery.txt')

full_prompt = prompt + rules + cards

def query_chatgpt(prompt, model=None, history=[]):
    if not OPEN_AI_API_KEY:
        return "No OpenAI API key found. Please contact support."
    if not model:
        return "No AI model specified. Please contact support."
    messages = history + [{"role": "user", "content": prompt}]
    response = openai.chat.completions.create(model=model, messages=messages)
    return response

def get_gpt_card(model=None):
    if not OPEN_AI_API_KEY:
        return "No OpenAI API key found. Please contact support."
    try:
        text = query_chatgpt(full_prompt, model=model).choices[0].message.content
        values = {
            "text": text,
            "tag" : "generated_text"}
        if model:
            values["model"] = model
        mongo_db.write_log(values)
        # log_mongo(values)
        return text
    except Exception as e:
        return f"Error: {e}. Please contact support."

if __name__ == "__main__":
    print(get_gpt_card())
