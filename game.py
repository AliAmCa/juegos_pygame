
import pygame as pg
pg.init()

class Vigneta:
    def __init__(self, padre, x,y, ancho, alto, color = (255,255,255)):
        self.padre = padre
        self.x = x
        self.y = y
        self.alto = alto
        self.ancho = ancho
        self.color = color
        self.vx = 0
        self.vy = 0

    def dibujar(self):
        pass
    def mover(self):
        pass

class Rock(Vigneta):
    
    def dibujar(self):
        pg.draw.rect(self.padre,self.color, (self.x, self.y, self.ancho, self.alto) )

    def desaparecer(self):
            self.color =(255,0,0)


class Player(Vigneta):
    def __init__(self, padre, x,y, ancho = 100, alto = 20, color = (255,255,255)):
        super().__init__(padre, x,y, ancho, alto, color)
        self.vx = 5
        
    def dibujar(self):
        pg.draw.rect(self.padre, self.color, (self.x, self.y, self.ancho, self.alto))

    def mover(self):
        teclas = pg.key.get_pressed()

        if teclas[pg.K_LEFT]:
           self.x -= self.vx

        if teclas[pg.K_RIGHT]:
            self.x += self.vx
        if self.x <= 0:
            self.x = 0
        if self.x +self.ancho >= self.padre.get_width():
            self.x = self.padre.get_width() - self.ancho

class Bola:
    def __init__(self, padre, x, y, color = (255,255,255), radio = 10):
        self.padre = padre
        
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
        

    def compruebaChoque(self, otro):
        if (self.posX - self.radio in range(otro.x, otro.x +  otro.ancho) or \
            self.posX + self.radio in range(otro.x, otro.x +  otro.ancho)) and \
            (self.posY - self.radio in range(otro.y, otro.y + otro.alto) or \
            self.posY + self.radio in range(otro.y, otro.y + otro.alto)):
                self.vy *= -1


class Game:
    
    rocas = []
    def __init__(self, ancho = 600, alto= 800):
        self.pantalla = pg.display.set_mode((ancho, alto))
        self.player = Player(self.pantalla, ancho//2, alto-30)
        self.bola = Bola(self.pantalla, ancho//2, alto//2,(255,255,0))
        for i in range(4):
            self.rocas.append(Rock(self.pantalla, 40 + 140*i, 20 , 100, 20))

    def bucle_ppal(self):
        game_over = False

        while not game_over:

            eventos = pg.event.get()
            for evento in eventos:
                if evento.type == pg.QUIT:
                    game_over = True


            self.pantalla.fill((255,0,0))
            for roca in self.rocas:
                roca.dibujar()
                if self.bola.posY == roca.y + roca.alto:
                    if roca.x<= self.bola.posX<= roca.x + roca.ancho:
                        roca.desaparecer()

            self.bola.mover()
            self.bola.dibujar()
            self.bola.compruebaChoque(self.player)
            self.player.dibujar()
            self.player.mover()

            


            pg.display.flip()

    pg.quit()


if __name__ == "__main__":
    pg.init()
    game = Game()
    game.bucle_ppal()