import pygame
import wave


pygame.mixer.init()

CHANNELS = 1
swidth = 2
Change_RATE = 2

spf = wave.open('sound.wav', 'rb')  #otvara sound.wav za citanje
RATE=spf.getframerate()             
signal = spf.readframes(-1)

wf = wave.open('sound.wav', 'wb')   #otvara sound.wav za pisanje
wf.setnchannels(CHANNELS)
wf.setsampwidth(swidth)
wf.setframerate(RATE*Change_RATE)   #menja framerate (trnutni * promena) ako je promena <1 && >0 onda usporava, ako je >1 onda se ubrzava
wf.writeframes(signal)
wf.close()

song = pygame.mixer.Sound('sound.wav')
clock = pygame.time.Clock()
song.play()
while True:
    clock.tick(60)