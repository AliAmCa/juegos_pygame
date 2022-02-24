from importlib import resources
import pygame as pg

from arkanoid.entities import Bola, Rock, Player
from arkanoid import niveles, FPS

class Escena:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.reloj = pg.time.Clock()
    
    def bucle_ppal(self) -> bool:
        pass


class Partida (Escena):
    
    def __init__(self, pantalla):
        super().__init__(pantalla)

        
        self.player = Player(self.pantalla, self.pantalla.get_width()//2, self.pantalla.get_height()-30)
        self.bola = Bola(self.pantalla, self.pantalla.get_width()//2, self.pantalla.get_height()//2,(255,255,0))
        self.rocas = []
        self.todos = []
        self.todos.append(self.bola)
        self.todos.append(self.player)

        self.contador_vidas = 3
       
        self.puntos = 0

    def creaRocas(self, nivel):
        for col, fil in niveles[nivel]:
            self.rocas.append(Rock(self.pantalla, 5 + 60*col, 25 + 30*fil , 50, 20))

        self.todos = self.todos + self.rocas
        

    def bucle_ppal(self):
        game_over = False
        nivel = 0

        while self.contador_vidas > 0 and not game_over and nivel < len(niveles):
            self.creaRocas(nivel)

            while self.contador_vidas > 0 and not game_over and len(self.rocas) > 0:
                self.reloj.tick(FPS)

                eventos = pg.event.get()
                for evento in eventos:
                    if evento.type == pg.QUIT:
                        game_over = True
                        return False


                self.pantalla.fill((255,0,0))

                for objeto in self.todos:
                    objeto.mover()


                for roca in self.rocas:
                    if roca.comprobarToque(self.bola):
                        self.rocas.remove(roca)
                        self.todos.remove(roca)
                        self.puntos += 10
                    
                    

                self.bola.compruebaChoque(self.player)

                if not self.bola.esta_viva:
                    self.contador_vidas -= 1
                    self.bola.reset()

                for objeto in self.todos:
                    objeto.dibujar()

                pg.display.flip()

            nivel += 1
            self.bola.reset()

        return True


class GameOver(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)

        self.fuente = pg.font.Font("resources/fonts/FredokaOne-Regular.ttf", 25)


    def bucle_ppal(self):
        
        while True:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    return False

                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_SPACE:
                        return True

            self.pantalla.fill((30,30,255))
            texto = self.fuente.render("GAME OVER", True, (255,255,0))

            print (texto.get_rect())

            self.pantalla.blit(texto, (10,10))

            pg.display.flip()