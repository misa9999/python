import os
from PIL import Image


def main(path, new_width=800):
    if not os.path.isdir(path):
        raise NotADirectoryError(f"{path} not exists")

    for root, dirs, files in os.walk(path):
        for file in files:
            complete_path = os.path.join(root, file)
            file_name, extension = os.path.splitext(file)

            converted_tag = "_CONVERTED"

            new_file = file_name + converted_tag + extension
            new_file_full_path = os.path.join(root, new_file)

            # if converted_tag in complete_path:
            #     os.remove(complete_path)
            # continue

            if os.path.isfile(new_file_full_path):
                continue

            if converted_tag in complete_path:
                continue

            img_pillow = Image.open(complete_path)
            # exif = img_pillow._getexif()
            # print(exif)
            # continue
            width, height = img_pillow.size
            new_height = round(new_width * height / width)

            new_image = img_pillow.resize((new_width, new_height), Image.LANCZOS)

            new_image.save(
                new_file_full_path,
                optimize=True,
                quality=70,
                # exif=img_pillow.info["exif"],
            )

            print(f"{complete_path} converted successfully")
            new_image.close()
            img_pillow.close()

            # os.remove(complete_path)


if __name__ == "__main__":
    main_images_folder = "/home/anthrax/git/python/courses/python3/ch5/21_lesson/imgs"
    main(main_images_folder, new_width=1920)
