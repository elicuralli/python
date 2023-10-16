import pyautogui,time

"""time.sleep(5)
var = open("archivo.txt","r")
for linea in carlos:
    pyautogui.typewrite(linea)
    pyautogui.press('enter')
"""
time.sleep(5)

for i in range(50):
    pyautogui.typewrite("hola")
    pyautogui.press('enter')
