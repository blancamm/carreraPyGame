import pygame

class Game():
    
    corredores = []
    
    def __init__(self):
        
        self.__screen = pygame.display.set_mode((640,480)) #aqui estamos diciendo el tamaño
        pygame.display.set_caption('Carrera de bichos')# a la pantalla se le pone titulo
        self.background = pygame.image.load('imagenes/background.png') #elegir fondo
        
    def competir(self):
        
        while True:
            #comprobacion de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #te esta diciendo que si pulsas las tecla Esc, se para el juego (QUIT es Esc en pygame)
                    pygame.quit()
                    sys.exit()
                    
                    
            #refrescar la pantalla/renderizar        
            self.__screen.blit(self.background, (0,0)) #pintar fondo
            pygame.display.flip() #refrescar
        
if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.competir()
    