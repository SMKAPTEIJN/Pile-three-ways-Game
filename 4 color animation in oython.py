
import pygame
import time
import math
from pygame.locals import *

desiredfps = 60
updaterate = int(1000 / desiredfps)

lasttime = 0
rectx = 0
recty = 0

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.time.set_timer(USEREVENT+1, updaterate)

    def mainloop():
        global lasttime
        global rectx
        global recty
        screen.fill(pygame.Color("white"))
        screen.fill(pygame.Color("red"), pygame.Rect(rectx,recty,20,20))
        screen.fill(pygame.Color("blue"), pygame.Rect(480-rectx,480-recty,20,20))
        screen.fill(pygame.Color("green"), pygame.Rect(rectx,480-recty,20,20))
        screen.fill(pygame.Color("yellow"), pygame.Rect(480-rectx,recty,20,20))
        rectx += 5
        if rectx > 500:
            rectx = 0
            recty += 20
        beforerender = time.clock()
        pygame.display.update()
        afterrender = time.clock()
        renderdelta = afterrender - beforerender
        framedelta = beforerender - lasttime
        lasttime = beforerender
        if renderdelta > 0.01:
            print ("render time: {0}").format(renderdelta)
            print ("frame delta: {0}").format(framedelta)
            print ("-------------------------------------")            
    while(1):
        for event in pygame.event.get():
            if event.type == USEREVENT+1:
                mainloop()
            if event.type == QUIT:
                pygame.quit()
                return 
     
run_game()
