import os
import argparse
import subprocess
import functions.utils as utils

def run_python_file(working_directory, file_path, args=None):
    validated_path, error = utils.get_validated_path(working_directory, file_path)
    if validated_path is None:
        return error or 'Error occurred validating path'

    if not utils.is_file(working_directory, file_path):
        return f'Error: "{file_path}" does not exist or is not a regular file'
    
    if not validated_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file'
    
    command = ["python", validated_path]

    if args:
        command.extend(args)

    try:
        output = subprocess.run(
            command,
            cwd=os.path.dirname(validated_path),
            capture_output=True,
            text=True,
            timeout=30
        )

        output_list = []

        if output.returncode != 0:
            output_list.append(f"Process exited with code {output.check_returncode}")
        
        if not output.stdout.strip() and not output.stderr.strip():
            output_list.append("No output produced")
        else:
            if output.stdout:
                output_list.append(f'STDOUT: {output.stdout.strip()}')
            if output.stderr:
                output_list.append(f'STDERR: {output.stderr}')
        
        return "\n".join(output_list)
    
    except subprocess.TimeoutExpired:
        return "Process timed out after 30 seconds"
    except Exception as e:
        return f'Error executing Python file: {e}'