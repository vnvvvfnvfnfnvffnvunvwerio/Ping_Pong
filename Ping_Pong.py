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
        if keys_pressed[K_RIGHT] and self.rect.x < 595:
            self.rect.x += self.speed
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
