# USAGE: python ocr_basic.py --image [FILE] --psm [0-13] --lang [language]
#
# python ocr_basic.py --image images/example_01.png
# python ocr_basic.py --image images/example_01.png --psm 3
# python ocr_basic.py --image images/example_01.png --psm 3 --lang eng 
import pytesseract
import argparse
import cv2
import sys

def pass_image(image_file, psm, language):
    # Define config parameters.
    config = ('--tessdata-dir "tessdata_best" -l eng --oem 1 --dpi 72 --psm {} -l {}'.format(psm, language)) 

    # Read image from disk
    im = cv2.imread(image_file, cv2.IMREAD_COLOR)

    # Run tesseract OCR on image
    text = pytesseract.image_to_string(im, config=config, output_type='dict')
    data = pytesseract.image_to_data(im, config=config, output_type='dict')

    return text, data

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("--image",
                    required=True,
                    help="path to image file")
    ap.add_argument("--psm",
                    default="3",
                    help="Page segmentation mode")
    ap.add_argument("--lang",
                    default="eng",
                    help="language")
    args = vars(ap.parse_args())

    text, data = pass_image(args["image"], args["psm"], args["lang"])
    d = '{' + '\n'.join(str(' '+repr(k) + ': ' + str(v)) for k,v in data.items()).strip() + '}'
    print(text['text'])
    print(d)
