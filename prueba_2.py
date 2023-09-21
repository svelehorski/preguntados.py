import pygame
from datos import *
from constantes import *

pregunta = ""
posicion = 0
score = 0
pregunta_activa = False
intentos_incorrectos = 0  # Contador de respuestas incorrectas

lista_solo_preguntas = []
lista_opciones_a = []
lista_opciones_b = []
lista_opciones_c = []
lista_respuesta = []

for i in lista:
    lista_solo_preguntas.append(i["pregunta"])
    lista_opciones_a.append(i["a"])
    lista_opciones_b.append(i["b"])
    lista_opciones_c.append(i["c"])
    lista_respuesta.append(i["correcta"])

pygame.init()

#Funcion para personalizar las caracteristicas de Score, y poder pegarlo en la superficie de la pantalla
def dibujar_score(superficie, texto):
    if intentos_incorrectos < 2:
        fuente = pygame.font.SysFont("Trebuchet MS Negrita", 40)
        texto_renderizado = fuente.render(texto, True, COLOR_VERDE)
        text_rect = texto_renderizado.get_rect() #almacena y modifica coordenadas de elementos
        text_rect.midtop = (318, 190)
        superficie.blit(texto_renderizado,text_rect)
    else:
        fuente = pygame.font.SysFont("Trebuchet MS Negrita", 40)
        texto_renderizado = fuente.render(texto, True, COLOR_ROJO)
        text_rect = texto_renderizado.get_rect()
        text_rect.midtop = (318, 190)
        superficie.blit(texto_renderizado,text_rect)

def reiniciar_juego():
    global pregunta_activa, posicion, score, intentos_incorrectos
    pregunta_activa = False
    posicion = 0
    score = 0
    intentos_incorrectos = 0

#defino mi pantalla 
pantalla = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("Preguntados")

#transformo las imagenes
imagen = pygame.image.load("preguntados2.png")
imagen = pygame.transform.scale(imagen, (170,170))
neon = pygame.image.load("neon.png")
neon = pygame.transform.scale(neon, (300,150))
sonido = pygame.image.load("nosound.png")
sonido = pygame.transform.scale(sonido, (50, 50))

#Defino mi texto
fuente = pygame.font.SysFont("Trebuchet MS Negrita", 30)
font = pygame.font.SysFont("Trebuchet MS Negrita", 25)
item_uno = fuente.render(str("PREGUNTA"), True, BLACK)
item_dos = fuente.render(str("REINTENTAR"), True, BLACK)
item_score = fuente.render(str("SCORE"), True, BLACK)

#musica de fondo
pygame.mixer.music.load('SuperMario.ogg')
pygame.mixer.music.play(-1) #utilizo -1 para reproducir la musica en bucle infinito 
pygame.mixer.music.set_volume(0.5) #el volumen determinado con el que voy a inicializar el juego


#bucle del juego
flag_ejecutar = True

while flag_ejecutar:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_ejecutar = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_click = list(evento.pos)
            #print(posicion_click)

            #para sumar una posicion siempre que el usuario haga click en "pregunta"
            if (posicion_click[0] > 300 and posicion_click[0] < 500) and (posicion_click[1] > 20 and posicion_click[1] < 120):
                if posicion < len(lista_solo_preguntas) and intentos_incorrectos < 2:
                    texto_pregunta = fuente.render(str(lista_solo_preguntas[posicion]), True, BLACK)
                    opcion_a = font.render(str(lista_opciones_a[posicion]), True, BLACK)
                    opcion_b = font.render(str(lista_opciones_b[posicion]), True, BLACK)
                    opcion_c = font.render(str(lista_opciones_c[posicion]), True, BLACK)
                    pregunta_activa = True

            if pregunta_activa:
                # Verificar clic en opción A
                if (posicion_click[0] > 55 and posicion_click[0] < 245) and (posicion_click[1] > 370 and posicion_click[1] < 445):
                    if lista_respuesta[posicion] == "a":
                        score += 10
                        posicion += 1
                        intentos_incorrectos = 0
                        pregunta_activa = False
                    else:
                        intentos_incorrectos += 1
                        if intentos_incorrectos == 2:
                            pregunta_activa = False

                # Verificar clic en opción B
                elif (posicion_click[0] > 295 and posicion_click[0] < 484) and (posicion_click[1] > 370 and posicion_click[1] < 445):
                    if lista_respuesta[posicion] == "b":
                        score += 10
                        posicion += 1
                        intentos_incorrectos = 0
                        pregunta_activa = False
                    else:
                        intentos_incorrectos += 1
                        if intentos_incorrectos == 2:
                            pregunta_activa = False

                # Verificar clic en opción C
                elif (posicion_click[0] > 540 and posicion_click[0] < 730) and (posicion_click[1] > 370 and posicion_click[1] < 445):
                    if lista_respuesta[posicion] == "c":
                        score += 10
                        posicion += 1
                        intentos_incorrectos = 0
                        pregunta_activa = False
                    else:
                        intentos_incorrectos += 1
                        if intentos_incorrectos == 2:
                            pregunta_activa = False

            #para reiniciar la posicion en el juego
            if (posicion_click[0] > 300 and posicion_click[0] < 500) and (posicion_click[1] > 469 and posicion_click[1] < 567):
                reiniciar_juego()

            #para mutear el sonido
            if (posicion_click[0] > 740 and posicion_click[0] < 780) and (posicion_click[1] > 30 and posicion_click[1] < 70):
                pygame.mixer.music.set_volume(0.0)

    pantalla.fill(COLOR_BLANCO)
    pygame.draw.rect(pantalla, COLOR_AMARILLO, (300, 20, 200, 100))
    pygame.draw.rect(pantalla, COLOR_AMARILLO, (301, 471, 200, 100))

    #marcador de puntos
    dibujar_score(pantalla, str(score))
    #imagen preguntados
    pantalla.blit(imagen, (4 , 5))
    #sonido
    pantalla.blit(sonido, (740, 30))

    if pregunta_activa:
        pantalla.blit(neon,(NEON_A))
        pantalla.blit(neon,(NEON_B))
        pantalla.blit(neon,(NEON_C))
        pantalla.blit(texto_pregunta, (50,290))
        pantalla.blit(opcion_a, (80,395))
        pantalla.blit(opcion_b, (335,395))
        pantalla.blit(opcion_c, (570,395))

    if intentos_incorrectos == 2:
        item_reiniciar = fuente.render(str("GAME OVER"), True, COLOR_ROJO)
        pantalla.blit(item_reiniciar, (289,303))


    if len(lista_solo_preguntas) - 1 < posicion:
        item_win = fuente.render(str("¡YOU WIN, CONGRATULATIONS!"), True, COLOR_VERDE)
        pantalla.blit(item_win, (230,303))

    pantalla.blit(item_uno, (340, 54))
    pantalla.blit(item_dos, (329, 505))
    pantalla.blit(item_score, (294, 153))
    pygame.display.flip()

pygame.quit()
