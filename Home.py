import streamlit as st
import random
from tools.settings import CARDS, SHOW_GENERATED_CARD
from tools.gpt_cards import get_gpt_card

# streamlit run Home.py

st.set_page_config(page_title="Delivery Game", page_icon=":game_die:")

def load_fortunes():
    return CARDS.split('\n')

# Initialize the fortunes list in the session state if it doesn't exist
if 'fortunes' not in st.session_state:
    st.session_state.fortunes = load_fortunes()

# Title of the app
st.title('The Delivery Game')

# Initialize or update session state for the last throw and count
if 'last_throw' not in st.session_state:
    st.session_state['last_throw'] = None
    st.session_state['repeat_count'] = 0

# Button to throw the dice
if st.button('Throw the dice'):
    dice = random.randint(1, 6)
    
    # Check if the same number was thrown as last time
    if dice == st.session_state['last_throw']:
        st.session_state['repeat_count'] += 1
        messages = [
            f"Wow, another {dice}!",
            f"Again a {dice}!",
            f"{dice}, yet again!",
        ]
        # Cycle through messages based on how many times the same number has been thrown
        msg = messages[st.session_state['repeat_count'] % len(messages)]
    else:
        # Reset the repeat count and update the last throw
        st.session_state['repeat_count'] = 0
        st.session_state['last_throw'] = dice
        msg = f"You threw a {dice}!"
    
    st.write(msg)

# Show a card button
if st.button('Show me a card from the deck'):
    if not st.session_state.fortunes:
        # Reload fortunes if all have been shown
        st.session_state.fortunes = load_fortunes()
    # Select a random fortune and remove it from the list to avoid duplicates
    fortune = random.choice(st.session_state.fortunes)
    st.session_state.fortunes.remove(fortune)
    # Display the selected fortune
    st.write(fortune)

if SHOW_GENERATED_CARD:
    # AI model selector
    # show a gpt-3 card
    if st.button("Generate a unique card using gpt-3.5-turbo"):
        st.write(get_gpt_card(model="gpt-3.5-turbo"))

    # show a gpt-4 card
    if st.button("Generate a unique card using gpt-4"):
        st.write(get_gpt_card(model="gpt-4"))