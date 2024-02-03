import glob
import os

def read_file(directory1, directory2, filename):
    """
    Read the contents of a file.

    Parameters:
    directory1 (str): The first directory name.
    directory2 (str): The second directory name.
    filename (str): The name of the file with extension.

    Returns:
    str: The content of the file.

    Raises:
    FileNotFoundError: If the file is not found at the specified path.
    FileNotFoundError: If the specified path is a directory.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    name = os.path.join(parent_dir, directory1, directory2, filename)
    file_paths = glob.glob(name)
    if len(file_paths) == 0:
        raise FileNotFoundError(f'{name} file not found at the specified path.')
    elif len(file_paths) > 1:
        raise FileNotFoundError(f'{name} is a directory. Provide the specified path.')
    else:
        file_path = file_paths[0]
        with open(file_path, 'r') as file:
            content = file.read()
    return content
