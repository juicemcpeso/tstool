#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 13:16:36 2018

@author: ryantmcnally
"""

## TStool 1.1
## 2018-03-19
## - added a save/load feature
## - changed the add cards functions to ask for optional cards once at the
##   beginning of the game

import pandas as pd

## Intro text
print('TSTool 1.1')

## Take input from user if they want to start a new game or load a game

setup_response = input('New game or load game: ')
setup_response = setup_response.lower()

## Logic for starting new or loading a saved table and setting up the 
## 'cards' DataFrame
if setup_response == 'new':
    ## Import the card list as a pandas data frame

    cards = pd.read_csv('tstool_cards.csv')
        
elif setup_response == 'load':
    filename = str(input('Enter the filename of your saved game: '))
    cards = pd.read_csv(filename)
  
## Shifts the index to align with the card number
## Replaces NaN with a whitespace
cards.index += 1
cards = cards.fillna('')

## Ask if the optional cards are in play, set to true/false bool values. If the
## user enters something other than Y/N, the optional cards are set to off.
## Should probably be a function
optional_input = str.upper(input('Optional cards (Y/N): '))
if optional_input == 'Y':
    optional_bool = True
elif optional_input == 'N':
    optional_bool = False
else:
    optional_bool = False

## Function to add early war cards
def addEarly():
    if optional_bool:
        cards.loc[cards.time == 'EARLY', 'location'] = 'DRAW'
    else:
        cards.loc[cards.time == 'EARLY', 'location'] = 'DRAW'
        cards.loc[cards.optional == True, 'location'] = 'BOX'

## Function to add mid war cards
def addMid():
    if optional_bool:
        cards.loc[cards.time == 'MID', 'location'] = 'DRAW'
    else:
        cards.loc[cards.time == 'MID', 'location'] = 'DRAW'
        cards.loc[cards.optional == True, 'location'] = 'BOX'

## Function to add late war cards
def addLate():
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

## Basic stats on the draw pile
def stats():
    
    ## Change in the future to allow you to run stats on any location based off
    ## input, but I don't know how to set a default input for a function
    stats_input = 'DRAW'
    
    ## creates a DataFrame of just the cards in the draw pile for ease of use
    statsFrame = cards.loc[cards.location == stats_input]
    
    ## Shows how many cards are in the draw pile by total ops
    print('Cards by ops: ')
    print(statsFrame['ops'].value_counts(sort=False))
    ## Plots how many cards of each op value remain. I would like it to be 
    ## lowest to highest still (rather than most to least frequent) and have
    ## have the option for a stacked chart (show the type for each)
    ##tempDraw['ops'].value_counts().plot.bar()
    
    ## Shows how many cards are in the draw pile by type
    print('\nCards by type:')
    print(statsFrame['type'].value_counts(sort=False))
    
    ## Plots number of cards by each type of card
    ##tempDraw['type'].value_counts().plot.bar()
    
    ## Table of cards of each op value, sorted by type
    print('\nCards by ops, sorted by type:')
    print(statsFrame.groupby('type')['ops'].value_counts(sort=False))

## Save game function (write to a csv)
def saveGame():
    save_filename = str(input('Enter your filename (.csv): '))
    cards.to_csv(save_filename, index=False)

## ------------------------------------------------------------------------- ##
    
## Start a new game. Should probably be a main, but I ran into issues with 
## setting global variables
if setup_response == 'new':
    addEarly()
        