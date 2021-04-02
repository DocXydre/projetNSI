import pygame
from pygame.locals import *
from tkinter import *
import tkinter as tk 

pygame.init()

continuer = True
choix=0

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

perso1 = pygame.image.load("perso1.png")
perso1 = pygame.transform.scale(perso1, (250, 100))
perso1_rect = perso1.get_rect()
perso1_rect.x, perso1_rect.y = 300, 150

perso4 = pygame.image.load("perso4.png")
perso4 = pygame.transform.scale(perso4, (250, 100))
perso4_rect = perso4.get_rect()
perso4_rect.x, perso4_rect.y = 400, 250

perso2 = pygame.image.load("perso2.png")
perso2 = pygame.transform.scale(perso2, (250, 400))
perso2_rect = perso2.get_rect()
perso2_rect.x, perso2_rect.y = 200, 450

perso3 = pygame.image.load("perso3.png")
perso3 = pygame.transform.scale(perso3, (250, 500))
perso3_rect = perso3.get_rect()
perso3_rect.x, perso3_rect.y = 100, 450

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
    screen.blit(perso1, perso1_rect)
    screen.blit(perso2, perso1_rect)
    screen.blit(perso3, perso1_rect)
    screen.blit(perso4, perso1_rect)
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
            Fenetre.geometry('200x100')
            entry= tk.Entry(Fenetre, textvariable="PSEUDO", width=25,font='Impact 10')
            entry.place(x=10,y=30)
            bouton=Button(Fenetre, text="Valider", command=Fenetre.quit)
            bouton.place(x=30,y=80)
            Fenetre.mainloop()
        if perso1_rect.collidepoint(x,y) and event.type == pygame.MOUSEBUTTONUP:
            Menu=0
            continuer = 0
            choix=1 
        if perso2_rect.collidepoint(x,y) and event.type == pygame.MOUSEBUTTONUP:
            Menu=0
            continuer = 0
            choix=2
        if perso3_rect.collidepoint(x,y) and event.type == pygame.MOUSEBUTTONUP:
            Menu=0
            continuer = 0
            choix=3
        if perso4_rect.collidepoint(x,y) and event.type == pygame.MOUSEBUTTONUP:
            Menu=0
            continuer = 0
            choix=4
    pygame.display.update()

pygame.quit()  