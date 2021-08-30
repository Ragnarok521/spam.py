
import os
import pyautogui
import time


Username = 'Ragnar.521'
Password= 'Ragnarok.404'

U = str(input('\033[1;93mUsername >>> :'))
P = str(input('\033[1;93mPassword >>> :'))

if os.name=='nt':oss="cls"
else:oss="clear"




if U ==Username and P==Password:
    print('\033[1;92mSave')
    while True:
        pyautogui.typewrite('\033[1;91mHacked')
        time.sleep(0.1)
        pyautogui.press('enter')



else:
    print('\033[1;91mNo')


