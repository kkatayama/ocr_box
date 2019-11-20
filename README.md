# OCR TESTS

## ocr_test.py
```YAML
$ python ocr_test.py
```
> This will take all images in the `images` folder and processes each image using the bash `tesseract` command, `ocr_basic.py`, and `ocr.py` using all available parameters.


## ocr_basic.py
```YAML
$ python ocr_basic.py -h
```
> ```YAML
> usage: ocr_basic.py [-h] --image IMAGE [--psm PSM] [--lang LANG]
> 
> optional arguments:
>   -h, --help     show this help message and exit
>   --image IMAGE  path to image file
>   --psm PSM      Page segmentation mode
>   --lang LANG    language
> ```
```YAML
$ python ocr_basic.py --image images/image.jpgsevensegthres.jpg --psm 10 --lang ssd
```
> ```YAML
> 0:44
> {'level': [1, 2, 3, 4, 5]
>  'page_num': [1, 1, 1, 1, 1]
>  'block_num': [0, 1, 1, 1, 1]
>  'par_num': [0, 0, 1, 1, 1]
>  'line_num': [0, 0, 0, 1, 1]
>  'word_num': [0, 0, 0, 0, 1]
>  'left': [0, 284, 284, 284, 284]
>  'top': [0, 18, 18, 18, 18]
>  'width': [996, 686, 686, 686, 686]
>  'height': [301, 242, 242, 242, 242]
>  'conf': ['-1', '-1', '-1', '-1', 96]
>  'text': ['', '', '', '', '0:44']}
> ```

## ocr.py
```YAML
$ python ocr.py -h
```
```YAML
> usage: ocr.py [-h] --image IMAGE [--preprocess PREPROCESS] [--psm PSM]
>               [--lang LANG]
> 
> optional arguments:
>   -h, --help            show this help message and exit
>   --image IMAGE         path to input image to be OCR'd
>   --preprocess PREPROCESS
>                         thresh: preprocess using threshold method
>                         blur: preprocess using blur method
>   --psm PSM             Page segmentation mode
>   --lang LANG           language
> ```
```YAML
$ python ocr.py --image images/image.jpgsevensegthres.jpg --preprocess thresh --psm 10 --lang ssd
```
> ```YAML
> 0:44
> {'level': [1, 2, 3, 4, 5]
>  'page_num': [1, 1, 1, 1, 1]
>  'block_num': [0, 1, 1, 1, 1]
>  'par_num': [0, 0, 1, 1, 1]
>  'line_num': [0, 0, 0, 1, 1]
>  'word_num': [0, 0, 0, 0, 1]
>  'left': [0, 284, 284, 284, 284]
>  'top': [0, 18, 18, 18, 18]
>  'width': [996, 686, 686, 686, 686]
>  'height': [301, 242, 242, 242, 242]
>  'conf': ['-1', '-1', '-1', '-1', 96]
>  'text': ['', '', '', '', '0:44']}
> ```

## tesseract
```YAML
$ tesseract --help-extra
```
```YAML
Usage:
  tesseract --help | --help-extra | --help-psm | --help-oem | --version
  tesseract --list-langs [--tessdata-dir PATH]
  tesseract --print-parameters [options...] [configfile...]
  tesseract imagename|imagelist|stdin outputbase|stdout [options...] [configfile...]

OCR options:
  --tessdata-dir PATH   Specify the location of tessdata path.
  --user-words PATH     Specify the location of user words file.
  --user-patterns PATH  Specify the location of user patterns file.
  --dpi VALUE           Specify DPI for input image.
  -l LANG[+LANG]        Specify language(s) used for OCR.
  -c VAR=VALUE          Set value for config variables.
                        Multiple -c arguments are allowed.
  --psm NUM             Specify page segmentation mode.
  --oem NUM             Specify OCR Engine mode.
NOTE: These options must occur before any configfile.

Page segmentation modes:
  0    Orientation and script detection (OSD) only.
  1    Automatic page segmentation with OSD.
  2    Automatic page segmentation, but no OSD, or OCR. (not implemented)
  3    Fully automatic page segmentation, but no OSD. (Default)
  4    Assume a single column of text of variable sizes.
  5    Assume a single uniform block of vertically aligned text.
  6    Assume a single uniform block of text.
  7    Treat the image as a single text line.
  8    Treat the image as a single word.
  9    Treat the image as a single word in a circle.
 10    Treat the image as a single character.
 11    Sparse text. Find as much text as possible in no particular order.
 12    Sparse text with OSD.
 13    Raw line. Treat the image as a single text line,
       bypassing hacks that are Tesseract-specific.

OCR Engine modes:
  0    Legacy engine only.
  1    Neural nets LSTM engine only.
  2    Legacy + LSTM engines.
  3    Default, based on what is available.

Single options:
  -h, --help            Show minimal help message.
  --help-extra          Show extra help for advanced users.
  --help-psm            Show page segmentation modes.
  --help-oem            Show OCR Engine modes.
  -v, --version         Show version information.
  --list-langs          List available languages for tesseract engine.
  --print-parameters    Print tesseract parameters.
```
```YAML
$ tesseract images/image.jpgsevensegthres.jpg stdout --tessdata-dir tessdata_best -l ssd --oem 1 --dpi 72 --psm 10
```
```YAML
0:44
````
