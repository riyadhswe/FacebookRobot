import pyautogui
import time
import keyboard
import random


def CommentsTimeline():
    comments = ["SavePalestine ","SaveTheMuslims  ","StopConspiracyAgainstIslam ","GazaUnderAttack ","AlAqsaUnderAttack ","FreePalestine ","StandForPalestine ","StandWithSheikhJarrah ","SaveSheikhJarrahFreedom ","StopTerrorismAgainstMuslims ","AlAqsa ","SaveAqsa ","MasjidAlAqsa "]
    pyautogui.click(x=10, y=908)
    pyautogui.press('f5')
    time.sleep(5)
    number = [1, 2,3,4,5,6,7,8,9,10,11,12,13]

    print("................Timeline Comments................")
    print(".................................................")
    for i in range(9999):
        while keyboard.is_pressed('t') == False:
            time.sleep(1)
            for j in range(9999):
                while keyboard.is_pressed('t') == False:
                    pyautogui.click(x=10, y=908)
                    time.sleep(2)
                    pyautogui.press('j')
                    time.sleep(1)
                    pyautogui.press('c')
                    time.sleep(5)
                    pyautogui.press('#')
                    pyautogui.typewrite(comments[j % random.choice(number)])
                    pyautogui.press('enter')
                    time.sleep(2)
                    pyautogui.click(x=10, y=908)
                    print("...............Timeline Comments", j+1, " Times...............")
                    break

    print("...............Stop...............")





