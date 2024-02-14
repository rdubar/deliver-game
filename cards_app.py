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
    st.write("""
    # Deliverance: The Delivery Game
    ### or Every Van For Themselves...
    * Each player starts at the Depot on the game board.
    * Each player throws the dice, the highest throw goes first.
    * Each player throws a dice, goes forward that number of stars, then takes a card.
    * Card bonuses or penalties are applied….
    * If the player has gone round the board and reached the depot, they get another star!
    * Players may gain “Lucky Break” tokens, which can be used once each only, at any time, to avoid a penalty. Use them wisely!
    * The winner is the first player to collect five stars.
    """)

    # Sidebar download button for the PDF
    with open("Game_Board.pdf", "rb") as file:
        st.download_button(
                label="Download Game Board",
                data=file,
                file_name="Game_Board.pdf",
                mime="application/octet-stream"
            )

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
