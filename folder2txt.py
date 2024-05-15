from os import listdir
import shutil

new_filename = 'base_labels_v1-1'
IMAGE_DIR = '/media/christian/USB STICK/Images/Images'
LABEL_PATH = f'/media/christian/USB STICK/labels/{new_filename}.txt'
merge_directories = False



def merge_classes(): # places all images into the parent folder
    #only works if only folders are present in directory
    folders = listdir(IMAGE_DIR)
    with open(LABEL_PATH, "w") as f:
        for folder in folders:
            path = f"{IMAGE_DIR}/{folder}"
            images = listdir(path)
            print(f"class {folder}: {len(images)} images")
            for image in images:
                f.write(f"{image}, {folder}\n")
                if merge_directories:
                    shutil.move(f"{path}/{image}", f"{IMAGE_DIR}/{image}")



if __name__ == "__main__":
    merge_classes()