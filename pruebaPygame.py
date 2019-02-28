import pygame, sys
from pygame.locals import *

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0) #rgb
white = (255,255,255)  #rgb
red = (255,0,0)  #rgb

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Simon!')
clock = pygame.time.Clock()

flechaUp = pygame.image.load('flechaUp.png') #Solo vamos a cargar la imagen
flechaDown = pygame.image.load('flechaDown.png') #Solo vamos a cargar la imagen
flechaLeft = pygame.image.load('flechaLeft.png') #Solo vamos a cargar la imagen
flechaRight = pygame.image.load('flechaRight.png') #Solo vamos a cargar la imagen

def mostrar(imagenObj,x,y):
    """ Mostrar una imagen a partir de coordenadas """
    gameDisplay.blit(imagenObj,(x,y))

crash=False

while not crash:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#la x de la ventana
            crash=True
        print(event)

    gameDisplay.fill(white)#importa orden en que pintas
    mostrar(flechaUp,display_width*0.4,display_height*0.2)#Mostramos la flecha up

    pygame.display.update()#tambien se puede usra .flip() pero es para toda la pantalla
    clock.tick(60)#Frames per second
pygame.quit()
quit()

# while True:
#     for event in pygame.event.get():
#         pygame.quit()
#         sys.exit()
#     pygame.display.update()
