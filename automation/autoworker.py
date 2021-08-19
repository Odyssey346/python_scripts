# This is a script to automate an action to make me loads of fake shitcoins on my friend's server
import pyautogui
import time

while True: 
    pyautogui.typewrite('-work')
    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.typewrite("-deposit all")
    pyautogui.press("enter")
    time.sleep(30)
