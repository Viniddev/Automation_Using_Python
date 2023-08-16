import os

def organize_folder():
    types = ["jpg", "png", "zip", "pdf", "svg"]

    base_Path = os.path.expanduser("~")
    path = os.path.join(base_Path, "Downloads")

    cwd = os.chdir(path)
    full_List = os.listdir(cwd)

    for type_ in types:
        if type_ not in os.listdir():
            os.mkdir(type_)

    for file in full_List:
        for type_ in types:
            if "." + type_ in file:
                old_path = os.path.join(path, file)
                new_path = os.path.join(path, type_, file)
                os.replace(old_path, new_path)


if __name__ == "__main__":
    organize_folder()

