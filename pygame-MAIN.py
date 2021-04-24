import pygame
import sys

    

class Game():
    
    runners = []
    
    def __init__(self):
        
        self.__screen = pygame.display.set_mode((640,480)) #aqui estamos diciendo el tamaño
        pygame.display.set_caption('Carrera de bichos')# a la pantalla se le pone titulo
        self.background = pygame.image.load('imagenes/background.png') #elegir fondo
        
        self.runner = pygame.image.load('imagenes/smallball.png')
        
    def competir(self):
        
        x = 0
        hayGanador = False
        
        while not hayGanador:
            #comprobacion de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #te esta diciendo que si pulsas las tecla Esc, se para el juego (QUIT es Esc en pygame)
                    pygame.quit()
                    sys.exit()
                    
                    
            #refrescar la pantalla/renderizar        
            self.__screen.blit(self.background, (0,0)) #pintar fondo
            self.__screen.blit(self.runner, (x,240))
            pygame.display.flip() #refrescar
            
            x  +=3
            
            if x >= 250:
                hayGanador = True
        pygame.quit()
        sys.exit()       
        
        
if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.competir()
    