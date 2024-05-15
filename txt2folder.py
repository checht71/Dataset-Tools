from os import listdir
import shutil

IMAGE_DIR = '/media/christian/USB STICK/Images/Images'
LABEL_PATH = '/media/christian/USB STICK/labels/base_labels.txt'

def read_labels(LABEL_PATH):
    with open(LABEL_PATH) as f:
        return f.readlines()


def sort_images(labels):
    for label in labels:
        img_name, classid = label.split(",")
        classid = classid[0] #remove \n from string
        try:
            old_path = f"{IMAGE_DIR}/{img_name}"
            new_path = f"{IMAGE_DIR}/{classid}/{img_name}"
            shutil.move(old_path, new_path)
        except:
            print(f"{img_name} not found.")


labels = read_labels(LABEL_PATH)
sort_images(labels)