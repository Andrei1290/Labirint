#створи гру "Лабіринт"!
from pygame import *
import pygame



class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        #print(keys)
        if keys[K_LEFT] and self.rect.x:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.x:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.x:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <= 370:
            self.direction = "right"
        if self.rect.x >= 600:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface([self.width, self.height])
        self.image.fill([color_1, color_2, color_3])
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



window = display.set_mode((700,500))
display.set_caption("Лабіринт")
background = transform.scale(image.load("background.jpg"),(700,500))


game = True
clock = time.Clock()
FPS = 60


player=Player("hero.png",20,400,5)
cyborg=Enemy("enemy.png",600,50,2)
treasure=GameSprite("treasure.png",600,160,0)

w1 =  Wall(190, 254, 94, 120,20,460,20)#
w2 =  Wall(190, 254, 94, 100,380,20,100)#
w3 =  Wall(190, 254, 94, 440,140,20,340)#
w4 =  Wall(190, 254, 94, 560,140,20,120)#
w5 =  Wall(190, 254, 94, 220,140,20,240)#
w6 =  Wall(190, 254, 94, 330,40,20,100)#
w7 =  Wall(190, 254, 94, 0,260,120,20)#
w8 =  Wall(190, 254, 94, 120,140,100,20)#
w9 =  Wall(190, 254, 94, 240,360,100,20)#
w10 =  Wall(190, 254, 94, 460,360,120,20)#
w11 =  Wall(190, 254, 94, 580,240,120,20)#
w12 =  Wall(190, 254, 94, 240,240,200,20)#
w13 =  Wall(190, 254, 94, 100,480,360,20)#



finish = False

font.init()
font = font.Font(None, 70)
win = font.render("YOU WIN!", True, (255, 215, 0))
lose = font.render("YOU LOSE!", True, (180, 0, 0))

mixer.init()
mixer.music.load("music.ogg")
mixer.music.play()
pygame.mixer.music.set_volume(0.2)

money = mixer.Sound("money.ogg")
kick = mixer.Sound("kick.ogg")


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish!=True:
        window.blit(background,(0,0))
        player.reset()
        player.update()
        cyborg.reset()
        cyborg.update()
        treasure.reset()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
        w10.draw_wall()
        w11.draw_wall()
        w12.draw_wall()
        w13.draw_wall()

        if (sprite.collide_rect(player, w1)
            or sprite.collide_rect(player, w2)
            or sprite.collide_rect(player, w3)
            or sprite.collide_rect(player, w4)
            or sprite.collide_rect(player, w5)
            or sprite.collide_rect(player, w6)
            or sprite.collide_rect(player, w7)
            or sprite.collide_rect(player, w8)
            or sprite.collide_rect(player, w9)
            or sprite.collide_rect(player, w10)
            or sprite.collide_rect(player, w11)
            or sprite.collide_rect(player, w12)
            or sprite.collide_rect(player, w13)):
            player.rect.x=20
            player.rect.y=400

        #Програш
        if sprite.collide_rect(player, cyborg):
            window.blit(lose, (200, 200))
            player.rect.x=50
            player.rect.y=400
            kick.play()
            finish = True

        #Виграш
        if sprite.collide_rect(player, treasure):
            window.blit(win, (200, 200))
            player.rect.x=50
            player.rect.y=400
            money.play()
            finish = True
        

    clock.tick(FPS)
    display.update()