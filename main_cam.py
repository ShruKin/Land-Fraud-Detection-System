import requests
import creds
import ocr
import cv2
import numpy as np



# instantaneous auto-focused capture URL
url_af = f'http://{creds.username}:{creds.password}@{creds.ip}/photoaf.jpg'

# continuous video feed capture
capture = cv2.VideoCapture(f'http://{creds.username}:{creds.password}@{creds.ip}/video')

# .jpg image file name
image_file = r'outfiles\image.jpg'



while True:
    ret, frame = capture.read()

    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # grayscaling the image
    _, th = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU) # applying otsu binarization

    cv2.imshow('frame', th)

    k = cv2.waitKey(1)

    if k == 32: # RETURN Key is pressed
        r = requests.get(url_af)
        with open(image_file, 'wb') as f:
            f.write(r.content)
            
        ocr.filter_image(image_file, False)
        text = ocr.run_ocr(image_file)

        print(text)
        with open(r'outfiles\infile.txt', 'w') as f:
            f.write(text)


    if k == 27: # ESC Key is pressed
        break