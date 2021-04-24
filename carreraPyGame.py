import pygame, sys, random

class Runner():
    __customes = ('turtle', 'fish', 'prawn', 'moray', 'octopus')
    
    def __init__(self, x=0, y=0, custome = 'turtle'):
        self.custome = pygame.image.load('imagenes/{}.png'.format(custome))
        self.position = [x,y] #para que sea mutable
        self.name = custome
        
    def avanzar(self):
        self.position[0] += random.randint (1,6) #solo se mueve en el eje x
        
    
class Game():
    runners = []
    __posY = (160, 200, 240, 280)
    __names = ('Speedy', 'Lucera', 'Alonso', 'Toby')
    __startLine = 5 #SI PUSIESE -15 ME SALDRIA SOLO LA CARA DE LA TORTUGA #esto es asi porque ahora las coordenadas son distintas
    __finishLine = 620
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption('Carrera de bichos')
        self.__background = pygame.image.load('imagenes/background.png') #elegir fondo
        
        for i in range (4):
            runner = Runner(self.__startLine,self.__posY[i])
            runner.name = self.__names[i]
            self.runners.append(runner)
    
    def close(self):
        pygame.quit()
        sys.exit()
        
    def competir(self):
        gameOver = False
        while not gameOver:         
            for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                     gameOver = True
                     
            for item in self.runners:
                item.avanzar()
                if item.position[0] >= self.__finishLine:
                    print('{} ha ganado'.format(item.name))
                    gameOver = True
            
                     
            self.__screen.blit(self.__background, (0,0)) #pintar fondo
            
            for item in self.runners:
                self.__screen.blit(item.custome, item.position) #IMPORTANTE VER A QUE ME QUIERO REFERIR
            
            
            pygame.display.flip()#REFRESCO DE PANTALLA
            
 #para que se vea el resultado y que se cierre cuando el usuario pulse el quit
            
        while True: 
            for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                     self.close()

    
if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.competir()
    
    