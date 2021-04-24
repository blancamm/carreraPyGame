import pygame, sys

class Game():
    runners = []
    __startLine = 20 #esto es asi porque ahora las coordenadas son distintas
    __finishLine = 620
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption('Carrera de bichos')
        self.__background = pygame.image.load('imagenes/background.png') #elegir fondo
        
    def competir(self):
        gameOver = False
        while not gameOver:         
            for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                     gameOver = True
                     
            self.__screen.blit(self.__background, (0,0)) #pintar fondo
            
            pygame.display.flip()#REFRESCO DE PANTALLA
            
        pygame.quit()
        sys.exit() 

    
if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.competir()
    
    