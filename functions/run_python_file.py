import os
import subprocess


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

        valid_target_dir = (
            os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        )

        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        # root, ext = os.path.splitext(target_file)

        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command_list = ["python", target_file]
        if args != None:
            for arg in args:
                command_list.append(arg)

        process = subprocess.run(
            command_list,
            cwd=working_dir_abs,
            capture_output=True,
            text=True,
            timeout=30,
        )

        output = []

        if process.stdout:
            output.append(f"STDOUT: {process.stdout}")

        if process.stderr:
            output.append(f"STDERR: {process.stderr}")

        if not process.stdout and not process.stderr:
            output.append("No output produced")

        if process.returncode != 0:
            output.append(f"Process exited with code {process.returncode}")

        return "\n".join(output)

    except Exception as e:
        return f"Error: executing Python file: {e}"
