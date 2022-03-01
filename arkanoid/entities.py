import pygame as pg

class Vigneta(pg.sprite.Sprite):
    def __init__(self, padre):
        super().__init__()
        self.padre = padre

    def intersecta(self, otro) -> bool:
        if self.rect.w > otro.rect.w:
            menor_ancho = otro
            mayor_ancho = self
        else:
            menor_ancho = self
            mayor_ancho = otro

        if self.rect.h > otro.rect.h:
            menor_alto = otro
            mayor_alto = self
        else:
            menor_alto = self
            mayor_alto = otro

        return (menor_ancho.rect.left  in range(mayor_ancho.rect.left, mayor_ancho.rect.right) or \
                menor_ancho.rect.right  in range(mayor_ancho.rect.left, mayor_ancho.rect.right)) and \
                (menor_alto.rect.top  in range(mayor_alto.rect.top, mayor_alto.rect.bottom) or \
                menor_alto.rect.bottom in range(mayor_alto.rect.top, mayor_alto.rect.bottom))
                
 
class Rock(Vigneta):
    
    def __init__(self, x, y, ancho, alto,color = (0,255,255)):
        super().__init__(None)
        self.image = pg.Surface((ancho, alto))
        pg.draw.rect(self.image, color, (0,0,ancho,alto))
        self.rect = self.image.get_rect(x=x, y=y)
      
        
   
    def comprobarToque(self, bola):
        if self.intersecta(bola):
            bola.vy *=-1
            return True
        return False

class Player(Vigneta):
    
    def __init__(self, padre, centrox, centroy):
        super().__init__(padre)
        self.imagenes = []
        for i in range(3):
            self.imagenes.append( pg.image.load(f"./resources/images/electric0{i}.png"))
        
        self.estado = 0
        
        self.frecuenciaCambio = 5
        self.contador_frames =0
        self.image = self.imagenes[self.estado]
        self.rect = self.image.get_rect(centerx = centrox, centery = centroy)
        
        self.vx = 5
        
        

    def update(self):
        teclas = pg.key.get_pressed()

        if teclas[pg.K_LEFT]:
           self.rect.x -= self.vx

        if teclas[pg.K_RIGHT]:
            self.rect.x += self.vx
        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.right >= self.padre.get_width():
            self.rect.right = self.padre.get_width() 

            
        self.contador_frames +=1
        if self.contador_frames == self.frecuenciaCambio:
            self.estado = (self.estado +1) % len(self.imagenes)
            self.contador_frames =0

        self.image = self.imagenes[self.estado]

class Bola(Vigneta):
    def __init__(self, padre, centrox, centroy, radio = 10, color = (255,255,255) ):
        super().__init__(padre)

        self.image = pg.Surface((radio*2, radio*2))
        pg.draw.circle(self.image, color, (radio,radio), radio)
        self.rect = self.image.get_rect(center = (centrox,centroy))

        self.vx = 3
        self.vy = 3
        self.xinit = centrox
        self.yinit = centroy
        self.esta_viva = True
    

    
    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

        if self.rect.right >= self.padre.get_width()  or self.rect.x <= 0:
            self.vx *= -1
        if self.rect.y <= 0:
            self.vy *= -1
        if self.rect.bottom >= self.padre.get_height():
            self.esta_viva = False
            
    def reset(self):
        self.rect.x = self.xinit
        self.rect.y = self.yinit
        self.vx = 3
        self.vy = 3
        self.esta_viva = True
        
    def compruebaChoque(self, otro):
        if self.intersecta(otro):
            self.vy *= -1
