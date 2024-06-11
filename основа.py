import pygame, sys , random , time
import pygame as pg

pg.init()
pygame.init()


FPS = 60
X =  600
Y = 600
screen = pygame.display.set_mode((X, Y))
clock = pygame.time.Clock()
game_state = 1
sekundi = 0

#классы
class Any:
    def __init__ (self , x , y , weight , height , sprite):
        self.rect = pygame.Rect(x , y , weight , height)
        self.sprite = pygame.image.load(sprite)
        self.sprite = pygame.transform.scale(self.sprite, (weight , height))    
    def draw(self):
        screen.blit(self.sprite ,(self.rect.x , self.rect.y))

class Wall:
    def __init__(self, x, y, w, h, img, col, row):
        self.col = col
        self.row = row
        self.rect = pygame.Rect(x, y, w, h)
        self.img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.img, (w, h))
        self.open = False
    def draw(self):
        screen.blit(self.img, (self.rect.x, self.rect.y))

def check(pole , i , j):
    rows = len(pole)
    cols = len(pole[0])
    countOfbomb = 0
    for x in range(max(0, i-1), min(rows,i+2)):
        for y in range(max(0, j-1), min(cols,j+2)):
            if pole[x][y] == '*':
                countOfbomb += 1

    return countOfbomb

def generatePole(rows , cols , mines):
    pole = []   
    for i in range(rows):
        pole.append([])
        for j in range(cols):
            pole[i].append(0) 


    minecount = 0
    while minecount < mines:
        i = random.randint(0 , rows - 1)               
        j = random.randint(0 , cols - 1)   
        if pole[i][j] != '*':
            pole[i][j] = "*"
            minecount += 1

    return pole                




#рандомайзер поля
pole = generatePole(4 , 4 , 6)
pole1 = generatePole(8 , 8 , 28)
pole2 = generatePole(16 , 16 , 84)

walls = []
walls2 = []
walls3 = []

for line in range(len(pole)):
    for cell in range(len(pole[line])):
            walls.append(Wall(cell * 150, line * 150, 150, 150, 'пусто.png', cell, line))

for line in range(len(pole1)):
    for cell in range(len(pole1[line])):
            walls2.append(Wall(cell * 75, line * 75, 75, 75, 'пусто.png', cell, line))

for line in range(len(pole2)):
    for cell in range(len(pole2[line])):
            walls3.append(Wall(cell * 37, line * 37, 37, 37, 'пусто.png', cell, line))      

# rows = len(pole)
# cols = len(pole[0])

# rows1 = len(pole1)
# cols1 = len(pole1[0])

# rows2 = len(pole2)
# cols2 = len(pole2[0])

# for i in range(rows):
#     for j in range(cols):
#         if pole[i][j] != 1:
#             pole[i][j] = check(pole , i ,  j)

#весь текст
font = pygame.font.Font('mine-sweeper.ttf', 50)
font2 = pygame.font.Font('mine-sweeper.ttf', 45)
font3 = pygame.font.Font('mine-sweeper.ttf', 35)
message1 = font.render('''start''', True ,(0, 0, 0) )
x4 = font2.render('''4 x 4''', True ,(0, 0, 0) )
x8 = font2.render('''8 x 8''', True ,(0, 0, 0) )
x16 = font3.render('''16 x 16''', True ,(0, 0, 0) )
x16 = pygame.transform.scale(x16 , (190 , 60))
win = font2.render('''you win!!!''', True ,(0, 0, 0) )
restartTxT = font.render('''restart?''' , True , (0,0,0) )
restartTxT = pygame.transform.scale(restartTxT , (250 , 150))

#кнопки
button = pygame.Rect(150, 150, 300 , 100)
hard1 = pygame.Rect(200, 150 , 200 , 100)#сложность 4 х 4
hard2 = pygame.Rect(200, 300 , 200 , 100)#сложность 8 х 8
hard3 = pygame.Rect(200, 450 , 200 , 100)#сложность 16 х 16
restart = pygame.Rect(150 , 225 , 300 , 150)

#цвета
buttonColor = (100, 100 , 100)
hardColor1 = (100 , 100 , 100)
hardColor2 = (255 , 255 , 255)
hardColor3 = (50 , 50 , 50)
restartColor = (148 , 0 , 211)

fon = Any(0 , 0 , 600 , 6000 , 'поле.jpg')
pos1 = Any(0 , 0 , 100 , 100 , 'bomb.png')

found = 0

#надо
screen = pygame.display.set_mode((X , Y))
clock = pygame.time.Clock()

#звуки
sound1 = pg.mixer.Sound('lose.mp3')
sound2 = pg.mixer.Sound('tick.mp3')



