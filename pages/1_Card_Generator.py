import streamlit as st
import random
from tools.settings import CARDS, SHOW_GENERATED_CARD
from tools.gpt_cards import get_gpt_card
from tools.throw_dice import st_throw_dice_button, init_dice

init_dice()

st.set_page_config(page_title="Delivery Game", page_icon=":game_die:")

st.title('Card Generator')

def load_fortunes():
    fortunes_list = CARDS.split('\n')
    random.shuffle(fortunes_list)  # Shuffle the list in place
    return fortunes_list

# Initialize or reload the fortunes list in the session state
if 'fortunes' not in st.session_state or not st.session_state.fortunes:
    st.session_state.fortunes = load_fortunes()

# Button to throw the dice
st_throw_dice_button(sides=6, show_sides=True)

# Show a random card from the standard deck button
if st.button('Show me a card from the deck'):
    if not st.session_state.fortunes:  # Check if the fortunes list is empty
        st.session_state.fortunes = load_fortunes()  # Reload fortunes if all have been shown
    fortune = st.session_state.fortunes.pop()  # Pop a fortune from the list
    st.write(fortune)  # Display the selected fortune

if SHOW_GENERATED_CARD:
    # show a gpt-3.5-turbo card
    if st.button("Generate a unique card using gpt-3.5-turbo"):
        st.write(get_gpt_card(model="gpt-3.5-turbo"))

    # show a gpt-4 card
    if st.button("Generate a unique card using gpt-4"):
        st.write(get_gpt_card(model="gpt-4"))
