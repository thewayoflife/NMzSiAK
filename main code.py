import pygame


pygame.init()
screen = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()
BG_COLOR = pygame.Color('aquamarine2')
BLUE = pygame.Color('gray12')
pygame.mixer.music.load('Linkin_Park_ogg.ogg')
pygame.mixer.music.play()

button = pygame.Rect(100, 140, 100, 30) # left, top, width, height
music_paused = False

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(event.pos):
                # Toggle the boolean variable.
                music_paused = not music_paused
                if music_paused:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

    screen.fill(BG_COLOR)
    pygame.draw.rect(screen, BLUE, button) #Draws a rectangle on the given surface, rect(surface, color, rect)
    pygame.display.flip() #Update the full display Surface to the screen
    clock.tick(30) #30-frames per second

#pygame.quit() # ovo može ali i ne mora
