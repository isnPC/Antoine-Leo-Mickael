#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 20:29:05 2020

@author: manu
"""
import pygame


pygame.init()
fenetre = pygame.display.set_mode((640, 480))
fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond, (0,0))
pygame.display.flip()
continuer = 1
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
pygame.quit()
