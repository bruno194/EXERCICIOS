import pygame
pygame.mixer.init()
pygame.mixer.music.load('fernandoesorocaba-19-seu-policia-9d7e19ae.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()): pass
