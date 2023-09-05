# Faça um programa em Python que abra e reproduza o audio de um arquivo MP3

# inicializando o mixer Pygame
import pygame

pygame.mixer.init()

# Inicializando o pygame
pygame.init()
pygame.mixer.music.load(input('Digite o nome da musica: '))
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()
