import streamlit as st
from tools.mongo_logger import get_all_records

st.title('Statistics')

"""
This page shows the text of cards that have been generated using OpenAI's GPT models.

Every time you click the button to create a new card, the text of the card is added to the list below.

No personal data is stored or used in the generation of these cards.
"""

data = get_all_records()

if data:
    text = ""
    count = 0
    for record in data:
        entry = record['generated_text']
        if "example log entry" in entry:
            continue
        count += 1
        time = record['timestamp'].strftime("%Y-%m-%d %H:%M")
        text += f"{time}   {entry}\n"
    st.text_area(f"{count:,} Generated Cards", text, height=400)