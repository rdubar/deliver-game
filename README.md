# Random Card

## Overview

This Streamlit App shows random lines of text fom a file, and can also use AI to generate new game cards automagically.

It was made as an aid to a boardgame development project for the Open University's U101 module "Design thinking: creativity for the 21st century". 

You use it to easily try out random cards for games without having to print them out, or even create new game cards every time you play.

The game rules, card text, and AI prompt are in the `data` folder.

Have fun, and modify for your own use as needed.

## Features

- **Random Fortune**: Each click provides a unique, randomly selected fortune from our curated list.
- **ChatGPT AI generated fortune**: Click to generate a unique fortune each time (experimental)
- **Simple UI**: A clean and straightforward interface for easy use.
- **Extensible**: Add your own fortunes to the list by simply editing a text file.
- **Logging**: The time & text of any AI generated cards are logged on MongoDB.
- **Wordcloud**: A wordcloud of words in the game (`python tools/settings.py` to update).
Note that no personal or user data is recorded - just the time the button was pressed, and the text it generated. 

## Getting Started

### Prerequisites

- Python 3.11 recommended
- Streamlit
- OpenAI (for GPT generated cards)
- MongoDB (for logging)

### Installation

If you are unsure about any of these steps you can use ChatGPT to guide you. 

```sh
# Move to the folder you wish to install into, for example in Linux, MacOS or Windows with WSL2:
mkdir -p ~/random-card
cd ~/random-card

# Clone the repository
# gh repo clone rdubar/deliver-game  # if you use gh
git clone https://github.com/rdubar/random-card.git

# Set up a virtual environment (optional, but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies (nb: keep minimal for Streamlit)
pip install -r requirements.txt

# set up API keys as needed by editing .streamlit/secrets.toml
mkdir -p .streamlit && cp secrets.toml .streamlit/secrets.toml

# Running the App

# After installation, run the app using Streamlit:
streamlit run Home.py

# Navigate to http://localhost:8501 in your web browser to view the app.
```
If you do not wish to use the experimental AIU card generator functionality, just set `SHOW_GENERATED_CARD = False` in the `tools/settings.py` file.

## How to Contribute
Your contributions and suggesitons are welcome! If you'd like to add more fortunes or improve the app:

* Fork the repository.
* Create a new branch for your feature (`git checkout -b feature/AmazingFeature`).
* Commit your changes (`git commit -m 'Add some AmazingFeature'`).
* Push to the branch (`git push origin feature/AmazingFeature`).
* Open a Pull Request.

## License
Distributed under the MIT License. See LICENSE for more information.

## Contact
* Roger Dubar, rdubar [at] gmail.com
* Project Link: https://github.com/rdubar/deliver-game
* Example Link: https://deliver-game.streamlit.app/

## Acknowledgements
* The Open University - The U101 Team, for inspiration.
* Streamlit - "The fastest way to build and share data apps."
* Python - The programming language used to create this app.
* ChatGPT - Your friendly AI assistant.

## Todo: 

* Show which engine is used in logged output
* More descriptive link from webpage to the Prompt & this page

