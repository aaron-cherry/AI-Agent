import os

def get_files_info(working_directory, directory="."):
    try:
        abs_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_path, directory))

        valid_target_dir = os.path.commonpath([abs_path, target_dir]) == abs_path

        if not os.path.isdir(target_dir): return f'Error: {directory} is not a directory'
        if not valid_target_dir: return Exception(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')

        display_string = ""
        for item in os.listdir(target_dir):
            item_path = os.path.join(target_dir, item)
            display_string += f'- {item}: file_size={os.path.getsize(item_path)}, is_dir={os.path.isdir(item_path)}\n'
        
        return display_string

    except Exception as e:
        return f'Error: {str(e)}'
