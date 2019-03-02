import pygame,random,time


pygame.init()

display_width = 900
display_height = 600

black = (50,50,50) #rgb
white = (240,240,240)  #rgb
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
Good = pygame.image.load('good.png')
bien = pygame.image.load('like.png')

def mostrar(imagenObj,x,y):
    """ Mostrar una imagen a partir de coordenadas """
    gameDisplay.blit(imagenObj,(x,y))

def text_objects(text,font):
    textSurface = font.render(text,True,black)
    return textSurface, textSurface.get_rect()

def message_display(text,centerX,centerY):
    largeText = pygame.font.SysFont('showcardgothic',80)
    textSurface, textRect = text_objects(text,largeText)
    textRect.center = ((centerX,centerY))
    gameDisplay.blit(textSurface,textRect)

    pygame.display.update()
    time.sleep(1)

def game_loop():
    """ Realiza el loop del juego"""

    # Inicializamos variables
    imagen = None
    gameExit=False
    turno = "simon"
    num_simon=0
    num_user=0
    num_intents=0
    simon.append(random.randint(0,3))

    while not gameExit:
        if turno == "simon":
            # message_display("Turno de Simon",display_width/2,display_height*0.1)

            if num_simon == len(simon):
                turno ="user"
                num_intents=0
                imagen=None
            else:
                imagen = listImg[simon[num_simon]]
                num_simon+=1

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

                if turno =="user":
                    #si el num_intents es menor que el la cantidad de numeros que hay en el simon
                    if num_intents < (len(simon)):
                        #Valido la el numero con el simon
                        if num_user == simon[num_intents]:
                            # asigno la imagen de la tecla
                            imagen = listImg[num_user]
                            num_intents+=1
                        else:#Si se equivoca, termina el juego
                            message_display("Perdiste!",display_width/2,display_height*.7)
                            gameExit=True
                            imagen = None
                    if num_intents == (len(simon)):#atinó todas, le toca a simon
                        turno = "simon"
                        #Agrega un elemento mas para que simon muestre
                        simon.append(random.randint(0,3))
                        #reset el num_simon para que muestre desde 0
                        num_simon=0


        gameDisplay.fill(white)
        #importa orden en que pintas

        if imagen is not None:

            if turno == "simon" and num_simon == 1:
                time.sleep(2)

            mostrar(imagen,display_width*0.4,display_height*0.2)

            if turno == "simon" and num_simon > 0:
                message_display("Turno ["+str(num_simon)+"] de Simon",display_width/2,display_height*.1)
                time.sleep(1)#Esperate para que alcance a ver el usuario

            if turno == "user" and num_intents > 0 and num_simon is not 0:
                mostrar(bien,display_width*.35,display_height*0.55 )
                message_display(" Turno ["+str(num_intents)+"]",display_width/2,display_height*.1)

        if turno == "user" and num_intents == 0:
            message_display("Tu turno",display_width/2,display_height*0.1)
        elif turno == "simon" and num_simon ==0:
            message_display(" Turno ["+str(num_intents)+"]",display_width/2,display_height*.1)
            mostrar(Good,display_width*.25,display_height*0.2)

        pygame.display.update()#tambien se puede usar .flip() pero es para toda la pantalla
        clock.tick(30)#Frames per second

game_loop()

pygame.quit()
quit()
