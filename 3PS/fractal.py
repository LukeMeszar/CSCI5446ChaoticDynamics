import pygame, math, random
import numpy as np

pygame.init()
window = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Fractal Tree")
screen = pygame.display.get_surface()
screen.fill((220,220,220))

#shrink1 = 0.7
#shrink2 = 0.65
#shrink1 = 1.5
#shrink2 = 1.5


def drawTree(posX, posY, dirX, dirY, size, angle1, angle2, depth):
    x2 = posX + size * dirX
    y2 = posY + size * dirY
    if depth >= initial_depth*(2/3):
        color1 = 139
        color2 = 69
        color3 = 19
    elif depth >= initial_depth * (1/3):
        color1 = 128
        color2 = 128
        color3 = 0
    else:
        color1 = 34
        color2 = 139
        color3 = 34
    pygame.draw.line(screen, (color1,color2,color3), (posX,posY), (x2, y2),2)
    if depth:
        posX2 = posX + size * dirX
        posY2 = posY + size * dirY
        newSize = size * shrink1
        dirX2 = np.cos(angle1) * dirX + np.sin(angle1) * dirY
        dirY2 = -np.sin(angle1) * dirX + np.cos(angle1) * dirY;
        drawTree(posX2, posY2, dirX2, dirY2, newSize, angle1, angle2, depth - 1)
        newSize = size * shrink2
        dirX2 = np.cos(-angle2) * dirX + np.sin(-angle2) * dirY;
        dirY2 = -np.sin(-angle2) * dirX + np.cos(-angle2) * dirY;
        drawTree(posX2, posY2, dirX2, dirY2, newSize, angle1, angle2, depth - 1)

def drawTreeRandom(posX, posY, dirX, dirY, size, angle1, angle2, shrink1, shrink2, depth):
    x2 = posX + size * dirX
    y2 = posY + size * dirY
    if depth >= initial_depth*(2/3):
        color1 = 139
        color2 = 69
        color3 = 19
    elif depth >= initial_depth * (1/3):
        color1 = 128
        color2 = 128
        color3 = 0
    else:
        color1 = 34
        color2 = 139
        color3 = 34
    pygame.draw.line(screen, (color1,color2,color3), (posX,posY), (x2, y2),2)
    if depth:
        posX2 = posX + size * dirX
        posY2 = posY + size * dirY
        newSize = size * shrink1
        shrink1 = random.uniform(0.51, 0.7)
        dirX2 = np.cos(angle1) * dirX + np.sin(angle1) * dirY
        dirY2 = -np.sin(angle1) * dirX + np.cos(angle1) * dirY;
        angle1 = random.uniform(0, np.pi/2)
        drawTreeRandom(posX2, posY2, dirX2, dirY2, newSize, angle1, angle2, shrink1, shrink2, depth - 1)
        newSize = size * shrink2
        shrink2 = random.uniform(0.51, 0.7)
        dirX2 = np.cos(-angle2) * dirX + np.sin(-angle2) * dirY;
        dirY2 = -np.sin(-angle2) * dirX + np.cos(-angle2) * dirY;
        angle2 = random.uniform(0, np.pi/2)
        drawTreeRandom(posX2, posY2, dirX2, dirY2, newSize, angle1, angle2, shrink1, shrink2, depth - 1)

def drawTreeRandom2(posX, posY, dirX, dirY, size, angle1, angle2, shrink1, shrink2, depth):
    x2 = posX + size * dirX
    y2 = posY + size * dirY
    if depth >= initial_depth*(2/3):
        color1 = 139
        color2 = 69
        color3 = 19
    elif depth >= initial_depth * (1/3):
        color1 = 128
        color2 = 128
        color3 = 0
    else:
        color1 = 34
        color2 = 139
        color3 = 34
    if depth == initial_depth*(1/2):
        shrink1 = random.uniform(0.51, 0.7)
        shrink2 = random.uniform(0.51, 0.7)
        angle1 = random.uniform(0, np.pi/2)
        angle2 = random.uniform(0, np.pi/2)
    pygame.draw.line(screen, (color1,color2,color3), (posX,posY), (x2, y2),2)
    if depth:
        posX2 = posX + size * dirX
        posY2 = posY + size * dirY
        newSize = size * shrink1
        dirX2 = np.cos(angle1) * dirX + np.sin(angle1) * dirY
        dirY2 = -np.sin(angle1) * dirX + np.cos(angle1) * dirY;
        drawTreeRandom(posX2, posY2, dirX2, dirY2, newSize, angle1, angle2, shrink1, shrink2, depth - 1)
        newSize = size * shrink2
        dirX2 = np.cos(-angle2) * dirX + np.sin(-angle2) * dirY;
        dirY2 = -np.sin(-angle2) * dirX + np.cos(-angle2) * dirY;
        drawTreeRandom(posX2, posY2, dirX2, dirY2, newSize, angle1, angle2, shrink1, shrink2, depth - 1)


def input(event):
    if event.type == pygame.QUIT:
        exit(0)

x0 = 500
y0 = 0
dirX0 = 0
dirY0 = 1
size = 300
#angle1 = np.pi/3
#angle2 = 0.698132
#angle1 = np.pi/2
#angle2 = np.pi/2
shrink1 = random.uniform(0.51, 0.7)
shrink2 = random.uniform(0.51, 0.7)
angle1 = random.uniform(0, np.pi/2)
angle2 = random.uniform(0, np.pi/2)
initial_depth = 16
#drawTree(x0, y0, dirX0, dirY0, size, angle1, angle2, initial_depth)
drawTreeRandom(x0, y0, dirX0, dirY0, size, angle1, angle2, shrink1, shrink2, initial_depth)
#drawTreeRandom2(x0, y0, dirX0, dirY0, size, angle1, angle2, shrink1, shrink2, initial_depth)
pygame.display.flip()
while True:
    input(pygame.event.wait())
