import os
import argparse
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
try:
    from .settings import IMAGES_DIR, FULL_PROMPT
except ImportError:
    from settings import IMAGES_DIR, FULL_PROMPT

def create_wordcloud(text, stopwords=None, filename='wordcloud.png'):
    """
    Generates a word cloud from a given text and saves it to a file.

    Parameters:
    - text (str): The input text from which to generate the word cloud.
    - stopwords (set, optional): A set of words to be excluded from the word cloud.
    - filename (str, optional): The name of the file to save the word cloud image to.
    """
    # Combine the default STOPWORDS with any additional stopwords
    if stopwords is not None:
        current_stopwords = STOPWORDS.union(stopwords)
    else:
        current_stopwords = STOPWORDS

    # Create the WordCloud object
    wordcloud = WordCloud(stopwords=current_stopwords, background_color="black", width=800, height=400).generate(text)

    # Display the generated word cloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    
    # Save the word cloud to a file
    plt.savefig(filename, bbox_inches='tight', pad_inches=0)
    plt.close()

def make_game_wordcloud(text=FULL_PROMPT):
    # Create a word cloud from the text
    output = os.path.join(IMAGES_DIR, 'wordcloud.png')
    create_wordcloud(text, filename=output)
    print(f"Word cloud image saved to {output}")

# Example usage
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate a word cloud from a given text.')
    parser.add_argument('-e', '--example', action='store_true', help='Use example text for the word cloud')
    parser.add_argument('-u', '--update', action='store_true', help='Update the word cloud image')
    args = parser.parse_args()

    print("Wordcloud generator")

    example_text = "This is a sample text for generating a word cloud. Word clouds are visual representations of word frequency."
    custom_stopwords = {'for', 'a', 'are'}  # Example of additional stopwords

    if args.example:
        create_wordcloud(example_text, stopwords=custom_stopwords, filename='example_wordcloud.png')
    
    if args.update:
        make_game_wordcloud()

    # if no args given, just print the help
    if not any(vars(args).values()):
        parser.print_help()
