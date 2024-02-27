import streamlit as st
import os
import pandas as pd
from tools.settings import PROMPT, CARDS, OPEN_AI_API_KEY, WORDCLOUD_PATH, show_gitub_repo_link
from tools.mongo_logger import mongo_db
from tools.wordcloud_tool import make_game_wordcloud


st.set_page_config(page_title="Delivery Game", page_icon=":game_die:")

# create anchor at top of page
st.markdown("<a id='top'></a>", unsafe_allow_html=True)

st.title('Resources')

# get all records, to test if we want to show this content
# records = get_all_records()
records = mongo_db.get_records()

# Create a table of contents
st.markdown("[Source Code](#source-code)")
st.markdown("[Default Game Cards](#default-game-cards)")
if OPEN_AI_API_KEY:
    st.markdown("[AI Prompt](#ai-prompt)")
if records:
    st.markdown("[AI Generated Cards](#ai-generated-cards)")
st.markdown("[Wordcloud](#wordcloud)")
st.markdown("[Statistics](#statistics)")

# Create the content
st.header("Source Code")
show_gitub_repo_link()

st.header("Default Game Cards")
st.text_area("Default Game Cards:", value=CARDS, height=400, max_chars=1500, key='cards')

if OPEN_AI_API_KEY:
    st.header("AI Prompt")
    st.text_area("AI Prompt (used with the game rules and standard cards to generate new cards):", 
        value=PROMPT, height=400, max_chars=1500, key='prompt')

if records:
    st.header("AI Generated Cards:")
    text = ""
    count = 0
    print(f'Found {len(records)} records in MongoDB.')
    for record in records:
        if not 'tag' in record or record['tag'] != 'generated_text':
            continue
        entry = record['text']
        if "example log entry" in entry:
            continue
        count += 1
        time = record['timestamp'].strftime("%Y-%m-%d %H:%M")
        model = record['model'] if 'model' in record else 'gpt-3.5-turbo'
        entry = entry.replace("\\n", "\n").replace("\\'", "'")
        text += f"{time}  {model:20}\n{entry}\n\n"
    st.text_area(f"There have been {count:,} AI Generated Cards", text, height=400)


if not os.path.exists(WORDCLOUD_PATH):
    make_game_wordcloud()
    
st.header("Wordcloud")

"""
This is a wordcloud of all of the text in the game:
"""
try:
    st.image(WORDCLOUD_PATH)
except Exception as e:
    st.write(f"Error: {e}")

st.header("Statistics")
st.text(mongo_db.text_report())

records = mongo_db.get_records() 

# Initialize a dictionary to hold the counts for each tag by day
records_by_day_and_tag = {}

for record in records:
    if 'timestamp' in record and 'tag' in record:  # Ensure both keys exist
        day = record['timestamp'].strftime("%Y-%m-%d")
        tag = record['tag']  # Assuming each record has a 'tag' that is either 'feedback' or 'generated_text'
        
        # Initialize the day if not already present
        if day not in records_by_day_and_tag:
            records_by_day_and_tag[day] = {'feedback': 0, 'generated_text': 0}
        
        # Increment the count for the specific tag on this day
        if tag in ['feedback', 'generated_text']:  # Safety check, in case there are other tags
            records_by_day_and_tag[day][tag] += 1

# Convert the dictionary to a DataFrame for easy plotting
df = pd.DataFrame.from_dict(records_by_day_and_tag, orient='index').fillna(0)
df.index = pd.to_datetime(df.index)  # Convert index to datetime for proper plotting
df.sort_index(inplace=True)  # Sort the DataFrame by date

# Plotting with Streamlit
st.bar_chart(df)

# link to top of page
st.markdown("<a href='#top'>Back to top</a>", unsafe_allow_html=True)