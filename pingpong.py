from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        # rect
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y)) 


class Player(GameSprite):
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height - 150:
            self.rect.y += self.speed

    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_height - 150:
            self.rect.y += self.speed



back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

game = True 
finish = False
clock = time.Clock()
FPS = 60


racket1 = Player('racket.png', 30, 200, 4, 50, 150)
racket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE', True, (180, 0, 0))


speedx = 3
speedy = 3


while game:
    for e  in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()

         if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speedx *= -1

        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speedy *= -1

        if ball.rect.x < - 50:
            finish = True
            window.blit(lose1, (200,200))

        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200,200))

        racket1.reset()
        racket2.reset()
        ball.reset()


    display.update()
    clock.tick(FPS)


