import pygame,random,time


pygame.init()

display_width = 800
display_height = 600

black = (0,0,0) #rgb
white = (255,255,255)  #rgb
red = (255,0,0)  #rgb

#aqui simon guarda los valores
simon=[]

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
# Inicializamos variables
turno = "simon"
num_simon=0
num_user
num_intents=0

    while not gameExit:
        if len(simon) == 0:
            simon.append(random.randint(0,3))

        if turno == "simon":
            imagen = listImg[simon[num_simon]]
            if num_simon == len(simon)-1
                turno ="user"
                imagen=None

            else:
                num_simon+=1

        elif turno =="user"
            for event in pygame.event.get():
                if event.type == pygame.QUIT:#la x de la ventana
                    gameExit=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        num_user = 0
                    elif event.key == pygame.K_DOWN:
                        num_user = 1
                    elif event.key == pygame.K_LEFT:
                        num_user = 2
                    elif event.key == pygame.K_RIGHT:
                        num_user = 3
                    # asigno la imagen de la tecla
                    imagen = listImg[num_user]
                    #si el num_intents es menor que el la cantidad de numeros que hay en el simon
                    if num_intents < (len(simon)):
                        #Valido la el numero con el simon
                        if num_user = simon[num_intents]:
                            print("Good!")
                            num_intents+=1
                        else:#Si se equivoca, termina el juego
                            print("Fin del juego, perdiste")
                            gameExit=True
                    else:#atinó todas, le toca a simon
                        turno = "simon"
                        #Agrega un elemento mas para que simon muestre
                        simon.append(random.randint(0,3))
                        #reset el num_simon para que muestre desde 0
                        num_simon=0
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
