import pygame as pg
pg.init()

class Bola:
    def __init__(self, x, y, color = (255,255,255), radio = 10):
        self.posX = x
        self.posY = y
        self.color = color
        self.radio = radio
    
    def pintate(self, pantalla):
        pg.draw.circle(pantalla, self.color, (self.posX,self.posY), self.radio)
    
    def mover(self, ancho, alto):
        movx = 1
        movy = 1
        
        if self.posX == ancho-self.radio or self.posX == 0+self.radio:
            movx * -1
        if self.posY == alto - self.radio or self.posY == 0 + self.radio:
            movy * -1
        self.posX += movx
        self.posY += movy


class Game:
    
    def __init__(self, ancho = 600, alto= 800):
        self.pantalla = pg.display.set_mode((ancho, alto))
        self.bola = Bola(ancho//2, alto//2,(255,255,0))

    def bucle_ppal(self):
        game_over = False

        while not game_over:

            eventos = pg.event.get()
            for evento in eventos:
                if evento.type == pg.QUIT:
                    game_over = True


            self.pantalla.fill((255,0,0))
            self.bola.mover(self.pantalla.get_width(), self.pantalla.get_height())
            self.bola.pintate(self.pantalla)

            pg.display.flip()

    pg.quit()


if __name__ == "__main__":
    pg.init()
    game = Game()
    game.bucle_ppal()