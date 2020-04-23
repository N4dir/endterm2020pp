import pygame
import random
from pygame import mixer

pygame.font.init()
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Collector")



mixer.music.load("Music/1.wav")
mixer.music.play(-1)
mixer.music.set_volume(0.1)

soundGG = mixer.Sound("Music/GG1.wav")
soundCatch = mixer.Sound("Music/plus_1.wav")

soundMiss = mixer.Sound("Music/miss.wav")


class Basket:
    def __init__(self, x, speed, color):
        self.x = x
        self.y = 450
        self.speed = speed
        self.width = 150
        self.height = 80
        self.color = color
        self.width1 = 130
        self.height1 = 70
        self.pressed = pygame.key.get_pressed()
        

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x,self.y,self.width,self.height))
        pygame.draw.rect(screen, (0,0,0), (self.x + 10, self.y, self.width1, self.height1))

    def move_left(self):
        
        self.x -= self.speed

        if self.x > screen.get_size()[0]:
            self.x = 0 - self.width
        if self.x < 0 - self.width:
            self.x = screen.get_size()[0]

        

    def move_right(self):

        self.x += self.speed

        if self.x > screen.get_size()[0]:
            self.x = 0 - self.width
        if self.x < 0 - self.width:
            self.x = screen.get_size()[0]

    def collision(self, circle):
        lx1 = self.x + 10
        lx2 = circle.x - circle.radius
        rx1 = self.x + self.width1
        rx2 = circle.x + circle.radius
        ty1 = self.y
        ty2 = circle.y - circle.radius
        by1 = self.y + self.height1
        by2 = circle.y + circle.radius

        lx = max(lx1, lx2)
        rx = min(rx1, rx2)
        ty = max(ty1, ty2)
        by = min(by1, by2)

        if lx <= rx and ty <= by:
            return True
        return False


class Circle:
    def __init__(self):
        self.x = random.randint(75, 725)
        self.y = random.randint(40, 80)
        self.speed = 15
        self.radius = 10
        self.cnt = 0
        

    def draw(self):
        Centre = (self.x, self.y)
        pygame.draw.circle(screen, (255,0,0), Centre, self.radius)
        
    def move(self):
        self.y += self.speed

        self.draw()

    def new_one(self):
        self.x = random.randint(75, 725)
        self.y = random.randint(40, 80)

        self.cnt += 1

    def upala_blet(self):
        if self.y >= screen.get_size()[1] - 40:
            self.new_one()
            self.cnt -= 6
            if self.cnt >= 0:
                soundMiss.play()
    
    def cnt_count(self):
        font = pygame.font.SysFont("Arial", 36)
        text = font.render("Collected: "+ str(self.cnt), 1, (255,255,255))
        place = text.get_rect(center=(720,50))
        screen.blit(text,place)


is_game = True
musicgg = False
gg = 0

basket = Basket(200, 20, (7,77,168))

circle = Circle()

FPS = 30

clock = pygame.time.Clock()

while is_game:
    mills = clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
               is_game = False
    screen.fill((0,0,0))

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        basket.move_left()
    if pressed[pygame.K_RIGHT]:
        basket.move_right()

    circle.move()
    basket.draw()

    if basket.collision(circle):
        circle.new_one()
        soundCatch.play()
    circle.upala_blet()

    if circle.cnt < 0:
        font1 = pygame.font.SysFont("Arial", 80)
        text1 = font1.render("Game Over", 1, (255,255,255))
        place1 = text1.get_rect(center = (400,300))

        font2 = pygame.font.SysFont("Arial", 30)
        text2 = font2.render("Press ESC to EXIT",1, (255,255,255))
        place2 = text2.get_rect(center = (400,340))

        screen.blit(text2,place2)
        screen.blit(text1,place1)
        basket.speed = 0
        circle.speed = 0
        mixer.music.stop()
        musicgg = True
        pygame.display.flip()

    if gg == 0 and musicgg:
        soundGG.play()
        gg = 1

    circle.cnt_count()

    pygame.display.flip()
