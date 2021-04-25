#para poder un corredor moverlo por pantalla

import pygame, sys, random

from pygame.locals import *

class Runner():
    __customes = ('turtle', 'fish', 'prawn', 'moray', 'octopus')
    
    def __init__(self, x=0, y=0):
        indiceCustome = random.randint(0,4)
         
        self.custome = pygame.image.load('imagenes/{}.png'.format(self.__customes[indiceCustome]))
        self.position = [x,y] #para que sea mutable
        self.name = ''
        
class Game():
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption('Carrera de bichos')
        self.__background = pygame.image.load('imagenes/background.png') #elegir fondo
        
        self.runner = Runner (320,240)
        
    def star(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()   
                elif event.type == KEYDOWN:
                    if event.key ==K_UP:                     #MOVER HACIA ARRIBA
                        self.runner.position[1] -= 5
                        
                    elif event.key ==K_DOWN: #MOVER HACIA ABAJO
                        self.runner.position[1] += 5 #PORQUE LAS COORDENADAS SON DISTINTAS
                        
                    elif event.key == K_LEFT:
                        self.runner.position[0] -= 5
                        
                    elif event.key == K_RIGHT:
                        #MOVER A LA DERECHA
                        self.runner.position[0] += 5
                    else:
                        pass
                    
            self.__screen.blit(self.__background, (0,0)) # SE ESCRIBE CADA VEZ, PORQUE SI NO SE PONDRIAN UNA ENCIMA DE OTRA Y SE VERIA SOMBRA
            self.__screen.blit(self.runner.custome, self.runner.position)
            
            pygame.display.flip()
                    
if __name__ == '__main__':
    game = Game()
    game.star()
    
