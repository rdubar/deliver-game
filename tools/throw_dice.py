import streamlit as st 
import random

def st_throw_dice_button(sides=6, show_sides=True):
    # Button to throw the dice
    button_text = f"Throw a {sides}-sided dice" if show_sides else "Throw the dice"
    if st.button(button_text):
        dice = random.randint(1, sides)
        
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