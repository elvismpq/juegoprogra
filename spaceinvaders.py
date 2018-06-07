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
        self.velocidad=5
        self.Vida=True
    def movimiento(self):
        if self.Vida==True:
            if self.rect.left<=0:
               self.rect.left=0
            elif self.rect.right>=870:
                self.rect.right=870
        self.listaDisparo=[]

    def disparar(self):
        print("disparo")
    def dibujar(self,superficie):
        superficie.blit(self.ImagenNave,self.rect)
class Proyectil(pygame.sprite.Sprite):
    def __init__(self,posX,posY):
        pygame.sprite.Sprite.__init__(self)
        self.imageProyectil=pygame.image.load("imagenes/disparoa.jpg")
        self.rect=self.imageProyectil.get_rect()
        self.velocidadDisparo=5
        self.rect.top=posY
        self.rect.left=posX
    def trayectoria(self):
        self.rect.top=self.rect.top-self.velocidadDisparo
    def dibujar(self,superficie):
        superficie.blit(self.imageProyectil,self.rect)

def SpaceInvader():
    pygame.init()
    venta=pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("Space Invader")
    ImagenFondo=pygame.image.load("imagenes/Fondo.jpg")
    jugador=naveEspacial()
    enJuego=True
    demoPro=Proyectil(ancho/2,alto-30)
    while True:
        jugador.movimiento()
        demoPro.trayectoria()
        venta.fill((0,0,0))
        for event in pygame.event.get():
            if enJuego==True:
                if event.type==pygame.KEYDOWN:
                    if event.key==K_LEFT:
                        jugador.rect.centerx-=jugador.velocidad
                    elif event.key==K_RIGHT:
                        jugador.rect.centerx+=jugador.velocidad
                    elif event.key==K_SPACE:
                        jugador.disparar()
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        venta.blit(ImagenFondo,(0,0))
        demoPro.dibujar(venta)
        jugador.dibujar(venta)
        pygame.display.update()

SpaceInvader()
