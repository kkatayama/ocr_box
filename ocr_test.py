# coding: utf-8
from ocr_basic import pass_image
from ocr import process_image
import pandas as pd
import subprocess
import shlex
import os

images = os.listdir('images')
if '.DS_Store' in images:
    images.remove('.DS_Store')

for image in images:
    image_name = os.path.splitext(image)[0].replace('.', '_') + '.csv'

    df = pd.DataFrame(columns=['tool','filter','psm','ocr_text','predicted_text','confidence_score'])
    
    print('\vtesseract cli...\n', '#'*40)
    for i in [x for x in range(1,14) if x != 2]:
        cmd = 'tesseract images/' + image + ' stdout --tessdata-dir "tessdata_best" -l eng --oem 1 --dpi 72 --psm ' + str(i)
        args = shlex.split(cmd)
        proc = subprocess.run(args, stdout=subprocess.PIPE, universal_newlines=True)
        text = proc.stdout
        print(text)
        print('#'*40)
        df = df.append({'tool': 'tesseract_cli', 'filter': 'NA', 'psm': str(i), 'ocr_text': text, 'predicted_text': 'NA', 'confidence_score': 'NA'}, ignore_index=True)
        
    print('\nocr_basic...\n', '#'*40)
    for i in [x for x in range(1,14) if x != 2]:
        text, data = pass_image('images/' + image, str(i))
        d = '{' + '\n'.join(str(' '+repr(k) + ': ' + str(v)) for k,v in data.items()).strip() + '}'
        print(text['text'])
        print(d)
        print('#'*40)
        word = '\n'.join(word for word in data['text'] if word != '').splitlines()
        conf = '\n'.join(str(conf) for conf in data['conf'] if conf != '-1').splitlines()
        df = df.append({'tool': 'ocr_basic.py', 'filter': 'NA', 'psm': str(i), 'ocr_text': text['text'], 'predicted_text': word, 'confidence_score': conf}, ignore_index=True)
    
    print('\nocr_processed_thresh...\n', '#'*40)
    for i in [x for x in range(1,14) if x != 2]:
        text, data = process_image(image_file='images/' + image, process_type='thresh', psm_value=str(i))
        d = '{' + '\n'.join(str(' '+repr(k) + ': ' + str(v)) for k,v in data.items()).strip() + '}'
        print(text['text'])
        print(d)
        print('#'*40)
        word = '\n'.join(word for word in data['text'] if word != '').splitlines()
        conf = '\n'.join(str(conf) for conf in data['conf'] if conf != '-1').splitlines()
        df = df.append({'tool': 'ocr.py', 'filter': 'thresh', 'psm': str(i), 'ocr_text': text['text'], 'predicted_text': word, 'confidence_score': conf}, ignore_index=True)
    
    print('\nocr_processed_blur...\n', '#'*40)
    for i in [x for x in range(1,14) if x != 2]:
        text, data = process_image(image_file='images/' + image, process_type='blur', psm_value=str(i))
        d = '{' + '\n'.join(str(' '+repr(k) + ': ' + str(v)) for k,v in data.items()).strip() + '}'
        print(text['text'])
        print(d)
        print('#'*40)
        word = '\n'.join(word for word in data['text'] if word != '').splitlines()
        conf = '\n'.join(str(conf) for conf in data['conf'] if conf != '-1').splitlines()
        df = df.append({'tool': 'ocr.py', 'filter': 'blur', 'psm': str(i), 'ocr_text': text['text'], 'predicted_text': word, 'confidence_score': conf}, ignore_index=True)
     
    df.to_csv('results/' + image_name)
