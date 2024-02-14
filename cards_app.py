import streamlit as st
import random
import os

# streamlit run cards_app.py

fortune_file = "delivery.txt"
fortune_path = os.path.join(os.path.dirname(__file__), fortune_file)

st.set_page_config(page_title="Random Card", page_icon=":game_die:")

def load_fortunes(filename):
    with open(filename, 'r') as file:
        fortunes = file.readlines()
    return [fortune.strip() for fortune in fortunes]

fortunes = load_fortunes(fortune_path)
        
# Title of the app
st.title('The Delivery Game')

# Sidebar with the rules of the game
with st.sidebar:
    st.write("## Rules of the Game")

    # Sidebar download button for the PDF
    with open("Game_Board.pdf", "rb") as file:
        st.download_button(
                label="Download Game Board",
                data=file,
                file_name="Game_Board.pdf",
                mime="application/octet-stream"
            )
        
    st.write("""
    # Deliverance: The Delivery Game
    ### *or Every Van For Themselves...*
    * Each player starts at the Depot on the game board.
    * Each player throws one six sided dice, the highest throw goes first.
    * Each player throws the dice, and moves forward that number of squares, then takes a card.
    * Card bonuses or penalties are applied: move forward of backward as directed.
    * If the player has gone forward round the board and reached the Depot, they collect another star!
    * Players may gain “Lucky Break” tokens, which can be used once each only, at any time, to avoid any one penalty. Use them wisely!
    * The winner is the first player to collect five stars.

    Comments and suggestions are welcome!
    """)

    # Adding a clickable email address
    st.markdown('**Send your feedback:** [rdubar@gmail.com](mailto:rdubar@gmail.com)', unsafe_allow_html=True)

# Main content area for the fortune card functionality
# When the button is pressed
if st.button('Show me my card'):
    if not fortunes:
        fortunes = load_fortunes(fortune_path)
    # Select a random fortune
    fortune = random.choice(fortunes)
    # Remove the fortune from the list
    fortunes.remove(fortune)
    # Display the selected fortune
    st.write(fortune)
