import pyautogui
import time
import keyboard
import random


def hahareact():
    number = [3]
    pyautogui.click(x=10, y=908)
    pyautogui.press('f5')
    time.sleep(5)

    print("................Timeline react................")
    for i in range(9999):
        while keyboard.is_pressed('t') == False:
            time.sleep(2)
            pyautogui.press('j')
            time.sleep(1)
            pyautogui.press('l')
            time.sleep(1)
            print("...............Timeline react", i + 1, " Times...............")
            for i in range(random.choice(number)):
                pyautogui.press('right')
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.click(x=10, y=908)

            break



    print("...............React Stop...............")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")





