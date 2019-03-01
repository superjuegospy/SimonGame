import pygame,random,time


pygame.init()

display_width = 800
display_height = 600

black = (0,0,0) #rgb
white = (255,255,255)  #rgb
red = (255,0,0)  #rgb

patron = []
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Simon!')
clock = pygame.time.Clock()

listImg=[]
listImg.append( pygame.image.load('flechaUp.png')) #Solo vamos a cargar la imagen
listImg.append( pygame.image.load('flechaDown.png')) #Solo vamos a cargar la imagen
listImg.append( pygame.image.load('flechaLeft.png') )#Solo vamos a cargar la imagen
listImg.append( pygame.image.load('flechaRight.png')) #Solo vamos a cargar la imagen
def mostrar(imagenObj,x,y):
    """ Mostrar una imagen a partir de coordenadas """
    gameDisplay.blit(imagenObj,(x,y))
def game_loop():
    """ Realiza el loop del juego"""
    imagen = None
    gameExit=False

    while not gameExit:
        if len(patron) == 0:
            patron.append(random.randint(0,3))

        # for num in patron:
        #     imagen = listImg[num]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#la x de la ventana
                gameExit=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    imagen = listImg[2]
                elif event.key == pygame.K_UP:
                    imagen = listImg[0]
                elif event.key == pygame.K_RIGHT:
                    imagen = listImg[3]
                elif event.key == pygame.K_DOWN:
                    imagen = listImg[1]

            print(event)


        gameDisplay.fill(white)#importa orden en que pintas
        if imagen is not None:
            #Mostramos la flechaa adecuada
            mostrar(imagen,display_width*0.4,display_height*0.2)

        pygame.display.update()#tambien se puede usra .flip() pero es para toda la pantalla
        clock.tick(30)#Frames per second

game_loop()
pygame.quit()
quit()

# while True:
#     for event in pygame.event.get():
#         pygame.quit()
#         sys.exit()
#     pygame.display.update()
