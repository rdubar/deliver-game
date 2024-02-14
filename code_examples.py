import streamlit as st
import random
import os

# streamlit run code_examples.py

st.set_page_config(page_title="Random Card", page_icon=":card:")

def load_fortunes(filename):
    with open(filename, 'r') as file:
        fortunes = file.readlines()
    return [fortune.strip() for fortune in fortunes]

fortunes = load_fortunes(os.path.join(os.path.dirname(__file__), 'fortunes.txt'))
        
# Title of the app
st.title('Code Examples')

"""
This page shows examples how to create pages with multiple columns, buttons, and expanders.
"""

# When the button is pressed
if st.button('Show me my card', help="Tooltip text for the button"):
    # Select a random fortune
    fortune = random.choice(fortunes)
    
    # Display the selected fortune
    st.write(fortune)


col1, col2 = st.columns(2)  # Create two columns

with col1:  # Use the first column to place the first button
    if st.button('Button 1'):
        st.write('Button 1 was clicked!')

with col2:  # Use the second column to place the second button
    if st.button('Button 2'):
        st.write('Button 2 was clicked!')

with st.expander("Help"):
    st.write("""
        Here's some detailed information to help you understand the app better:
        
        - **Feature 1**: Explanation of feature 1.
        - **Feature 2**: Explanation of feature 2.
        - **Usage tips**: Some tips on how to use the app effectively.
        
        For more assistance, contact support@example.com.
    """)
