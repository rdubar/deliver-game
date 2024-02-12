import streamlit as st
import random

# List of fortunes
fortunes = [
    "You will have a great day!",
    "Be cautious of unexpected offers.",
    "An exciting opportunity lies ahead.",
    "Happiness begins with facing life with a smile and a wink.",
    "Today is a lucky day for those who remain cheerful and optimistic.",
    "Your ability to juggle many tasks will take you far.",
    "A friend asks only for your time, not your money.",
    "You will travel to many exotic places in your lifetime.",
    "Your talents will be recognized and suitably rewarded.",
    "A pleasant surprise is waiting for you."
]

# Title of the app
st.title('Your Fortune for Today')

# When the button is pressed
if st.button('Show me my fortune'):
    # Select a random fortune
    fortune = random.choice(fortunes)
    # Display the selected fortune
    st.write(fortune)
