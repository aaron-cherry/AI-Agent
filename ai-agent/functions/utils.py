import os

def get_validated_path(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))

    if os.path.commonpath([abs_working_dir, abs_file_path]) != abs_working_dir:
        return None, f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    return abs_file_path, None

def is_file(working_directory, file_path):
    validated_path, error = get_validated_path(working_directory, file_path)

    if validated_path is None:
        return error or "Error occurred while validating path is in permitted directory"

    return os.path.isfile(validated_path)
    