#начало цикла
while True:
    screen.fill((200 , 200 , 200))
    if game_state == 1:            
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x , y = event.pos
                if button.x < x < 450 and 150 < y < 250:
                    game_state = 2
            

        pygame.draw.rect(screen, buttonColor , button)
        fon.draw
        screen.blit(message1,(170 , 165))

    if game_state == 2:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_state = 1

            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x , y = event.pos
                if 200 < x < 400 and 150 < y < 250:
                    game_state = 3
                elif 200 < x < 400 and 300 < y < 400:
                    game_state = 4
                elif 200 < x < 400 and 450 < y < 550:
                    game_state = 5  

        pygame.draw.rect(screen, hardColor1 , hard1)        
        pygame.draw.rect(screen, hardColor2 , hard2)         
        pygame.draw.rect(screen, hardColor3 , hard3)
        screen.blit(x4,(205 , 170))
        screen.blit(x8,(205 , 320)) 
        screen.blit(x16,(205 , 470)) 

    if game_state == 'lose':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x , y = event.pos
                if 150 < x < 450 and 225 < y < 375:
                    pole = generatePole(4 , 4 , 6)
                    pole1 = generatePole(8 , 8 , 28)
                    pole2 = generatePole(16 , 16 , 84)

                    walls = []
                    walls2 = [] 
                    walls3 = []

                    for line in range(len(pole)):
                        for cell in range(len(pole[line])):
                                walls.append(Wall(cell * 150, line * 150, 150, 150, 'пусто.png', cell, line))

                    for line in range(len(pole1)):
                        for cell in range(len(pole1[line])):
                                walls2.append(Wall(cell * 75, line * 75, 75, 75, 'пусто.png', cell, line))

                    for line in range(len(pole2)):
                        for cell in range(len(pole2[line])):
                                walls3.append(Wall(cell * 37, line * 37, 37, 37, 'пусто.png', cell, line))   
                    game_state = 1 
     
        pygame.draw.rect(screen, restartColor , restart)
        screen.blit(restartTxT,(175 , 225))

        # time.sleep(3)
        # sys.exit()
        
    if game_state == 3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for wall in walls:
                    if wall.rect.collidepoint(event.pos[0], event.pos[1]):
                        mine = (pole[wall.row][wall.col])

                        if mine == '*':
                            wall.img = pygame.image.load('bomb.png')  
                            wall.img = pygame.transform.scale(wall.img, (wall.rect.width, wall.rect.height))                                                      
                            sound1.play()

                            game_state = 'lose'

                        else:
                            if wall.open == False:
                                    
                                wall.open = True
                                sound2.play()
                                boms = check(pole , wall.row , wall.col)
                                wall.img = pygame.image.load(str(boms) + '.png')
                                wall.img = pygame.transform.scale(wall.img, (wall.rect.width, wall.rect.height))

                                found += 1
                                if found == 10:                             
                                    game_state = 'win'

        for wall in walls:
            wall.draw()

    if game_state == 4:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for wall in walls2:
                    if wall.rect.collidepoint(event.pos[0], event.pos[1]):
                        mine = (pole1[wall.row][wall.col])

                        if mine == '*':
                            wall.img = pygame.image.load('bomb.png')  
                            wall.img = pygame.transform.scale(wall.img, (wall.rect.width, wall.rect.height))                                                      
                            sound1.play()

                            game_state = 'lose'

                        else:
                            sound2.play()
                            boms = check(pole1 , wall.row , wall.col)
                            wall.img = pygame.image.load(str(boms) + '.png')
                            wall.img = pygame.transform.scale(wall.img, (wall.rect.width, wall.rect.height))
                            found += 1
                            if found == 36:                              
                                game_state = 'win'

        for wall in walls2:
            wall.draw()

    if game_state == 5:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for wall in walls3:
                    if wall.rect.collidepoint(event.pos[0], event.pos[1]):
                        mine = (pole2[wall.row][wall.col])
                        if mine == '*':
                            wall.img = pygame.image.load('bomb.png')  
                            wall.img = pygame.transform.scale(wall.img, (wall.rect.width, wall.rect.height))                                                      
                            sound1.play()

                            game_state = 'lose'

                        else:
                            sound2.play()
                            boms = check(pole2 , wall.row , wall.col)
                            wall.img = pygame.image.load(str(boms) + '.png')
                            wall.img = pygame.transform.scale(wall.img, (wall.rect.width, wall.rect.height))
                            found += 1                                                                                                                                                   
                            if found == 174:
                                game_state = 'win'

        for wall in walls3:
            wall.draw()

    if game_state == 'win':

        sekundi += 1
        if sekundi == 180:
            sys.exit()           
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()            
        screen.blit(win,(130 , 250))




    pygame.display.update()
    clock.tick(60)

    
  
