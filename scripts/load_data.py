import pandas as pd
import os

from.utils import get_data_directory

def load_csv_file(filename):
    file_path = os.path.join(get_data_directory(), filename)
    print(f"Attempting to load file at: {file_path}")
    return pd.read_csv(file_path)