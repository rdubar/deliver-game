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

# Initialize the fortunes list in the session state if it doesn't exist
if 'fortunes' not in st.session_state:
    st.session_state.fortunes = load_fortunes(fortune_path)
        
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
Experience all the thrills of being a delivery driver, battling with traffic, customers, huge corporations and faceless AI systems, all from the comfort of your own home! 
* Each player starts at the Depot on the game board.
* Each player throws one six sided dice, the highest throw goes first.
* Each player throws the dice, and moves forward that number of spaces, then takes a card.
* Card bonuses or penalties are applied: move forward of backward as directed.
* If the player has gone forward round the board and reached the Depot, they collect another star!
* If you are unlucky, you may lose a star, or have to go back to the Depot without collecting a star.
* Players may gain “Lucky Break” tokens, which can be used once each at any time to avoid any one penalty. Use them wisely!
* If you land on a "Lucky Break" space, take a Lucky break token. 
* If a card says you lose "Lucky Break" or stars but have none left to lose, miss a turn instead. 
* The winner is the first player to collect five stars.
Comments and suggestions are welcome!
    """)

    # Adding a clickable email address
    st.markdown('**Send your feedback:** [rdubar@gmail.com](mailto:rdubar@gmail.com)', unsafe_allow_html=True)

# Throw a dice
if st.button('Throw the dice'):
    dice = random.randint(1, 6)
    st.write(f"You threw a {dice}!")

# Show a card button
if st.button('Show me my card'):
    if not st.session_state.fortunes:
        # Reload fortunes if all have been shown
        st.session_state.fortunes = load_fortunes(fortune_path)
        st.write("All fortunes have been shown. Starting over.")
    else:
        # Select a random fortune and remove it from the list to avoid duplicates
        fortune = random.choice(st.session_state.fortunes)
        st.session_state.fortunes.remove(fortune)
        # Display the selected fortune
        st.write(fortune)
