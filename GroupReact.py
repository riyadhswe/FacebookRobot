import pyautogui
import time
import keyboard
import random


def GroupReact():
    number = [1, 2, 4]
    time.sleep(5)
    print("................Group React................")
    for i in range(9999):
        while keyboard.is_pressed('t') == False:
            time.sleep(1)
            for j in range(9999):
                while keyboard.is_pressed('t') == False:
                    time.sleep(1)
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    time.sleep(1)
                    pyautogui.press('l')
                    time.sleep(1)
                    print("...............GroupReact :", j+1, " Times...............")
                    for i in range(random.choice(number)):
                        pyautogui.press('right')
                    time.sleep(1)
                    pyautogui.press('enter')
                    time.sleep(1)
                    pyautogui.press('c')
                    time.sleep(1)
                    break

    print("...............React Stop...............")





