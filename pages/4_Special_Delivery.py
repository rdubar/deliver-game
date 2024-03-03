import streamlit as st
from tools.settings import SPECIAL
from tools.throw_dice import st_throw_dice_button, init_dice

init_dice()

st.set_page_config(page_title="Delivery Game", page_icon=":game_die:")

st.title("Special Delivery")

"""
*Optional Special Delivery Rules:*
* Each player received a random Special Delivery Card a the start of the game.
* Select a card at random, or use the app to select a random card for you.
* Special Delivery cards may be used as indicated. One used, they are returned to the bottom of the deck.
* Players may trade one Star or one Lucky Break token for a new Special Delivery Card
* Players may trade Special Delivery cards with each other at any time, for free, or for Stars or Lucky Break tokens.
* Only one Special Delivery card can be used per turn.
"""
st_throw_dice_button(sides=10, show_sides=True)

st.markdown(SPECIAL)

