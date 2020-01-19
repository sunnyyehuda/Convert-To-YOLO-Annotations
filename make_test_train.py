import PIL
from PIL import Image
from PIL import ImageOps
import numpy as np
import glob


if __name__ == '__main__':
    f = open("annotationsTrain.txt", "r")
    train = open("train.txt", "w")
    test = open("test.txt", "w")
    # duty cycle is equal to the number of train annotation out of 5, the fifth is for test
    duty_cycle = 4
    counter = 0
    # every line in f is single file annotation
    for single_file in f:
        # get the file name
        file_name = single_file[:single_file.index(':')]
        if counter < duty_cycle:
            train.write("images/"+file_name+"\n")
            counter += 1
        else:
            test.write("images/"+file_name+"\n")
            counter = 0
    test.close()
    train.close()
    f.close()






