import PIL
from PIL import Image
from PIL import ImageOps
import numpy as np
import glob

def convert_annotation(old_object, width, height):
    vals = old_object.split(',')
    x_center = float(vals[0]) + 0.5*float(vals[2])
    y_center = float(vals[1]) + 0.5*float(vals[3])

    object_class_id = int(vals[4]) - 1
    x_center = x_center/width
    y_center = y_center/height
    width = float(vals[2])/width
    height = float(vals[3])/height

    return "{0} {1} {2} {3} {4}".format(object_class_id, x_center, y_center, width, height)

if __name__ == '__main__':
    f = open("annotationsTrain.txt", "r")
    # every line in f is single file annotation
    for single_file in f:
        # get the file name
        file_name = single_file[:single_file.index('.')]
        annotation_file = open("{}.txt".format(file_name), "w")
        # slice the file name
        single_file = single_file[single_file.index(':')+1:]
        # cut the '[' at beginning and the ']' at end
        single_file = single_file[1:-2]
        objects = single_file.split('],[')
        for single_object in objects:
            new_element = convert_annotation(single_object, 3648, 2736) #these are the width and the height of the image
            annotation_file.write(new_element+"\n")
        annotation_file.close()
    f.close()






