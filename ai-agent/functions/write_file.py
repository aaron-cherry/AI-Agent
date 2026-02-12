import os
import functions.utils as utils

def write_file(working_directory, file_path, content):
    abs_file_path, error = utils.get_validated_path(working_directory, file_path)

    if abs_file_path is None:
        return error or "Error: An unknown validation error occured"
    
    if not utils.is_file(working_directory, file_path):
        return f'Error: Cannot write to {file_path} as it is a directory'
    
    os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)

    with open(abs_file_path, "w") as f:
        f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'