
import pygame as pg

pg.init()


pantalla = pg.display.set_mode((600,800) )

game_over = False

x = 300
y = 400
movx = 1
movy = 1
while not game_over:
    eventos = pg.event.get()

    for evento in eventos:
        if evento.type == pg.QUIT:
            game_over = True
        


    # Modificar los objetos del juego
    if x == 590 or x == 10:
        movx *=-1
    if y == 790 or y == 10:
        movy *= -1

    x +=  movx
    y += movy
    # Aquí no hay nada que hacer

    # Refrescar la  pantalla
    pantalla.fill((255,0,0))
    bola = pg.draw.circle(pantalla, (255,255,0), (x,y), 10)


    pg.display.flip()

pg.quit()