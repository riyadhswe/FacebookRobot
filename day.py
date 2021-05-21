import pyautogui
import time
import keyboard

def ReactDay():
    time.sleep(5)
    print("................Timeline react................")
    for i in range(9999):
        while keyboard.is_pressed('t') == False:
            pyautogui.click(x=534, y=991)
            time.sleep(2)
            pyautogui.click(x=780, y=555)
            print("...............Timeline Comments", i + 1, " Times...............")
            break