import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

        valid_taget_dir = (
            os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        )

        if not valid_taget_dir:
            return f'Result for {directory} directory:\nError: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir):
            return f'Result for {directory} directory:\n Error: "{directory}" is not a directory'

        # return f'Success: "{directory}" is within the working directory'

        file_list = os.listdir(target_dir)

        return_string = f"Result for '{directory}' directory:\n"

        for file in file_list:
            size = os.path.getsize(os.path.join(target_dir, file))
            is_dir = os.path.isdir(os.path.join(target_dir, file))

            return_string += f"{file}: file_size={size} bytes, is_dir={is_dir}\n"

        return return_string
    except (OSError, ValueError) as e:
        return f"Result for {directory} directory:\n Error: {e}"
