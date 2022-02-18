import random
import pygame as pg
pg.init()
class Rock():
    def __init__(self, padre, x, y):
        self.padre = padre
        self.altura = 20
        self.anchura = 100
        self.x = x
        self.y = y
        self.color = (0,0,0)

    def dibujar(self):
        pg.draw.rect(self.padre,self.color, (self.x, self.y, self.anchura, self.altura) )

    def romper(self):
        pass


class Player():
    def __init__(self, padre):
        self.padre = padre
        self.altura = 20
        self.anchura = 100
        self.posX =self.padre.get_width()//2 -50
        self.posY = self.padre.get_height()- 50
        self.color = (255,255,255)
    def dibujar(self):
        pg.draw.rect(self.padre, self.color, (self.posX, self.posY, self.anchura, self.altura))

    def mover(self, evento):
        if evento.type == pg.KEYDOWN:
            if evento.key == pg.K_RIGHT:
                self.posX +=2

            if evento.key == pg.K_LEFT:
                self.posX -= 2


class Bola:
    def __init__(self, padre, player, x, y, color = (255,255,255), radio = 10):
        self.padre = padre
        self.player = player
        self.posX = x
        self.posY = y
        self.color = color
        self.radio = radio
        self.vx = 2
        self.vy = 2
    
    def dibujar(self):
        pg.draw.circle(self.padre, self.color, (self.posX,self.posY), self.radio)
    
    def mover(self):
        self.posX += self.vx
        self.posY += self.vy

        if self.posX >= self.padre.get_width() - self.radio or self.posX <= self.radio :
            self.vx *= -1
        if self.posY >= self.padre.get_height() - self.radio or self.posY <= self.radio:
            self.vy *= -1
        if self.posY == self.player.posY and self.player.posX<=self.posX <=(self.player.posX+self.player.anchura):
            self.vy *= -1



class Game:
    colors = {
        1: (0,102,204),
        2: (102,204,0),
        3: (204,0,204),
        4: (0,0,204),
        5: (255,128,0),
        6: (0,255,255)
    }
    bolas = []
    def __init__(self, ancho = 600, alto= 800):
        self.pantalla = pg.display.set_mode((ancho, alto))
        self.player = Player(self.pantalla)
        self.bola = Bola(self.pantalla,self.player, ancho//2, alto//2,(255,255,0))
        for i in range(10):
            x = random.randint(0,ancho)
            y = random.randint(0,alto)
            color = self.colors[random.randint(1,6)]
            self.bolas.append(Bola(self.pantalla, self.player, x, y, color))

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
            self.player.dibujar()
            self.player.mover(evento)

            for i in range(10):
                self.bolas[i].dibujar()
                self.bolas[i].mover()


            pg.display.flip()

    pg.quit()


if __name__ == "__main__":
    pg.init()
    game = Game()
    game.bucle_ppal()