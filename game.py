
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

    @property
    def xcentro(self):
        return self.x + self.ancho//2
    @property
    def ycentro(self):
        return self.y + self.alto//2

    def dibujar(self):
        pass
    def mover(self):
        pass

    def intersecta(self, otro) -> bool:
        return (self.x  in range(otro.x, otro.x +  otro.ancho) or \
                self.x + self.ancho in range(otro.x, otro.x +  otro.ancho)) and \
                (self.y  in range(otro.y, otro.y + otro.alto) or \
                self.y + self.alto in range(otro.y, otro.y + otro.alto))
                
 
class Rock(Vigneta):
    def __init__(self,padre, x, y, ancho, alto,color = (0,0,0)):
        super().__init__(padre, x, y, ancho, alto,color)
        

    def dibujar(self):
       
        pg.draw.rect(self.padre,self.color, (self.x, self.y, self.ancho, self.alto) )
    '''
    def desaparecer(self):
            self.color =(255,0,0)
            self.x= 0-self.ancho
            self.y= 0-self.alto
    '''
    def comprobarToque(self, bola):
        if self.intersecta(bola):
            bola.vy *=-1
            return True
        return False

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

class Bola(Vigneta):
    def __init__(self, padre, x, y, color = (255,255,255), radio = 10):
        super().__init__(padre, x-radio, y-radio, 2*radio, 2*radio, color)
        self.radio = radio
        self.vx = 3
        self.vy = 3
        self.xinit = x
        self.yinit = y
        self.esta_viva = True
    
    def dibujar(self):
        pg.draw.circle(self.padre, self.color, (self.xcentro, self.ycentro), self.radio)
    
    def mover(self):
        self.x += self.vx
        self.y += self.vy

        if self.x >= self.padre.get_width() - self.ancho or self.x <= 0:
            self.vx *= -1
        if self.y <= 0:
            self.vy *= -1
        if self.y >= self.padre.get_height() - self.alto:
            self.esta_viva = False
            
    def reset(self):
        self.x = self.xinit
        self.y = self.yinit
        self.esta_viva = True
        
    def compruebaChoque(self, otro):
        if self.intersecta(otro):
            self.vy *= -1
            #    if isinstance(otro,Rock):
             #       otro.desaparecer()


class Game:
    
    
    def __init__(self, ancho = 600, alto= 800):
        self.pantalla = pg.display.set_mode((ancho, alto))
        self.player = Player(self.pantalla, ancho//2, alto-30)
        self.bola = Bola(self.pantalla, ancho//2, alto//2,(255,255,0))
        self.rocas = []
        self.creaRocas()
        self.contador_vidas = 3
        self.reloj = pg.time.Clock()

    def creaRocas(self):
        for i in range(10):
            for j in range(4):
                self.rocas.append(Rock(self.pantalla, 5 + 60*i, 35 + 30*j , 50, 20))

    def bucle_ppal(self):
        game_over = False

        while self.contador_vidas > 0 and not game_over:
            self.reloj.tick(60)

            eventos = pg.event.get()
            for evento in eventos:
                if evento.type == pg.QUIT:
                    game_over = True


            self.pantalla.fill((255,0,0))
            for roca in self.rocas:
                if roca.comprobarToque(self.bola):
                    self.rocas.remove(roca)
                roca.dibujar()
                

            self.bola.mover()
            self.player.mover()
            self.bola.compruebaChoque(self.player)

            if not self.bola.esta_viva:
                self.contador_vidas -= 1
                self.bola.reset()

            self.bola.dibujar()
            self.player.dibujar()
            

            


            pg.display.flip()

    pg.quit()


if __name__ == "__main__":
    pg.init()
    game = Game()
    game.bucle_ppal()