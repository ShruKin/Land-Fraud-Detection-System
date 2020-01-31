import cv2 # for OpenCV
import numpy as np 
from PIL import Image, ImageFilter # loading and filtering image
import pytesseract     #pytesseract is used to recognise the text from image



def filter_image(image_file, if_rotate):
    img = Image.open(image_file) # in PIL
    if if_rotate:
        img = img.rotate(-90, expand=True) # rotate to straight
    im2 = img.filter(ImageFilter.SHARPEN) # sharpening image
    im3 = im2.filter(ImageFilter.DETAIL) # detaling image
    im3.save(image_file) # rewrite

    # PIL to OpenCV crossover!
    img_cv = cv2.imread(image_file, 0) # in OpenCV
    ret, th = cv2.threshold(img_cv, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU) # applying otsu binarization

    cv2.imwrite(image_file, th) # rewrite



def run_ocr(image_file):
    pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract.exe' # specifying the path to the tesseract.exe file
    img = Image.open(image_file) # accessing the image 
    output_text = pytesseract.image_to_string(img, lang= 'eng') # converting the image contents to string
    # print(output_text) # printing the image contents in terminal
    return output_text