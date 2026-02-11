import os

def get_file_content(working_directory, file_path):
    try:
        working_path = os.path.abspath(working_directory)
        abs_file_path = os.path.join(working_path, file_path)
        valid_file = os.path.isfile(abs_file_path)
        valid_path = os.path.commonpath([abs_file_path, working_path]) == working_path

        if not valid_path: return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not valid_file: return f'Error: file not found or is not a regular file: "{file_path}'

        #read file contents only up to 1000 chars
        with open(abs_file_path, "r") as f:
            MAX_CHARS = 10000
            file_content = f.read(MAX_CHARS)
            if f.read(1):
                file_content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return(file_content)

    except Exception as e:
        print(f'Error: {str(e)}')
        return f'Error: {str(e)}'