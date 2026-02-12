import os
import functions.utils as utils

def get_file_content(working_directory, file_path):
    try:
        abs_file_path, error = utils.get_validated_path(working_directory, file_path)
        if abs_file_path is None:
            return error or "Error: An unknown validation error occurred"

        if not utils.is_file(working_directory, file_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        with open(abs_file_path, "r") as f:
            MAX_CHARS = 10000
            file_content = f.read(MAX_CHARS)
            if f.read(1):
                file_content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return(file_content)

    except Exception as e:
        print(f'Error: {str(e)}')
        return f'Error: {str(e)}'