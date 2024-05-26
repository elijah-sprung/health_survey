import webbrowser
import pyautogui
import time

webbrowser.open("https://highpoint.co1.qualtrics.com/jfe/form/SV_eL2xGEdY8FWcCG1")

time.sleep(5)

screenWidth, screenHeight = pyautogui.size()

pyautogui.click(100, 500)

pyautogui.press('tab')
pyautogui.write('Elijah', interval = 0.001)

pyautogui.press('tab')
pyautogui.write('Sprung', interval = 0.001)

pyautogui.press('tab')
pyautogui.write('3526152535', interval = 0.001)

pyautogui.press('tab')
pyautogui.write('esprung@highpoint.edu', interval = 0.001)

pyautogui.press('tab')
pyautogui.write('1798719', interval = 0.001)

pyautogui.press('tab')
pyautogui.press('down')
pyautogui.press('up')

pyautogui.press('tab')
pyautogui.press('enter')

time.sleep(2)

pyautogui.moveTo(100, 500)

for i in range(5):
  pyautogui.press('tab')
  pyautogui.press('down')

pyautogui.press('tab')
pyautogui.press('down')
pyautogui.press('up')

pyautogui.press('tab')
pyautogui.press('enter')

time.sleep(2)
pyautogui.hotkey('ctrl', 'w')