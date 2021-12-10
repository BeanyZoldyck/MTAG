import pytesseract
from PIL import ImageGrab
from pyperclip import copy
import pyautogui as pag
from keyboard import press
keyboard.press_and_release('page up')
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\ezeocm7471\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
screencap = ImageGrab.grabclipboard()
text = pytesseract.image_to_string(screencap, lang='eng')
copy(text)
input(text)
region=pag.screenshot(0,0,1920,1080)#change to where name appears
beanzMessages = pag.locateAll('BeanZ.bmp',region)
#next
