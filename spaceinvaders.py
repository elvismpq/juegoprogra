import pygame,sys
from pygame.locals import *
from random import randint
ancho=900
alto=480

class naveEspacial(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagenNave=pygame.image.load("imagenes/nave.png")
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
        proy=Proyectil(x,y,"imagenes/disparoa.png",True)
        self.listaDisparo.append(proy)
    def dibujar(self,superficie):
        superficie.blit(self.ImagenNave,self.rect)
class Proyectil(pygame.sprite.Sprite):
    def __init__(self,posx,posy,ruta,personaje):
        pygame.sprite.Sprite.__init__(self)
        self.imageProyectil=pygame.image.load(ruta)
        self.rect=self.imageProyectil.get_rect()
        self.velocidadDisparo=2
        self.rect.top=posy
        self.rect.left=posx
        self.disparoPersonaje =personaje
    def trayectoria(self):
        if self.disparoPersonaje == True:
            self.rect.top=self.rect.top-self.velocidadDisparo
        else:
            self.rect.top = self.rect.top + self.velocidadDisparo
    def dibujar(self,superficie):
        superficie.blit(self.imageProyectil,self.rect)
class Invasor(pygame.sprite.Sprite):
    def __init__(self,posx,posy):
        pygame.sprite.Sprite.__init__(self)
        self.imagenA = pygame.image.load("imagenes/MarcianoA.jpg")
        self.imagenB = pygame.image.load("imagenes/MarcianoB.jpg")
        self.listaImagenes=[self.imagenA, self.imagenB]
        self.posImagen=0
        self.imagenInvasor=self.listaImagenes[self.posImagen]
        self.rect=self.imagenInvasor.get_rect()
        self.listaDisparo=[]
        self.velocidad=20
        self.rect.top=posy
        self.rect.left=posx
        self.rangoDisparo=5
        self.tiempoCambio=1

    def dibujar(self,superficie):
        self.imagenInvasor=self.listaImagenes[self.posImagen]
        superficie.blit(self.imagenInvasor, self.rect)

    def comportamiento(self,tiempo):
        if self.tiempoCambio == tiempo:
              self.posImagen +=+1
              self.tiempoCambio +=+1
              if self.posImagen >len(self.listaImagenes)-1:
                  self.posImagen=0
        self._ataque()
    def _ataque(self):
        if (randint(0,100)<self.rangoDisparo):
           self._disparo()
    def _disparo(self):
        x,y =self.rect.center
        miProyectil=Proyectil(x,y,"imagenes/disparob.png",False)
        self.listaDisparo.append(miProyectil)
def SpaceInvader():
    pygame.init()
    venta=pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("Space Invader")
    ImagenFondo=pygame.image.load("imagenes/Fondo.jpg")
    jugador=naveEspacial()
    enemigo = Invasor(100, 100)
    enJuego=True
    reloj=pygame.time.Clock()

    while True:
        reloj.tick(60)
        #jugador movimiento
        tiempo=int(pygame.time.get_ticks()/1000)
        for event in pygame.event.get():
            if enJuego==True:
                if event.type==pygame.KEYDOWN:
                    if event.key==K_LEFT:
                        jugador.movimientoIzquierda()
                    elif event.key==K_RIGHT:
                        jugador.movimientoDerecha()
                    elif event.key==K_SPACE:
                        x,y=jugador.rect.center
                        jugador.disparar(x,y)
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        venta.blit(ImagenFondo,(0,0))
        enemigo.comportamiento(int(tiempo))
        enemigo.dibujar(venta)
        jugador.dibujar(venta)
        if len(jugador.listaDisparo)>0:
            for x in jugador.listaDisparo:
                x.dibujar(venta)
                x.trayectoria()
                if x.rect.top<-10:
                    jugador.listaDisparo.remove(x)
        if len(enemigo.listaDisparo)>0:
            for x in enemigo.listaDisparo:
                x.dibujar(venta)
                x.trayectoria()
                if x.rect.top>900:
                    enemigo.listaDisparo.remove(x)
        pygame.display.update()

SpaceInvader()

