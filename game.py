import pygame as pg
pg.init()

class Bola:
    def __init__(self, padre, x, y, color = (255,255,255), radio = 10):
        self.padre = padre
        self.posX = x
        self.posY = y
        self.color = color
        self.radio = radio
        self.vx = 1
        self.vy = 1
    
    def dibujar(self):
        pg.draw.circle(self.padre, self.color, (self.posX,self.posY), self.radio)
    
    def mover(self):
        self.posX += self.vx
        self.posY += self.vy

        if self.posX >= self.padre.get_width() - self.radio or self.posX <= self.radio:
            self.vx *= -1
        if self.posY >= self.padre.get_height() - self.radio or self.posY <= self.radio:
            self.vy *= -1
        

class Game:
    
    def __init__(self, ancho = 600, alto= 800):
        self.pantalla = pg.display.set_mode((ancho, alto))
        self.bola = Bola(self.pantalla,ancho//2, alto//2,(255,255,0))

    def bucle_ppal(self):
        game_over = False

        while not game_over:

            eventos = pg.event.get()
            for evento in eventos:
                if evento.type == pg.QUIT:
                    game_over = True


            self.pantalla.fill((255,0,0))
            self.bola.mover()
            self.bola.dibujar()

            pg.display.flip()

    pg.quit()


if __name__ == "__main__":
    pg.init()
    game = Game()
    game.bucle_ppal()