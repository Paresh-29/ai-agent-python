import os
import subprocess
from google.genai import types


def run_python_file(working_directory: str, file_path: str, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_working_dir, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(abs_file_path):
        return f'Error: File "{file_path}" not found.'

    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        output = subprocess.run(
            ["python3", abs_file_path, *args],
            cwd=abs_working_dir,
            timeout=30,
            text=True,
            capture_output=True,
        )

        final_string = f"""
        STDOUT: {output.stdout}
        STDERR: {output.stderr}
        """

        if output.stdout == "" and output.stderr == "":
            final_string += "No output produced.\n"

        if output.returncode != 0:
            final_string += f"process exited with code {output.returncode}"

        return final_string

    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a pyhton file with python3 interpreter, Accepts additional CLI args as an optional array",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to run, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="An optional array of string to be used as the CLI args for the python file",
                items=types.Schema(type=types.Type.STRING),
            ),
        },
    ),
)
