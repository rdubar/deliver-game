import streamlit as st
from tools.settings import SPECIAL
from tools.throw_dice import st_throw_dice_button

st.set_page_config(page_title="Delivery Game", page_icon=":game_die:")

st.title("Special Abilities")

"""
*Optional Special Ability Rules:*
* Each player has one special ability at a time. 
* Either take a card at random if you have cards, or roll the special dice below to select a special ability at random.
* If another player already has that special ability, roll the dice again,
* If another player has the same special ability, you can barter and trade with them for Stars and Lucky Break tokens at ant time. 
* You can promise to give the next one or more Stars or Lucky Break tokens if the other player accepts this. 
* Once your Special Ability is used up, roll the dice again to select a new one.
* Remember, only one Special Ability can be used per turn, and each player must have a different Special Ability.
"""
st_throw_dice_button(sides=10, show_sides=True)

st.markdown(SPECIAL)

