import pygame, math
import numpy as np

pygame.init()
window = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Fractal Tree")
screen = pygame.display.get_surface()
window.fill((0,0,0))

shrink = 0.6


def drawTree(posX, posY, dirX, dirY, size, angle, depth):
    x2 = posX + size * dirX
    y2 = posY + size * dirY
    pygame.draw.line(screen, (255,255,255), (posX,posY), (x2, y2),2)
    if depth:
        posX2 = posX + size * dirX
        posY2 = posY + size * dirY
        newSize = size * 0.6
        dirX2 = np.cos(angle) * dirX + np.sin(angle) * dirY
        dirY2 = -np.sin(angle) * dirX + np.cos(angle) * dirY;
        drawTree(posX2, posY2, dirX2, dirY2, newSize, angle, depth - 1)
        dirX2 = np.cos(-angle) * dirX + np.sin(-angle) * dirY;
        dirY2 = -np.sin(-angle) * dirX + np.cos(-angle) * dirY;
        drawTree(posX2, posY2, dirX2, dirY2, newSize, angle, depth - 1)
    #if depth:

#        x2 = x1 + int(math.cos(math.radians(angle)) * depth * 10.0)
#        y2 = y1 + int(math.sin(math.radians(angle)) * depth * 10.0)
#        pygame.draw.line(screen, (255,255,255), (x1, y1), (x2, y2), 2)
#        drawTree(x2, y2, angle, depth - 1)
#        drawTree(x2, y2, angle, depth - 1)


def input(event):
    if event.type == pygame.QUIT:
        exit(0)

x0 = 500
y0 = 0
dirX0 = 0
dirY0 = 1
size = 500
angle = np.pi/2
depth = 10
drawTree(x0, y0, dirX0, dirY0, size, angle, depth)
pygame.display.flip()
while True:
    input(pygame.event.wait())
