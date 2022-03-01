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
        self.bola = Bola(self.pantalla, self.pantalla.get_width()//2, self.pantalla.get_height()//2)
        self.fondo = pg.image.load("./resources/images/background.jpg")
        self.rocas = pg.sprite.Group()
        self.todos = pg.sprite.Group()

        self.contador_vidas = 3
        self.reset()    
        self.puntos = 0
    
    def reset(self):
        self.rocas.empty()
        self.todos.empty()
        self.todos.add(self.bola, self.player)
        self.contador_vidas = 3
    
    def creaRocas(self, nivel):
        for col, fil in niveles[nivel]:
            self.rocas.add(Rock(5 + 60*col, 25 + 30*fil , 50, 20))

        self.todos.add(self.rocas)
        

    def bucle_ppal(self) -> bool:
        game_over = False
        nivel = 0
        self.reset()

        while self.contador_vidas > 0 and not game_over and nivel < len(niveles):
            self.creaRocas(nivel)

            while self.contador_vidas > 0 and not game_over and len(self.rocas) > 0:
                self.reloj.tick(FPS)

                eventos = pg.event.get()
                for evento in eventos:
                    if evento.type == pg.QUIT:
                        game_over = True
                        return False


                
                self.pantalla.blit(self.fondo, (0,0))
               

                self.todos.update()


                for roca in self.rocas:
                    if roca.comprobarToque(self.bola):
                        self.rocas.remove(roca)
                        self.todos.remove(roca)
                        self.puntos += 10
                    
                    

                self.bola.compruebaChoque(self.player)

                if not self.bola.esta_viva:
                    self.contador_vidas -= 1
                    self.bola.reset()

                self.todos.draw(self.pantalla)

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
            rectTexto = texto.get_rect()
            rectPantalla = self.pantalla.get_rect()

            #print (texto.get_rect())

            self.pantalla.blit(texto, (rectPantalla.centerx - rectTexto.centerx, rectPantalla.centery - rectTexto.centery))
            pg.display.flip()