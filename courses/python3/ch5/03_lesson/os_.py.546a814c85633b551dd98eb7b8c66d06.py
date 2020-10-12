import os


file_path = input("Type a path: ")
file_path2 = os.path.expanduser("~/")
print(file_path2 + file_path)
search = input("Search file: ")


def format_size(size):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if size < kilo:
        text = "B"
    elif size < mega:
        size /= kilo
        text = "K"
    elif size < giga:
        size /= mega
        text = "M"
    elif size < tera:
        size /= giga
        text = "G"
    elif size < peta:
        size /= tera
        text = "T"
    else:
        size /= peta
        text = "P"

    size = round(size, 2)
    return f"{size}{text}".replace(".", ",")


count = 0
for root, folders, files in os.walk(file_path2 + file_path):
    for file in files:
        if search in file:
            try:
                count += 1
                full_path = os.path.join(root, file)
                file_name, file_extension = os.path.splitext(file)
                size = os.path.getsize(full_path)

                print()
                print("Found the file:", file)
                print("Path:", full_path)
                print("Name:", file_name)
                print("Extension:", file_extension)
                print("Size:", size)
                print("Real size:", format_size(size))
            except PermissionError as e:
                print("Without permissions")
            except FileNotFoundError as e:
                print("File not found")
            except Exception as e:
                print("Unkown error:", e)

print()
print(f"{count} files found")
