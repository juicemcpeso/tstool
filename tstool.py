#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 13:16:36 2018

@author: ryantmcnally
"""

import pandas as pd

## Import the card list as a pandas data frame
## Shifts the index to align with the card number
## Replaces NaN with a whitespace
cards = pd.read_csv('tstool_cards.csv')
cards.index += 1
cards = cards.fillna('')

## Intro text
print('TSTool 1.0')
print('To start game, run startGame() function')
print('startGame takes True or False as inputs for the optional cards \n')


## Function to start the game. Takes "True or False"
def startGame(optional_bool):
    if optional_bool:
        cards.loc[cards.time == 'EARLY', 'location'] = 'DRAW'
    else:
        cards.loc[cards.time == 'EARLY', 'location'] = 'DRAW'
        cards.loc[cards.optional == True, 'location'] = 'BOX'

## Function to add mid war cards
def addMid(optional_bool):
    if optional_bool:
        cards.loc[cards.time == 'MID', 'location'] = 'DRAW'
    else:
        cards.loc[cards.time == 'MID', 'location'] = 'DRAW'
        cards.loc[cards.optional == True, 'location'] = 'BOX'

## Function to add late war cards
def addLate(optional_bool):
    if optional_bool:
        cards.loc[cards.time == 'LATE', 'location'] = 'DRAW'
    else:
        cards.loc[cards.time == 'LATE', 'location'] = 'DRAW'
        cards.loc[cards.optional == True, 'location'] = 'BOX'

## Shuffle takes cards from the discard and puts them in the draw
def shuffle():
    cards.loc[cards.location == 'DISCARD', 'location'] = 'DRAW'


## Functions to move location of cards
## Locations:
## BOX
## DRAW
## DISCARD
## REMOVED
## MY_HAND
## ENEMY_HAND

def move(card_number, card_location):
    if (    card_location == 'BOX' or card_location == 'DRAW' or 
            card_location == 'DISCARD' or card_location == 'REMOVED' or 
            card_location == 'MY_HAND' or card_location == 'ENEMY_HAND'):
        
        cards.loc[cards.index == card_number, 'location'] = card_location
    else:
        print('Enter location of BOX, DRAW, DISCARD, ' 
              'REMOVED, MY_HAND, or ENEMY_HAND')


def discard(card_number):
    cards.loc[cards.index == card_number, 'location'] = 'DISCARD'

def remove(card_number):
    cards.loc[cards.index == card_number, 'location'] = 'REMOVED'
    
def myHand(card_number):
    cards.loc[cards.index == card_number, 'location'] = 'MY_HAND'

def enemyHand(card_number):
    cards.loc[cards.index == card_number, 'location'] = 'ENEMY_HAND'

def moveLots(location_from, location_to):
    cards.loc[cards.location == location_from, 'location'] = location_to


## Print the discard/draw/removed/hands   
    
def showAll():
    print(cards.loc[cards.location != 'BOX'])
    
def showDiscard():
    print(cards.loc[cards.location == 'DISCARD'])
    
def showDraw():
    print(cards.loc[cards.location == 'DRAW'])
    
def showRemoved():
    print(cards.loc[cards.location == 'REMOVED'])
    
def showMyHand():
    print(cards.loc[cards.location == 'MY_HAND'])
    
def showEnemyHand():
    print(cards.loc[cards.location == 'ENEMY_HAND'])

## Basic stats
def drawStats():
    
    tempDraw = cards.loc[cards.location == 'DRAW']
    tempDraw.plot.hist(bins=5)
       