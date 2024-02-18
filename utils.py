import os

# current_script_dir = os.path.dirname(__file__)


def load_data(filename, split=False):
    # Use the current working directory as the base
    base_dir = os.getcwd()
    data_dir = os.path.join(base_dir, 'data')
    file_path = os.path.join(data_dir, filename)
    
    try:
        with open(file_path, 'r') as f:
            data = f.read()
        if split:
            data = data.split('\n')
        return data
    except Exception as e:
        print(f"Error loading data from {file_path}: {e}")
        return None
