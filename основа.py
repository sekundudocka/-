import pygame, sys , random
import pygame as pg

pg.init()
pygame.init()


FPS = 60
X =  600
Y = 600
screen = pygame.display.set_mode((X, Y))
clock = pygame.time.Clock()
game_state = 1

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
    def draw(self):
        screen.blit(self.img, (self.rect.x, self.rect.y))

#рандомайзер поля
pole = [[0,0,0,0],
       [0,0,0,0],    
       [0,0,0,0],
       [0,0,0,0],
        ]

walls = []


for line in range(len(pole)):
    for cell in range(len(pole[line])):
            walls.append(Wall(cell * 150, line * 150, 150, 150, 'поле.jpg', cell, line))

rows = len(pole)
cols = len(pole[0])

for i in range(3):
    for j in range(3):
        pole[i][j] = random.randint(0, 1) 

def check(pole , i , j):
    countOfbomb = 0
    for x in range(max(0, i-1), min(rows,i+2)):
        for y in range(max(0, j-1), min(cols,j+2)):
            if pole[x][y] == 1:
                countOfbomb += 2 

    return countOfbomb 

for i in range(rows):
    for j in range(cols):
        if pole[i][j] != 1:
            pole[i][j] = check(pole , i ,  j)


file = open('map3.txt' , 'w')
file.write('')
file.close()
file = open('map3.txt' , 'a')
for i in pole:
    for j in i:
        file.write(str(j))
    file.write('\n')

print(pole[0])
print(pole[1])
print(pole[2])
print(pole[3])

#весь текст
font = pygame.font.Font('mine-sweeper.ttf', 50)
font2 = pygame.font.Font('mine-sweeper.ttf', 45)
message1 = font.render('''start''', True ,(0, 0, 0) )
x4 = font2.render('''4 x 4''', True ,(0, 0, 0) )
x8 = font2.render('''4 x 4''', True ,(0, 0, 0) )
x16 = font2.render('''4 x 4''', True ,(0, 0, 0) )

#кнопки
button = pygame.Rect(150, 150, 300 , 100)
hard1 = pygame.Rect(200, 150 , 200 , 100)#сложность 4 х 4
hard2 = pygame.Rect(200, 300 , 200 , 100)#сложность 8 х 8
hard3 = pygame.Rect(200, 450 , 200 , 100)#сложность 16 х 16

#цвета
buttonColor = (100, 100 , 100)
hardColor1 = (100 , 100 , 100)
hardColor2 = (255 , 255 , 255)
hardColor3 = (50 , 50 , 50)

fon = Any(0 , 0 , 600 , 6000 , 'поле.jpg')
pos1 = Any(0 , 0 , 100 , 100 , 'bomb.png')

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

        pygame.draw.rect(screen, hardColor1 , hard1)        
        pygame.draw.rect(screen, hardColor2 , hard2)         
        pygame.draw.rect(screen, hardColor3 , hard3)
        screen.blit(x4,(205 , 170))
        screen.blit(x8,(205 , 320)) 
        screen.blit(x16,(205 , 470)) 

    if game_state == 3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for wall in walls:
                    if wall.rect.collidepoint(event.pos[0], event.pos[1]):
                        mine = (pole[wall.row][wall.col])
                        if mine == 1:
                            sys.exit()
                        else:
                            print('норм')

    pygame.display.update()
    clock.tick(60)

    
  
        # for event in pygame.event.get():
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_SPACE:
        #             game_state = 1

        #     if event.type == pygame.QUIT:
        #         sys.exit()

        # if event.type == pygame.MOUSEBUTTONDOWN:
        #   if click.collidepoint(event.pos[0], event.pos[1]):
        #     event.pos - это координаты нажатия [0] - x [1] - y