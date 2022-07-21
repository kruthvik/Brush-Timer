from math import ceil
from playsound import playsound as ps
from time import sleep as s
import pygame
import threading
from math import floor as f
from pygame import mixer

pygame.init() 
pygame.font.init()
mixer.init()

screen = pygame.display.set_mode([500 for i in range(2)])

font = pygame.font.SysFont('Arial', 30)

running = True

g = mixer.Sound("sound.wav")

startingTime = 120
time = startingTime + 1
text = text = font.render(str(time), True, (0, 0, 0))
def timer():
    global time
    global text
    global running
    while time >= 0 and running:
        s(0.01)     
        time -= 0.01
        if (f(time) < 0):
            break
        
        if (f(time) % (startingTime / 4) == 0) and f(time) != startingTime:
            mixer.Sound.play(g)

        text = font.render(str(f(time)), True, (0, 0, 0))
    
    if running:
    
        mixer.Sound.play(g)
        running = False

thread = threading.Thread(target=timer)
thread.start()        

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill((75, 0, 130))

    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(0, 0, 500, (time * (500 / startingTime))))

    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    screen.blit(text, (240, 235))



    pygame.display.flip()


pygame.quit()

