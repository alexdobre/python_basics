import math
import pygame
from time import sleep
from random import randint

pygame.init()

font = pygame.font.Font('freesansbold.ttf', 200)
background_colour = (255,255,255)
(width, height) = (800, 800)
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('JOC')
screen.fill(background_colour)
pygame.display.flip()
bg = (40,24,20)

ptinta=()
d=150
r=350
stanga = False
dreapta = False
l=0

def move_coords(angle, radius, coords):
    theta = math.radians(angle)
    return coords[0] + radius * math.cos(theta), coords[1] + radius * math.sin(theta)

cords = (width/2-15,height/2-15)
center = (width/2,height/2)
pos = move_coords(randint(1,360), r - d+1, center)
scor = 0

running = True
k=0
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                stanga = True
            if event.key == pygame.K_RIGHT:
                dreapta= True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                stanga = False
            if event.key == pygame.K_RIGHT:
                dreapta = False
    if stanga == True:
        l=l-2
    if dreapta == True:
        l=l+2
    liniec = [0,0]
    liniec[0] = cords
    liniec[1] = cords
    if k>40 :
        liniec[0]= move_coords(l,r-d,center)
        liniec[1] = move_coords(l, r, cords)
        x = list(liniec[1])
        x[0] = x[0] + 15
        x[1] = x[1] + 15
        liniec[1] = tuple(x)
    if k==50:
        k=0
    if ((list(pos)[0] >= list(liniec[0])[0] - 20) and (list(pos)[0] <= list(liniec[0])[0] + 20) and (list(pos)[1] >= list(liniec[0])[1] - 20) and (list(pos)[1] <= list(liniec[0])[1] + 20)):
        pos = move_coords(randint(1,360), r - d+1, center)
        scor = scor + 1
    screen.fill(bg)
    text = font.render(str(scor), True, (200,200,200))
    textRect = text.get_rect()
    textRect.center = (width/2,100)
    screen.blit(text, textRect)
    pygame.draw.circle(screen, (0, 0, 255), pos, 10)
    pygame.draw.line(screen, (0, 255, 0), liniec[0], liniec[1])
    pygame.draw.circle(screen, (255, 0, 0),center, r-d)
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(*move_coords(l,r,cords), 30, 30))
    pygame.display.flip()
    k=k+1
    sleep(0.02)