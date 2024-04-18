from pygame import *
mixer.init()
udar = mixer.Sound('udar.ogg')
font.init()

speed_x = 3
speed_y = 3

font1 = font.SysFont('Times New Roman', 35)
lose1 = font1.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font1.render('PLAYER 2 LOSE!', True, (180, 0, 0))



class GameSprite(sprite.Sprite):
    def __init__(self,im,sp,x,y,w = 80,h=100):
        super().__init__()
        self.image = transform.scale(image.load(im),(w,h))
        self.speed = sp
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))




class Player(GameSprite):
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        elif keys[K_s] and self.rect.y <300:
            self.rect.y += self.speed




    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        elif keys[K_DOWN] and self.rect.y <300:
            self.rect.y += self.speed

game=True
bg = transform.scale(image.load('table.png'),(700,500))
playerone = Player('rocketkaone.png',5,0,5,50,200)
playertwo = Player('rocketkatwo.png',5,650,5,50,200)
ball = Player('myach.png',5,350,250,50,50)
window = display.set_mode((700,500))
window.blit(bg,(0,0))
clock = time.Clock()
finish = False
while game:
    window.blit(bg,(0,0))
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > 500-50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(playerone, ball) or sprite.collide_rect(playertwo, ball):
            udar.play()
            speed_x *= -1
        if ball.rect.x < 0:
            window.blit(lose1, (200, 200))
        if ball.rect.x > 700:
            window.blit(lose2, (200, 200))
        

        ball.reset()
        playerone.reset()
        playertwo.reset()
        playerone.update_right()
        playertwo.update_left()
    for e in event.get():
        if e.type == QUIT:
            game =False
    clock.tick(60)
    display.update()