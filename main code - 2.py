import pygame
import wave


pygame.mixer.init()

CHANNELS = 1
swidth = 2
Change_RATE = 1

screen = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()
BG_COLOR = pygame.Color('aquamarine2')
GRAY = pygame.Color('gray12')
BLUE = pygame.Color('blue')
img1 = pygame.image.load('Leva.png')
img2 = pygame.image.load('Desna.png')

button1 = pygame.Rect(28, 230, 110, 30) # left, top, width, height
button2 = pygame.Rect(168, 230, 110, 30) # left, top, width, height

sound1 = wave.open('sound1.wav', 'rb')  #otvara sound.wav za citanje
RATE=sound1.getframerate()*2             
signal = sound1.readframes(-1)

sound2 = wave.open('sound2.wav', 'rb')  #otvara sound.wav za citanje
RATE=sound2.getframerate()*2             
signal = sound2.readframes(-1)


wf1 = wave.open('sound1-new.wav', 'wb')   #otvara sound.wav za pisanje
wf1.setnchannels(CHANNELS)
wf1.setsampwidth(swidth)
wf1.setframerate(RATE*Change_RATE)   #menja framerate (trnutni * promena) ako je promena <1 && >0 onda usporava, ako je >1 onda se ubrzava
wf1.writeframes(signal)
wf1.close()

wf2 = wave.open('sound2-new.wav', 'wb')   #otvara sound.wav za pisanje
wf2.setnchannels(CHANNELS)
wf2.setsampwidth(swidth)
wf2.setframerate(RATE*Change_RATE)   #menja framerate (trnutni * promena) ako je promena <1 && >0 onda usporava, ako je >1 onda se ubrzava
wf2.writeframes(signal)
wf2.close()


song1 = pygame.mixer.Sound('sound1-new.wav')
song2 = pygame.mixer.Sound('sound2-new.wav')
#song1.stop()
#song2.stop()

def volume_keys(): # The Key pressed is going to control the sound volume
    keys = pygame.key.get_pressed()       
    
    n1 = song1.get_volume()
    n2 = song2.get_volume()
    
    if keys [pygame.K_UP]:
        song1.set_volume(n1 + 0.059)
        song2.set_volume(n2 + 0.059)
        print(song1.get_volume())
        
    if keys [pygame.K_DOWN]:
        song1.set_volume(n1 - 0.059)
        song2.set_volume(n2 - 0.059)
        print(song1.get_volume())

music_sound1 = False
music_sound2 = False

done = False
while not done:
    volume_keys()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button1.collidepoint(event.pos): #collidepoint - test if a point is inside the button
                # Toggle the boolean variable.
                music_sound1 = not music_sound1
                if music_sound1:
                    song2.stop()
                    song1.play(-1)
                    music_sound2 = False

                else:
                    song1.stop()
                    #music_sound1 = False

            elif button2.collidepoint(event.pos):
                music_sound2 = not music_sound2
                if music_sound2:
                    song1.stop()
                    song2.play(-1)
                    music_sound1 = False
                
                else:
                    song2.stop()
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
