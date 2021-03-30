import pygame
from pygame.locals import *
from tkinter import*
import tkinter as tk 

pygame.init()

continuer = True

screen = pygame.display.set_mode((1280, 700))
fond = pygame.image.load("background.png").convert()
screen.blit(fond, (0,0))

new = pygame.image.load("new.png")
new = pygame.transform.scale(new, (250, 100))
new_rect = new.get_rect()
new_rect.x, new_rect.y = 200, 100

play = pygame.image.load("play.jpg")
play = pygame.transform.scale(play, (250, 100))
play_rect = play.get_rect()
play_rect.x, play_rect.y = 200, 300

name = pygame.image.load("name.png")
name = pygame.transform.scale(name, (250, 100))
name_rect = name.get_rect()
name_rect.x, name_rect.y = 200, 300

Quit = pygame.image.load("quit.jpg")
Quit = pygame.transform.scale(Quit, (250, 100))
Quit_rect = Quit.get_rect()
Quit_rect.x, Quit_rect.y = 200, 450

Menu=False

while continuer:
    screen.blit(Quit, Quit_rect)
    screen.blit(play, play_rect)
    screen.blit(new, new_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
            pygame.quit()
        x,y = pygame.mouse.get_pos()
        if play_rect.collidepoint(x,y) and event.type == pygame.MOUSEBUTTONUP:
            print("coucou c'est moi")
        if Quit_rect.collidepoint(x,y) and event.type == pygame.MOUSEBUTTONUP:
            continuer = 0
            Menu=0
        if new_rect.collidepoint(x,y) and event.type == pygame.MOUSEBUTTONUP:
            continuer = False
            Menu = True
    pygame.display.update()

while Menu:
    screen.blit(fond, (0,0))
    screen.blit(Quit, Quit_rect)
    screen.blit(name, name_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Menu = False
            pygame.quit()
        x,y = pygame.mouse.get_pos()
        if Quit_rect.collidepoint(x,y) and event.type == pygame.MOUSEBUTTONUP:
            Menu=0
            continuer = 0
        if name_rect.collidepoint(x,y) and event.type == pygame.MOUSEBUTTONUP:
            Fenetre=Tk()
            Fenetre.title("PSEUDO")
            Fenetre.geometry('600x200')
            entry= tk.Entry(Fenetre, textvariable="vald", width=30,font='Impact 8')
            entry.place()
            Fenetre.mainloop()
    pygame.display.update()

pygame.quit()  