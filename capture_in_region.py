#hacer un capture en una region especifica. Si despues queremos comparar algo que se encuentra en una region especifica

import pyautogui
import time

#region(x,y,ancho,alto)
screenshot = pyautogui.screenshot(region(0,0,500,500))
screenshot.save("screenshot.png")
