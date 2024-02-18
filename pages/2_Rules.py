import streamlit as st
from utils import load_data

st.title('Rules of the Game')

rules = load_data('rules.md')

# Sidebar download button for the PDF
with open("Game_Board.pdf", "rb") as file:
    st.download_button(
            label="Download Game Board",
            data=file,
            file_name="Game_Board.pdf",
            mime="application/octet-stream"
        )        
st.write(rules)

# Adding a clickable email address
st.markdown('**Send your feedback:** [rdubar@gmail.com](mailto:rdubar@gmail.com)', unsafe_allow_html=True)