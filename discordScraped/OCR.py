import pytesseract
from PIL import ImageGrab
from pyperclip import copy
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\ezeocm7471\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
screencap = ImageGrab.grabclipboard()
text = pytesseract.image_to_string(screencap, lang='eng')
copy(text)
input(text)
