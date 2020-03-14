import pygame

pygame.mixer.init()

screen = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()
BG_COLOR = pygame.Color('aquamarine2')
GRAY = pygame.Color('gray12')
BLUE = pygame.Color('blue')
sound1 = pygame.mixer.Sound('Linkin_Park_ogg.ogg')
sound2 = pygame.mixer.Sound('Leteci_odred_ogg.ogg')
img1 = pygame.image.load('Leva.png')
img2 = pygame.image.load('Desna.png')
sound1.stop()

button1 = pygame.Rect(28, 230, 110, 30) # left, top, width, height
button2 = pygame.Rect(168, 230, 110, 30) # left, top, width, height

music_sound1 = False
music_sound2 = False


def volume_keys(): # The Key pressed is going to control the sound volume
    keys = pygame.key.get_pressed()       
    
    n1 = sound1.get_volume()
    n2 = sound2.get_volume()
    
    if keys [pygame.K_UP]:
        sound1.set_volume(n1 + 0.059)
        sound2.set_volume(n2 + 0.059)
        print(sound1.get_volume())
        
    if keys [pygame.K_DOWN]:
        sound1.set_volume(n1 - 0.059)
        sound2.set_volume(n2 - 0.059)
        print(sound1.get_volume())


done = False
while not done:
    volume_keys()
    speed_keys()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button1.collidepoint(event.pos): #collidepoint - test if a point is inside the button
                # Toggle the boolean variable.
                music_sound1 = not music_sound1
                if music_sound1:
                    sound2.stop()
                    sound1.play(-1)
                    music_sound2 = False

                else:
                    sound1.stop()
                    #music_sound1 = False

            elif button2.collidepoint(event.pos):
                music_sound2 = not music_sound2
                if music_sound2:
                    sound1.stop()
                    sound2.play(-1)
                    music_sound1 = False
                
                else:
                    sound2.stop()
                    #music_sound2 = False


    pygame.display.set_caption("BRatko") #Change name on top of the window
    screen.fill(BG_COLOR)
    pygame.draw.rect(screen, GRAY, button1) #Draws a rectangle on the given surface, rect(surface, color, rect)
    pygame.draw.rect(screen, BLUE, button2)
    screen.blit(img1, (28, 230, 106, 30)) #Draw one image onto another, blit(string, (left, top, width, height))
    screen.blit(img2, (170, 230, 106, 30))
    pygame.display.flip() #Update the full display Surface to the screen
    clock.tick(30) #30-frames per second

pygame.quit() #Ovo ipak mora. Da deaktivira pygame biblioteku
