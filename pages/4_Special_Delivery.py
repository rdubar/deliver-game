import random
import streamlit as st
from tools.settings import SPECIAL

st.set_page_config(page_title="Delivery Game", page_icon=":game_die:")

st.title("Special Delivery")

"""
*Optional Special Delivery Rules:*
* Each player received a random Special Delivery Card a the start of the game.
* Select a card at random, or use the app to select a random card for you.
* Special Delivery cards may be used as indicated. One used, they are returned to the deck.
* Players may trade one Star or one Lucky Break token for a new Special Delivery Card
* Players may trade Special Delivery cards with each other at any time, for free, or for Stars or Lucky Break tokens.
* Only one Special Delivery card can be used per turn.
"""

# Initialize or reset the special_list in session state
if 'special_list' not in st.session_state or 'last_special' not in st.session_state:
    st.session_state.special_list = []
    st.session_state.last_special = "No Special Delivery Card"

def create_special_list():
    special_list = SPECIAL.split('\n\n')  # Split the string into a list
    special_list = [x for x in special_list if x]  # Remove empty lines
    random.shuffle(special_list)  # Shuffle the list
    return special_list

# Create button to draw a random special delivery card
if st.button("Draw a Special Delivery Card"):
    if not st.session_state.special_list:  # If the list is empty, create a new list
        st.session_state.special_list = create_special_list()  # Create and store a new list in session state
    st.session_state.last_special = st.session_state.special_list.pop()  # Pop the last item from the list
    st.write(st.session_state.last_special)  # Display the last item

# Privide a help area with all of the special delivery cards
st.divider()
with st.expander("Special Delivery Cards"):
    st.write(SPECIAL)