import pygame


pygame.init()
screen = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()
BG_COLOR = pygame.Color('aquamarine2')
GRAY = pygame.Color('gray12')
BLUE = pygame.Color('blue')
sound1 = pygame.mixer.Sound('Linkin_Park_ogg.ogg')
sound2 = pygame.mixer.Sound('Leteci_odred_ogg.ogg')
img1 = pygame.image.load('Leva.png')
img2 = pygame.image.load('Desna.png')
sound1.play()

button1 = pygame.Rect(28, 230, 110, 30) # left, top, width, height
button2 = pygame.Rect(168, 230, 110, 30) # left, top, width, height


music_sound1 = False
music_sound2 = False

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button1.collidepoint(event.pos):
                # Toggle the boolean variable.
                music_sound1 = not music_sound1
                if music_sound1:
                    sound1.stop()
                else:
                    sound2.stop()
                    sound1.play()
            elif button2.collidepoint(event.pos):
                music_sound2 = not music_sound2
                if music_sound2:
                    sound1.stop()
                    sound2.play()
                else:
                    sound2.stop()


    screen.fill(BG_COLOR)
    pygame.draw.rect(screen, GRAY, button1) #Draws a rectangle on the given surface, rect(surface, color, rect)
    pygame.draw.rect(screen, BLUE, button2)
    screen.blit(img1, (28, 230, 106, 30)) #Draw one image onto another, blit(string, (left, top, width, height))
    screen.blit(img2, (170, 230, 106, 30))
    pygame.display.flip() #Update the full display Surface to the screen
    clock.tick(30) #30-frames per second

pygame.quit() #Ovo ipak mora. Da deaktivira pygame bibiloteku
