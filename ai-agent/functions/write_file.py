import os
import functions.utils as utils
from google.genai import types

def write_file(working_directory, file_path, content):
    abs_file_path, error = utils.get_validated_path(working_directory, file_path)

    if abs_file_path is None:
        return error or "Error: An unknown validation error occured"
    
    if os.path.isdir(abs_file_path):
        return f'Error: Cannot write to {file_path} as it is a directory'
    
    os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)

    with open(abs_file_path, "w") as f:
        f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Overwrites specified file with provided content",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write to",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Provided content to write into the file"
            )
        },
        required=["file_path", "content"]
    ),
)