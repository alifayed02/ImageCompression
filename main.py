import sys

from PIL import Image
import zipfile

def compress_individual_image(path_to_image, save_path):
    image = Image.open(path_to_image)
    image.save(save_path, format="webp", quality=10)

def compress_batch_images(path, image_file_names):
    compression = zipfile.ZIP_DEFLATED
    zip = zipfile.ZipFile("images/compressed/compressed_images.zip", mode="w", compresslevel=9)
    try:
        for image_name in image_file_names:
            image_name_webp = image_name.rsplit(".", 1)[0] + ".webp"
            compress_individual_image(path + image_name, path + "compressed/" + image_name_webp)
            zip.write(path + "compressed/" + image_name_webp, image_name_webp, compress_type=compression)
    except FileNotFoundError as e:
        print(str(e))
    finally:
        zip.close()

def main():
    if len(sys.argv) < 4:
        print("Error: Not enough arguments provided")
        print("Format: python main.py batch <image_folder_path> <list_of_files>")
        print("Format: python main.py individual <path> <list_of_files>")
        return

    type = sys.argv[1]

    if type == "batch":
        path = sys.argv[2]
        files = sys.argv[3].split(",")
        compress_batch_images(path, files)
    elif type == "individual":
        path_to_image = sys.argv[2]
        save_path = sys.argv[3]
        compress_individual_image(path_to_image, save_path)

if __name__=="__main__":
    main()