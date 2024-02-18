import streamlit as st
from mongo_logger import get_all_records

st.title('Statistics')

"""
This page shows the text of cards that have been generated using OpenAI's GPT-3 model.

Every time you click the button to create a new card, the text of the card is added to the list below.

No personal data is stored or used in the generation of these cards.
"""

data = get_all_records()

if data:
    text = ""
    for record in data:
        time = record['timestamp'].strftime("%Y-%m-%d %H:%M:%S")
        text += f"{time}   {record['generated_text']}\n"
    st.text_area("Generated Cards", text, height=400)