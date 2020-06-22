import pyautogui

###### COMO SABER el color del pixel que se encuentra en una coordenada x,y
im = pyautogui.screenshot()
im.getpixel((215,349))
