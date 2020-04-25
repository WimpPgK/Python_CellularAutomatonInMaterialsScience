from tkinter import *
import pygame
import random
import os
import Image

'''
root = Tk()
embed = Frame(root, width=640, height=480)
embed.grid(row=0,column=2)
root.update()
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'
pygame.display.init()
screen = pygame.display.set_mode((640,480))
pygame.display.flip()
while True:
    #your code here
    screen.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    pygame.display.flip()
    root.update()
'''

filename = "birds.bmp"
image = Image.open(filename)
coordinate = x,y = 100,140
print (image.getpixel(coordinate))