import pygame as pg
import random
import time
window_size = (1280,640)

class GopherSprite(pg.sprite.Sprite):
    def __init__(self,x,y,z):
        super().__init__()
        self.images = []
        for i in range(0,16):
            filename = '/Users/tinypatrice/Desktop/gophers/鼠%0d.png' % i
            self.images.append(pg.transform.smoothscale
                               (pg.image.load(filename), (134,123))) #原尺寸134*123/0.7倍 94*86/

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.stop_sign = False
        self.num = z
        
    def update(self):
        if self.stop_sign == False:
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
                self.stop_sign = True
        self.image = self.images[self.index]
        
'''
     (460,)(640,)(820,)
(,180)  1    2     3
(,320)  4    5     6
(,460)  7    8     9

'''


gopher1 = GopherSprite(460,180,1)
gopher2 = GopherSprite(640,180,2)
gopher3 = GopherSprite(820,180,3)
gopher4 = GopherSprite(460,320,4)
gopher5 = GopherSprite(640,320,5)
gopher6 = GopherSprite(820,320,6)
gopher7 = GopherSprite(460,460,7)
gopher8 = GopherSprite(640,460,8)
gopher9 = GopherSprite(820,460,9)
'''gophers = [gopher1,gopher2,gopher3,
           gopher4,gopher5,gopher6,
           gopher7,gopher8,gopher9]'''
gophers= pg.sprite.Group(gopher1,gopher2,gopher3,
                         gopher4,gopher5,gopher6,
                         gopher7,gopher8,gopher9)#小群組
Gophers= pg.sprite.OrderedUpdates(gophers)#大群組


#stop_sign=False
#pg.time.set_timer(pg.USEREVENT, 500)0.5秒


pg.init()


screen = pg.display.set_mode(window_size)
screen.fill((255,255,255))
pg.display.set_caption('第一支pygame程式')
bg_image = pg.transform.scale(
        pg.image.load('/Users/tinypatrice/Desktop/gophers/草.jpg'), (window_size[0], window_size[1]))


done = False
while not done:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
            
        if event.type == pg.USEREVENT:
            new_gopher = GopherSprite()
            gophers.add(new_gopher) #小群組
            Gophers=pg.sprite.OrderedUpdates(gophers)#大群組

    screen.blit(bg_image, [0,0]

                
    Gophers.draw(screen) 
    pg.display.update()
    

pg.quit()
