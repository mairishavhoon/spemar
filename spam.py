#!/bin/python3
import pyautogui, time
m = input("Input Spam Message : ")
i = int(input("Enter spam amount :"))
j = 1
print("Spammer by Rishav started")
time.sleep(15)
while(j<i):
    pyautogui.typewrite(m)
    pyautogui.press("enter")
    j = j+1

print("Spammer by Rishav ended")    
