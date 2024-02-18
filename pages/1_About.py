import streamlit as st

st.title('About the Game')

"""
This game was developed for the Open University U101 module 
*Design thinking: creativity for the 21st century* TMA03 in Febraury 2024.

The game features the ability to generate new "event" cards using OpenAI's GPT-3 model.

Please enjoy!

Your suggestions and feedback are very welcome.

"""

# Adding a clickable email address
st.markdown('**Send your feedback:** [rdubar@gmail.com](mailto:rdubar@gmail.com)', unsafe_allow_html=True)

# Sidebar download button for the PDF
with open("Game_Board.pdf", "rb") as file:
    st.download_button(
            label="Download Game Board",
            data=file,
            file_name="Game_Board.pdf",
            mime="application/octet-stream"
        )        

