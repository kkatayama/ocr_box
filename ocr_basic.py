import cv2
import sys
import pytesseract

def pass_image(imPath, psm):
    # Uncomment the line below to provide path to tesseract manually
    # pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

    # Define config parameters.
    # '-l eng'  for using the English language
    # '--oem 1' for using LSTM OCR Engine
    #   config = ('-l eng --oem 1 --psm 3')
    config = ('--tessdata-dir "tessdata_best" -l eng --oem 1 --dpi 72 --psm ' + str(psm)) 
    # Read image from disk
    im = cv2.imread(imPath, cv2.IMREAD_COLOR)

    # Run tesseract OCR on image
    text = pytesseract.image_to_string(im, config=config, output_type='dict')
    data = pytesseract.image_to_data(im, config=config, output_type='dict')

    return text, data

if __name__ == '__main__':
      
    if len(sys.argv) < 2:
        print('Usage: python ocr_simple.py image.jpg')
        sys.exit(1)
   
    # Read image path from command line
    imPath = sys.argv[1]

    # Read psm mode from command line
    psm = sys.argv[2]

    text, data = pass_image(imPath, psm)
    d = '{' + '\n'.join(str(' '+repr(k) + ': ' + str(v)) for k,v in data.items()).strip() + '}'
    print(text['text'])
    print(d)
