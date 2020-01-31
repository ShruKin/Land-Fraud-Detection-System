import ocr

image_file = 'image.jpg'

ocr.filter_image(image_file, True)
text = ocr.run_ocr(image_file)
print(text)