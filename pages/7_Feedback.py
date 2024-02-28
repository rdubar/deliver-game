import streamlit as st
from tools.mongo_logger import mongo_db
from tools.settings import is_running_locally
from tools.mongo_chart import st_mongo_chart

st.set_page_config(page_title="Delivery Game", page_icon=":game_die:")

st.title("Feedback")

"""
We'd love to hear your thoughts on the game. Please fill out the form below.

You can leave your name, location and email address if you like!

No personal data will be stored or used for any purpose other than improving the game.
"""

with st.form(key="feedback_form"):
    feedback = st.text_area("What do you think of the game?")
    submit = st.form_submit_button("Submit")

if submit:
    values = {
        "text": feedback,
        "tag": "feedback"
    }
    # log_mongo(values)
    mongo_db.write_log(values)
    st.write("Thank you for your feedback!")

# Only show feedback received if running locally
if is_running_locally():

    st.subheader("Statistics")

    # Show the chart
    st_mongo_chart()

    feedback = mongo_db.get_feedback()
    if feedback:
        st.subheader("Feedback Received:")
        # show newest feedback first
        feedback.reverse()
        for entry in feedback:
            entry['timestamp'] = entry['timestamp'].strftime("%Y-%m-%d %H:%M")
            st.write(entry)
    else:
        st.write("No feedback received yet.")