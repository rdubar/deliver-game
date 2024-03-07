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

# set up 2 columns
col1, col2 = st.columns(2)
with col1:
    st.page_link("pages/1_Card_Generator.py", label = "Card Generator", icon="🎴")
    st.page_link("pages/2_Board.py", label = "Game Board", icon="🎲")
    st.page_link("pages/3_Rules.py", label = "Rules", icon="📜")
    st.page_link("pages/4_Special_Delivery.py", label = "Special Delivery", icon="📦")
with col2:
    st.page_link("pages/5_Resources.py", label = "Resources", icon="📚")
    st.page_link("pages/6_Thanks.py", label = "Thanks", icon="🙏")
    st.page_link("pages/7_Feedback.py", label = "Feedback", icon="📝")
    st.page_link("pages/8_Share.py", label = "Share", icon="📚")
