import os

def get_file_contents(root_dir, file_name="demo.pybul"):
    file_contents = []

    for dirpath, _, filenames in os.walk(root_dir):
        if file_name in filenames:
            file_path = os.path.join(dirpath, file_name)
            with open(file_path, 'r') as file:
                content = file.read().strip()
                file_contents.append(content)

    return file_contents