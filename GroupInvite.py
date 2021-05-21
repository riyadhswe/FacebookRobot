import pyautogui
import time
import keyboard

def GroupInvite():
    time.sleep(5)
    print("................Invite Group................")
    for i in range(9999):
        while keyboard.is_pressed('t') == False:
            pyautogui.press('tab')
            time.sleep(0.2)
            pyautogui.press('enter')
            pyautogui.press('down')
            pyautogui.press('down')
            pyautogui.press('down')
            pyautogui.press('down')
            pyautogui.press('down')
            pyautogui.press('down')
            pyautogui.press('down')
            pyautogui.press('down')
            pyautogui.press('down')
            pyautogui.press('down')
            print("...............Invite :",i+2," Times...............")
            time.sleep(1)
            break
    print("...............Invite Stop...............")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")





