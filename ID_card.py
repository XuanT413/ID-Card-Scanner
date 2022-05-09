## ID card Capture Program
import os
import sys
import PySimpleGUI as sg
import numpy as np
from PIL import Image, ImageEnhance
from Webcam_capture import WebCamCap as WCC
import time as time

import pytesseract
pytesseract.pytesseract.tesseract_cmd = os.path.join( r'C:\Program Files\Tesseract-OCR\tesseract.exe')


def img_Enhance(file):
    ImageEnhance.Contrast(file).enhance(5)
    ImageEnhance.Sharpness(file).enhance(5)

def capture_img():
    cap = WCC()
    cap.res_1080p()
    cap.Capture()
    return cap.get_name(), cap

def img2str(img):
#   Create an event loop
    identif = Image.open(img)    
    identif = identif.convert('RGB')
    img_Enhance(identif)
    
    pix = identif.load()
    for y in range(identif.size[1]):
        for x in range(identif.size[0]):
            if pix[x, y][0] <= 164 or pix[x, y][1] <= 164 or pix[x, y][2] <= 164:                pix[x, y] = (0, 0, 0)
            else:
                pix[x, y] = (255, 255, 255)

    img_name = 'temp{}.png'.format(time.ctime().replace(':', '_'))
    identif.resize((640, 360), Image.LANCZOS).save(img_name)
    info = pytesseract.image_to_string(Image.open(img_name))

    return info, img_name


def separate_win(imag):
##    menu = ['&Right', ['Right', '!&Click', '&Menu', 'E&xit', 'Properties']]
    layout = [[sg.Text('IDENTIFICATION CARD CAPTURE', size=(30, 2), text_color='RED')],
              [sg.Image(imag, key='-ONSCR-')],
              [sg.Output(size=(60,10))],
              [sg.Button('PRINT')], [sg.Button('CAPTURE')], [sg.Button('EXIT')]]
    window = sg.Window('ID Capture', layout, margins=(10, 10)) # Create the window
    return window

def create_file():
    return None

def delete(name_list):
    for i in name_list:
        os.remove(os.path.join(os.getcwd(), i))

def clean_up(cam_obj, file_list):
    cam_obj.cam.release()
    delete(file_list)

##def extract(image):
    

def main():
    initial_img = 'temp.png'
    file_names = np.array([])
    info = "There's nothing to print yet."
    camera = None
    new_win = separate_win(initial_img)
    while True:
        event, values = new_win.read()
        if event == 'PRINT':
            print(info)
        elif event == 'CAPTURE':
            try:
                photo, camera = capture_img()
                info, img_name = img2str(photo)
                info = info.split('\n')
                file_names = np.append(file_names, [img_name, photo])
                new_win['-ONSCR-'].update(img_name)
            except:
                print("Unexpected error:", sys.exc_info())       
        else: 
            break
        
    new_win.close(); del new_win
    if camera!= None:
        clean_up(camera, file_names)


main()
