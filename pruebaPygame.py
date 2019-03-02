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
    num_user=0
    num_intents=0
    simon.append(random.randint(0,3))
    print("Primera asignacion del simon")

    while not gameExit:
        if turno == "simon":

            print("longitud de simon:",len(simon),"num_simon",num_simon)

            if num_simon == len(simon):
                turno ="user"
                num_intents=0
            else:
                print("Asigno imagen del simon numero:",num_simon)
                print(simon)
                imagen = listImg[simon[num_simon]]
                print(imagen)
                num_simon+=1

        elif turno =="user":
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

                    #si el num_intents es menor que el la cantidad de numeros que hay en el simon
                    if num_intents < (len(simon)):
                        #Valido la el numero con el simon
                        if num_user == simon[num_intents]:
                            print("intento",num_intents,"Good!",num_user," esta bien")
                            # asigno la imagen de la tecla
                            imagen = listImg[num_user]
                            num_intents+=1
                        else:#Si se equivoca, termina el juego
                            print("Fin del juego, perdiste era",simon[num_intents])
                            gameExit=True
                    if num_intents == (len(simon)):#atinó todas, le toca a simon
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
            if turno == "simon":
                time.sleep(3)#Esperate para que alcance a ver el usuario

        pygame.display.flip()#tambien se puede usra .flip() pero es para toda la pantalla
        clock.tick(30)#Frames per second

game_loop()
pygame.quit()
quit()

# while True:
#     for event in pygame.event.get():
#         pygame.quit()
#         sys.exit()
#     pygame.display.update()
