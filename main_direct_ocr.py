import ocr
import os


if not os.path.exists('outfiles'):
    os.makedirs('outfiles')

image_file = r'outfiles\image.jpg'

ocr.filter_image(image_file, True)
text = ocr.run_ocr(image_file)

print(text)
with open(r'outfiles\infile.txt', 'w') as f:
    f.write(text)