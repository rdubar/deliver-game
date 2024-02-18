import os

def load_data(filename, split=False):
    current_script_dir = os.path.dirname(__file__)
    data_dir = os.path.join(current_script_dir, 'data')
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
