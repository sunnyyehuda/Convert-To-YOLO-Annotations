# Convert-To-YOLO-Annotations
convert single text of classic annotations to a multiple text file of YOLO annotations

# convert-annotations-yolov3.py
this script convert a single text file of annotations in the format:
image.jpg:[xmin1, ymin1, width1, height1, class1],..,[xminN, yminN, widthN, heightN, classN]
where every line belongs each image, and every couple of parentheses belongs to a object that in the picture.
- xmin, ymin are the coordinates of the bounding block (at the top left corner).
- width, height are the dimension of the bounding box.
- class is the object that we want to train (from 1 to N)

# reminder
yolo annotation format (.txt per .jpg):
class x y width height

- class now go from 0 to N-1
- x, y are the center coordinates of the bounding box devided by width and the height of the picture
- width, height as before but devided by width and the height of the picture

# make_test_train.py
this script make to text file for test and train and fill them with the images.
the script is configurable, by default the duty cycle of train/test division is 4/1 (or 80% for train and 20% for test)
