def get_extension(filename):
    filename = filename.strip()

    # Case of missing extensions
    if "." not in filename or filename[-1] == '.':
        return  "none"

    return filename.split(".")[-1]