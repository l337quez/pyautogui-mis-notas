#si necesitas encontrar un pixel de un screenshot este script te va funcionar
import os, sys, time
import pyautogui
from PIL import Image, ImageDraw


#retardo  4 segundos
time.sleep(4)

ruta= os.getcwd()

# Capturar pantalla en una region delimitada (x,y,height,width).
screenshot = pyautogui.screenshot(region=(675,270, 155, 90))
# Guardar imagen.
screenshot.save(ruta + "\\check load\\screenshot.png")
#ruta de la imagen
screenshot_ruta= ruta + "\\check load\\screenshot.png"

#obtenemos el ancho y el alto
img=Image.open(screenshot_ruta)

# Devuelve una tupla con la anchura y altura de la imagen
width,height=img.size
print(height)
print(width)

#cargamos la imagen
img = img.load()

ban= False
i = 0
while i<height and ban==False:
    j = 0
    while j<width and ban==False:
        print(img[j,i])
        # si encuentra el color RGB sale
        if (img[j,i] == (0, 71, 158)) == True:
            print("Ha encontrado el Pixel (0, 71, 158) ")
            ban= True # obliga a salir de los bucles
            break
            
        j = j+1
    i = i+1
