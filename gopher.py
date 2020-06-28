import pygame as pg
import random
import time
window_size = (1280,640)


class Point(pg.sprite.Sprite):
   def __init__(self, x, y):
       super().__init__()
       self.rect = pg.Rect(x, y, x + 2, y + 2)
       

class GopherSprite(pg.sprite.Sprite):
    def __init__(self,x,y):
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
        self.create_time = time.time()
        self.killornot = False
    
        
    def update(self):
        #if self.killornot:
            #self.image = self.images[self.index]
            #self.image.set_alpha(100)
            #self.image.set_alpha(50)
            #self.image.set_alpha(100)
            #self.image.set_alpha(50)
            #self.kill()
            #kill_time = time.time() - self.create_time
            #print("kill_time:",kill_time)
        
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0 
            self.kill()
            dead_time=time.time() - self.create_time
            print ("dead_time:",dead_time)
        self.image = self.images[self.index]

        p1,p2,p3=pg.mouse.get_pressed()
        pos = pg.mouse.get_pos()
        collisions = pg.sprite.spritecollideany(Point(pos[0], pos[1]), gophers)
        if collisions:
            if p1== True:
                self.kill()
                kill_time = time.time() - self.create_time
                print("kill_time:",kill_time)
                




'''
     (460,)(640,)(820,)
(,180)  1    2     3
(,320)  4    5     6
(,460)  7    8     9

'''

'''
gopher1 = GopherSprite(460,180)
gopher2 = GopherSprite(640,180)
gopher3 = GopherSprite(820,180)
gopher4 = GopherSprite(460,320)
gopher5 = GopherSprite(640,320)
gopher6 = GopherSprite(820,320)
gopher7 = GopherSprite(460,460)
gopher8 = GopherSprite(640,460)
gopher9 = GopherSprite(820,460)
gophers = [gopher1,gopher2,gopher3,
           gopher4,gopher5,gopher6,
           gopher7,gopher8,gopher9]'''
gophers= pg.sprite.Group()#小群組
Gophers= pg.sprite.OrderedUpdates(gophers)#大群組


#stop_sign=False
#pg.time.set_timer(pg.USEREVENT, 500)0.5秒


pg.init()


screen = pg.display.set_mode(window_size)
screen.fill((255,255,255))
pg.display.set_caption('gopher')
bg_image = pg.transform.scale(
        pg.image.load('/Users/tinypatrice/Desktop/gophers/草.jpg'), (window_size[0], window_size[1]))

hole_image = pg.image.load('/Users/tinypatrice/Desktop/gophers/鼠0.png')

clock = pg.time.Clock()
pg.time.set_timer(pg.USEREVENT, 1000)

done = False
while not done:
    clock.tick(60)
    for event in pg.event.get():

        if event.type == pg.QUIT:
            done = True


        if event.type == pg.USEREVENT:
            x_x=[460,640,820]
            y_y=[180,320,460]
            new_gopher = GopherSprite(x_x[random.randint(0,2)],y_y[random.randint(0,2)])
            if not pg.sprite.spritecollideany(new_gopher, gophers):
                gophers.add(new_gopher) #小群組
                Gophers=pg.sprite.OrderedUpdates(gophers)#大群組
            
        
        
        

    screen.blit(bg_image, [0,0])
    screen.blit(hole_image,[393,118.5]) #1
    screen.blit(hole_image,[573,118.5]) #2
    screen.blit(hole_image,[753,118.5]) #3
    screen.blit(hole_image,[393,258.5]) #4
    screen.blit(hole_image,[573,258.5]) #5
    screen.blit(hole_image,[753,258.5]) #6
    screen.blit(hole_image,[393,398.5]) #7
    screen.blit(hole_image,[573,398.5]) #8
    screen.blit(hole_image,[753,398.5]) #9

    gophers.update()
    Gophers.draw(screen) 
    pg.display.update()
    
    

pg.quit()

'''
     (393,)(573,)(753,)
(,118.5)  1    2     3
(,258.5)  4    5     6
(,398.5)  7    8     9

'''
