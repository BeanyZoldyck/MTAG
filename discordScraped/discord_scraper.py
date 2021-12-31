import mouse as m
from time import sleep as s
import keyboard
import clipboard
textPath = 'data.txt'
beanPath = 'BeanZ.txt'
def capture():
    
    """
    scrape BeanZ's messages then go next
    """
    topPageLeftCorner = (882,179)#(1329,266)
    dragAt = (1150, 719)
    nextButton = (1209, 648)
    m.move(topPageLeftCorner[0], topPageLeftCorner[1])
    s(1)
    m.press()
    s(.5)
    m.move(dragAt[0],dragAt[1],duration=1.2)
    s(2.5)
    m.move(nextButton[0],nextButton[1],duration=.5)
    m.release()
    s(.5)
    keyboard.press_and_release('ctrl+c')
    s(.01)
    data=clipboard.paste()
    m.click()
    s(3)
    with open(textPath,'wb') as f:
        f.write(data.encode())
        f.close()
def clean():
    user = b'WINGU INTJ Sigma Lifter yb stan'
    tempList =[]
    index = 0
    endIndex=0
    wrongIndices=[]
    with open(textPath,'rb') as f:
        textList = f.readlines()
        for line in textList:
            if user in line or b'GIF' in line or b'Image' in line:
                continue
            elif b'//twitter.com/' in line:
                endIndex = index+10
            elif b'parsec.gg/' in line:
                endIndex = index+4
                pass
            if index > endIndex:
                tempList.append(line)
            
            index+=1
        f.close()
    tempList=list(map(lambda x: x.replace(b'\r\n',b'')+b'\n',tempList))
    with open(beanPath,'ab') as q:
        q.writelines(tempList)
        q.close()
for i in range(26):
    capture()
    clean()

