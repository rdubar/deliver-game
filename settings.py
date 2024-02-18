import os

"""
Global settings for the Random Card Generator app.
"""

# Set to False to hide the experimental AI card generator feature
SHOW_GENERATED_CARD = True

base_dir = os.getcwd()

data_dir = os.path.join(base_dir, 'data')

images_dir = os.path.join(base_dir, 'images')

wordcloud_path = os.path.join(images_dir, 'wordcloud.png')

