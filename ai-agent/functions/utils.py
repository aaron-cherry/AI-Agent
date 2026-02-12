import os

def get_validated_path(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))

    if os.path.commonpath([abs_working_dir, abs_file_path]) != abs_working_dir:
        return None, f'Error: "{file_path}" is outside the permitted working directory'

    if not os.path.isfile(abs_file_path):
        return None, f'Error: File not found or is not a regular file: "{file_path}"'

    return abs_file_path, None