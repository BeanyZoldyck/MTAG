from time import sleep as s
import keyboard
import clipboard
from guide import file
import pyautogui as pag
peachsocne = file('lex')
textPath = 'lex.txt'
def area(t1, t2):
    return (t1[0],t1[1],t2[0]-t1[0],t2[1]-t1[1])
def capture():
    click=True
    post = pag.screenshot(region=area((1060,151),(1611,888)))
    #if pag.locate(file('at'),post,confidence=.8) or pag.locate(file('hashtag'),post,confidence=.8):
    #    click=False
    if click:
        with open(textPath,'ab') as f:
            for name in pag.locateAll(peachsocne,post,confidence=.9):
                pag.moveTo(name[0]+1060+90+7,name[1]+151+9)
                for _ in range(3):
                    pag.click()
                    s(.15)
                s(.35)
                keyboard.press_and_release('ctrl+c')
                s(.1)
                data=clipboard.paste()
                f.write(data.encode())
                pag.move(0,-100)
            f.close()
            keyboard.press_and_release('right')
            s(2)
            s(.3)
    else:
        keyboard.press_and_release('right')
while 1:
    capture()
    
