import pyautogui

###### COMO SABER el color del pixel que se encuentra en una coordenada x,y
im = pyautogui.screenshot()
im.getpixel((215,349))


###### QUEREMOS HACER CLICK EN UN LUGAR DINAMICO
#ASI QUE NO PODEMOS HACER LA COMPARACION UNA IMAGEN. TENIENDO EN CUENTA QUE LA SITUACION ES
# QUE CUANDO CARGA CAMBIA DE COLOR

while True:
  screenshot= pyautogui.screenshot()
  #buscamos que color de pixel tiene el capture en la psoicion x,y
  color= screenshot.getpixel((704,323))
  #color que deseamos buscar  (0,71,158)
  if color == (0,71,158):
    #encotramos el color y salimos del while
    break
