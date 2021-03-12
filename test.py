import pygame
from pygame.locals import *

pygame.init()

continuer = True

screen = pygame.display.set_mode((1280, 780))
fond = pygame.image.load("background.png").convert()
screen.blit(fond, (0,0))

play = pygame.image.load("play.jpg")
play = pygame.transform.scale(play, (250, 100))
play_rect = play.get_rect()
play_rect.x, play_rect.y = 100, 400

Quit = pygame.image.load("quit.jpg")
Quit = pygame.transform.scale(Quit, (250, 100))
Quit_rect = Quit.get_rect()
Quit_rect.x, Quit_rect.y = 100, 550

option = pygame.image.load("option.png")
option = pygame.transform.scale(option, (50, 50))
option_rect = option.get_rect()
option_rect.x, option_rect.y = 1180, 50

while continuer:
    
    
    screen.blit(play, play_rect)
        
    screen.blit(Quit, Quit_rect)

    screen.blit(option, option_rect)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
            pygame.quit()
        x,y = pygame.mouse.get_pos()
        if play_rect.collidepoint(x,y) and event.type == pygame.MOUSEBUTTONUP:
            print("coucou c'est moi")
        if Quit_rect.collidepoint(x,y) and event.type == pygame.MOUSEBUTTONUP:
            pygame.quit()
        if option_rect.collidepoint(x,y) and event.type == pygame.MOUSEBUTTONUP:
            print("coucou c'est elle")
    pygame.display.update()