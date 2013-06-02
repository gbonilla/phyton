import pygame , os 
from pygame import time as pytime  
from pygame.locals import*  
      
# Inicializamos
pygame.mixer.init()  
# Cargamos la cancion  
pygame.mixer.music.load(os.path.join('D:\gbackup\Respaldo\Musik\Mana\\ana.mp3'))  
# Le damos al Play  
pygame.mixer.music.play()  
# Esperamos un tiempo a que acabe la cancion  
#pytime.wait(110000)  
# Salimos del programa  
exit(0)  


