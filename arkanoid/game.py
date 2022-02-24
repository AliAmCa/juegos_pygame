
import pygame as pg
from arkanoid.entities import Bola, Rock, Player
from arkanoid import niveles, FPS
pg.init()


class Game:
    
    
    def __init__(self, ancho = 600, alto= 800):
        self.pantalla = pg.display.set_mode((ancho, alto))
        self.player = Player(self.pantalla, ancho//2, alto-30)
        self.bola = Bola(self.pantalla, ancho//2, alto//2,(255,255,0))
        self.rocas = []
        
        self.contador_vidas = 3
        self.reloj = pg.time.Clock()
        self.puntos = 0

    def creaRocas(self, nivel):
        for col, fil in niveles[nivel]:
            self.rocas.append(Rock(self.pantalla, 5 + 60*col, 25 + 30*fil , 50, 20))

        '''
            for i in range(10):
                for j in range(4):
                    self.rocas.append(Rock(self.pantalla, 5 + 60*i, 35 + 30*j , 50, 20))
        '''
    def bucle_ppal(self):
        game_over = False
        nivel = 0

        while self.contador_vidas > 0 and not game_over and nivel < len(niveles):
            self.creaRocas(nivel)

            while self.contador_vidas > 0 and not game_over and len(self.rocas) > 0:
                self.reloj.tick(60)

                eventos = pg.event.get()
                for evento in eventos:
                    if evento.type == pg.QUIT:
                        game_over = True


                self.pantalla.fill((255,0,0))
                for roca in self.rocas:
                    if roca.comprobarToque(self.bola):
                        self.rocas.remove(roca)
                        self.puntos += 10
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

            nivel += 1

    pg.quit()

