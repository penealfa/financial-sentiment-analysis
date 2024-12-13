import os

def get_data_directory():
    project_root = os.path.dirname(os.path.abspath(__file__ + "/../"))
    return os.path.join(project_root, 'data/')

def get_output_file_path(filename):
    data_dir = get_data_directory()
    return os.path.join(data_dir, filename)