# Utilities 
import os

def load_data(file, split=False):
    if not os.path.exists(file):
        file = os.path.join('data', file)
    try:
        with open(file, 'r') as f:
            data = f.read()
        if split:
            data = data.split('\n')
        return data
    except Exception as e:
        print(e)
        return None
