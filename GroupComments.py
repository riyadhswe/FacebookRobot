import pyautogui
import time
import keyboard
import random


def GroupComments():
    comments = ["Nice", "wow", "joss", "excellent", "superior", "good"]
    time.sleep(5)
    print("................Group Comments................")
    for i in range(9999):
        while keyboard.is_pressed('t') == False:
            time.sleep(1)
            for j in range(9999):
                while keyboard.is_pressed('t') == False:
                    time.sleep(2)
                    pyautogui.press('tab')
                    time.sleep(0.5)
                    pyautogui.press('tab')
                    time.sleep(0.5)
                    pyautogui.press('tab')
                    time.sleep(0.5)
                    pyautogui.press('tab')
                    time.sleep(0.5)
                    pyautogui.press('tab')
                    time.sleep(0.5)
                    pyautogui.press('tab')
                    time.sleep(1)
                    pyautogui.press('c')
                    time.sleep(2)
                    pyautogui.typewrite(comments[j % 6])
                    time.sleep(0.5)
                    pyautogui.press('enter')
                    time.sleep(2)
                    print("...............Group Comments:", j, " Times...............")
                    break
    print("...............Comments Stop...............")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")





