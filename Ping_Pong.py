from pygame import *

time.delay(50)

window = display.set_mode((1200,600))
display.set_caption('Саблезубая пиявка')
background = transform.scale(image.load("hydra.jpg"),(1200,600))
speed_x = 3
speed_y = 3
class GameSprite(sprite.Sprite):
    #создать класс для игровых обьектов
    def __init__(self,player_image,player_x,player_y,player_speed,width,height):
        #функции
        super().__init__()
        self.image = transform.scale(image.load(player_image),(width,height))
        #картинк
        self.speed = player_speed
        #скорость
        self.rect = self.image.get_rect()
        #прямоугольник
        self.rect.x = player_x
        #положение по х
        self.rect.y = player_y
        #положение по у
    def reset(self):
        #функция
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y <350:
            self.rect.y += self.speed

    def updateR(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y >0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y <350:
            self.rect.y += self.speed

rocket1 = Player('11111.jpg', 10,10,25,25,250)
rocket2 = Player('11111.jpg', 1150,200,25,25,250)
ball = GameSprite('mikasa.jpg',105,10,400,100,100)
finish = False
game = True
while game:
    if finish != True:
        window.blit(background,(0,0))




        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > 500:
            speed_y *= -1
        if ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(ball,rocket1):
            speed_x *= -1
        if sprite.collide_rect(ball,rocket2):
            speed_x *= -1
        rocket1.update()
        ball.update()
        rocket2.updateR()
        rocket1.reset()
        rocket2.reset()
        ball.reset()

        if ball.rect.x < 0:
            game = False
        if ball.rect.x > 1200:
            game = False
    for e in event.get():
        if e.type == QUIT:
            game= False
    display.update()
    time.delay(10)
