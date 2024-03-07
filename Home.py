import streamlit as st

# streamlit run Home.py

st.set_page_config(page_title="Delivery Game", page_icon=":game_die:")

# Title of the app
st.title('The Delivery Game')

"""
Welcome to **Deliverance**, a fun game for 1-5 players aged 8 and up.

This page can use AI to generate unique game cards every time you play!

You can find the game board, rules, card generator, and feedback form in the menu.

Please enjoy!

-- Rog
"""

st.page_link("pages/1_Card_Generator.py", label = "Card Generator", icon="🎴")
st.page_link("pages/2_Board.py", label = "Game Board", icon="🎲")
st.page_link("pages/3_Rules.py", label = "Rules", icon="📜")
st.page_link("pages/4_Special_Delivery.py", label = "Special Delivery", icon="📦")
st.page_link("pages/7_Feedback.py", label = "Feedback", icon="📝")
