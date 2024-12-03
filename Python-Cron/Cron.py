import os

def organize_folder():
    types = [
        "jpg", "png", "zip", "pdf", "svg", "xlsx", "docx", "exe", "doc", "jpeg", "pptx", "json"
    ]

    base_Path = os.path.expanduser("~")
    path = os.path.join(base_Path, "Documents")

    print(path)

    cwd = os.chdir(path)
    full_List = os.listdir(cwd)

    for files in os.listdir():
        document = files.split(".")
        if len(document) > 1:
            if document[len(document)-1] not in types:
                types.append(document[1])

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
