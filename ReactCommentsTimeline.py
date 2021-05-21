import pyautogui
import time
import keyboard
import random


def ReactCommentsTimeline():
    number = [1, 2, 4]
    pyautogui.click(x=10, y=908)
    pyautogui.press('f5')
    time.sleep(5)
    comments = ["amazing", "awesome", "believe", "brave", "classic", "constant", "cool", "courageous", "excellent", "good"]

    print("................Timeline react................")
    for i in range(9999):
        while keyboard.is_pressed('t') == False:
            time.sleep(2)
            pyautogui.press('j')
            time.sleep(1)
            pyautogui.press('l')
            time.sleep(1)
            print("...............Timeline react", i + 1, " Times...............")
            for j in range(random.choice(number)):
                pyautogui.press('right')
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.press('c')
            pyautogui.typewrite(comments[i%10])
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.click(x=10, y=908)
            break
    print("...............React Stop...............")






