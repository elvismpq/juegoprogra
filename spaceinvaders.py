import pygame,sys
from pygame.locals import *
ancho=900
alto=480

class naveEspacial(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagenNave=pygame.image.load("imagenes/Nave.jpg")
        self.rect=self.ImagenNave.get_rect()
        self.rect.centerx=ancho/2
        self.rect.centery=alto-30
        self.velocidad=20
        self.Vida=True
        self.listaDisparo=[]
    def movimientoDerecha(self):
        self.rect.right+=self.velocidad
        self.movimiento()
    def movimientoIzquierda(self):
        self.rect.left-=self.velocidad
        self.movimiento()
    def movimiento(self):
        if self.Vida==True:
            if self.rect.left<=0:
               self.rect.left=0
            elif self.rect.right>=870:
                self.rect.right=870
    def disparar(self,x,y):
        proy=Proyectil(x,y)
        self.listaDisparo.append(proy)
    def dibujar(self,superficie):
        superficie.blit(self.ImagenNave,self.rect)
class Proyectil(pygame.sprite.Sprite):
    def __init__(self,posx,posy):
        pygame.sprite.Sprite.__init__(self)
        self.imageProyectil=pygame.image.load("imagenes/disparoa.jpg")
        self.rect=self.imageProyectil.get_rect()
        self.velocidadDisparo=2
        self.rect.top=posy
        self.rect.left=posx
    def trayectoria(self):
        self.rect.top=self.rect.top-self.velocidadDisparo
    def dibujar(self,superficie):
        superficie.blit(self.imageProyectil,self.rect)
class Invasor(pygame.sprite.Sprite):
    def __init__(self,posx,posy):
        pygame.sprite.Sprite.__init__(self)
        self.imagenA=pygame.image.load("imagenes/MarcianoA.jpg")
        self.rect=self.imagenA.get_rect()
        self.listaDisparo=[]
        self.velocidad=20
        self.rect.top=posy
        self.rect.left=posx
    def dibujar(self,superficie):
        superficie.blit(self.imagenA,self.rect)
def SpaceInvader():
    pygame.init()
    venta=pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("Space Invader")
    ImagenFondo=pygame.image.load("imagenes/Fondo.jpg")
    jugador=naveEspacial()
    enJuego=True
    reloj=pygame.time.Clock()
    enemigo=Invasor(100,100)
    while True:
        reloj.tick(60)
        for event in pygame.event.get():
            if enJuego==True:
                if event.type==pygame.KEYDOWN:
                    if event.key==K_LEFT:
                        jugador.movimientoIzquierda()
                    elif event.key==K_RIGHT:
                        jugador.movimientoDerecha()
                    elif event.key==K_SPACE:
                        x,y=jugador.rect.center
                        print (jugador.rect.center)
                        jugador.disparar(x,y)
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        venta.blit(ImagenFondo,(0,0))
        enemigo.dibujar(venta)
        if len(jugador.listaDisparo)>0:
            for x in jugador.listaDisparo:
                x.dibujar(venta)
                x.trayectoria()
                if x.rect.top<100:
                    jugador.listaDisparo.remove(x)
        jugador.dibujar(venta)
        pygame.display.update()

SpaceInvader()
