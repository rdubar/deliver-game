import streamlit as st
import random
from tools.settings import setup_ai_model, CARDS, SHOW_GENERATED_CARD, DEFAULT_AI_MODEL
from tools.gpt_cards import get_gpt_card

# Initialize AI_MODEL in the session state
setup_ai_model()
AI_MODEL = st.session_state.get('AI_MODEL', DEFAULT_AI_MODEL)

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
if st.button('Show me my card'):
    if not st.session_state.fortunes:
        # Reload fortunes if all have been shown
        st.session_state.fortunes = load_fortunes()
    # Select a random fortune and remove it from the list to avoid duplicates
    fortune = random.choice(st.session_state.fortunes)
    st.session_state.fortunes.remove(fortune)
    # Display the selected fortune
    st.write(fortune)

if SHOW_GENERATED_CARD:
    # ge the ai model from the session state
    ai_model = st.session_state.AI_MODEL
    if ai_model:
        if st.button(f"Generate unique card using OpenAI's {ai_model}"):
            st.write(get_gpt_card())
    else:
        st.write("Unable to load AI model. Please contact support.")
