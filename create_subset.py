from os import listdir, makedirs, path
import os
import shutil

SUBSET_SIZE_DIVISION = 20     # 4= 1/4, 6=1/6 of original set
IMAGE_DIR = '/media/christian/USB STICK/Images/Images'
SUBSET_DIR = IMAGE_DIR+'/subset'

def make_directory(my_dir):
    try:
        makedirs(my_dir, mode=0o755, exist_ok=False)
        print(my_dir)
    except OSError as error:
        print(f"Error creating directory {my_dir}: {error}")


def merge_classes(): # places all images into the parent folder
    #only works if only folders are present in directory
    folders = listdir(IMAGE_DIR)
    make_directory(SUBSET_DIR)
    for folder in folders:
        make_directory(f"{SUBSET_DIR}/{folder}")
        path = f"{IMAGE_DIR}/{folder}"
        images = listdir(path)
        for index, image in enumerate(images):
            if index % SUBSET_SIZE_DIVISION == 0:
                shutil.move(f"{path}/{image}", f"{SUBSET_DIR}/{folder}/{image}")



if __name__ == "__main__":
    merge_classes()