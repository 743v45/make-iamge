#coding:utf-8
import pygame
from pygame.locals import *
from sys import exit
SCREEN_SIZE = 1920,1080

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE,0,32)
WHITE = (255,255,255)
GREY = (96,96,96)

x,y = SCREEN_SIZE
for i in range(0,x):
    for j in range(0,y):
        if (i/3+j/3) % 2 == 1:  # 一个像素太小了.只能把3*3当作一个像素处理了
            screen.set_at((i,j),WHITE)
        else:
            screen.set_at((i,j),GREY)

pygame.image.save(screen,'image.png')
