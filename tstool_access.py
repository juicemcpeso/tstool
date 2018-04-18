#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 20:29:54 2018

@author: ryantmcnally
"""

## TStool influence/access tracker

import pandas as pd

## Intro text
print('TSTool access/influence module')

## Take input from user if they want to start a new game or load a game

setup_response = input('New game or load game: ')
setup_response = setup_response.lower()

## Logic for starting new or loading a saved table and setting up the
## 'cards' DataFrame
if setup_response == 'new':
    ## Import the country list as a pandas data frame

    countries = pd.read_csv('tstool_countrylist.csv')

elif setup_response == 'load':
    filename = str(input('Enter the filename of your saved game: '))
    countries = pd.read_csv(filename)

## Changes NaN to whitespace
countries = countries.fillna('')

## Import the scoring csv
scoring_table = pd.read_csv('tstool_scoring.csv')

## Changes the influence in a country
def change(country_name, a_inf, r_inf):
    ## Logic to check if the country name inputted is valid. Takes the country
    ## name and if it's a full name, runs two statements to update the america
    ## influence and then the russia influence based off of the provided
    ##numbers
    if any(countries.name == country_name):
        countries.loc[countries.name == country_name, 'A_influence'] = a_inf
        countries.loc[countries.name == country_name, 'R_influence'] = r_inf
        temp_stability = countries.loc[countries.name == country_name,
                                       'stability'].values[0]

        ## Statement to determine control of recently changed country
        if (a_inf - r_inf) >= temp_stability:
            countries.loc[countries.name == country_name, 'controlled'] = 'A'
        elif (r_inf - a_inf) >= temp_stability:
            countries.loc[countries.name == country_name, 'controlled'] = 'R'
        else:
            countries.loc[countries.name == country_name, 'controlled'] = ''

    elif any(countries.nickname == country_name):
        countries.loc[countries.nickname == country_name, 'A_influence'] = a_inf
        countries.loc[countries.nickname == country_name, 'R_influence'] = r_inf
        temp_stability = countries.loc[countries.nickname == country_name,
                                       'stability'].values[0]

        ## Statement to determine control of recently changed country
        if (a_inf - r_inf) >= temp_stability:
            countries.loc[countries.nickname == country_name, 'controlled'] = 'A'
        elif (r_inf - a_inf) >= temp_stability:
            countries.loc[countries.nickname == country_name, 'controlled'] = 'R'
        else:
            countries.loc[countries.nickname == country_name, 'controlled'] = ''

    else:
        print('Enter the full country name or the first four letters of the '
              'name (all lowercase). Australia is koala.')


## Shows the influence in the specified country
def show(country_name):

    printFormat = ['name','battleground','stability', 'A_influence',
                   'R_influence', 'controlled']

    if any(countries.name == country_name):
        temp_frame = countries.loc[countries.name == country_name]
        print(temp_frame[printFormat])

    elif any(countries.nickname == country_name):
        temp_frame = countries.loc[countries.nickname == country_name]
        print(temp_frame[printFormat])

    elif any(countries.region == country_name):
        temp_frame = countries.loc[countries.region == country_name]
        print(temp_frame[printFormat])

    else:
        print('Enter the full region name with caps (South America), '
              'full country name, or the first four letters of the name '
              '(all lowercase). Australia is koala.')

## Shows all the cards
def showCountries():
    printFormat = ['name','battleground','stability', 'A_influence',
                   'R_influence', 'controlled']
    print(countries[printFormat])

## Scores each of the regions, not southeast asia
def score(region_name):
    
    if region_name == 'Southeast Asia':
        ## Create a subframe for all the southeast asia countries, followed
        ## by subframes for the Russian and American players
        region_fr = countries.loc[countries.subregion == region_name]
        region_fr_bat = region_fr.loc[region_fr.battleground == True]
        
        R_frame = region_fr.loc[region_fr.controlled == 'R']
        R_control_count = (region_fr.controlled == 'R').sum()
        R_control_count_bat = (region_fr_bat.controlled == 'R').sum()
    
        A_frame = region_fr.loc[region_fr.controlled == 'A']
        A_control_count = (region_fr.controlled == 'A').sum()
        A_control_count_bat = (region_fr_bat.controlled == 'A').sum()
        
        ## Set the scores. SE Asia scoring is one point for each controlled
        ## country in the region and an extra point for controlling Thailand.
        ## Since Thailand is the only battleground in this subregion, I just
        ## reused the count number of battlegrounds/non-battlegrounds code.
        R_score = R_control_count + R_control_count_bat
        A_score = A_control_count + A_control_count_bat
        
        print('Russia scores', R_score)
        print('America scores', A_score)
        
    else:
        ## Score the specified region
        region_fr = countries.loc[countries.region == region_name]
        region_fr_bat = region_fr.loc[region_fr.battleground == True]
    
        ## Count how many battlegrounds there are in the region
        number_bat = len(region_fr_bat)
    
        ## Counts of controlled battlegrounds and non battlegrounds in the region
        R_frame = region_fr.loc[region_fr.controlled == 'R']
        R_control_count = (region_fr.controlled == 'R').sum()
        R_control_count_bat = (region_fr_bat.controlled == 'R').sum()
    
        A_frame = region_fr.loc[region_fr.controlled == 'A']
        A_control_count = (region_fr.controlled == 'A').sum()
        A_control_count_bat = (region_fr_bat.controlled == 'A').sum()
    
        ## Create variables for the type of score (presence, domination, control)
        R_score_type = 'nothing'
        R_score = 0
        A_score_type = 'nothing'
        A_score = 0

        ## Determine presence for Russia
        if R_control_count > 0:
            R_score_type = 'presence'
    
        ## Determine presence for America
        if A_control_count > 0:
            A_score_type = 'presence'
    
        ## Determine domination for Russia. First statement makes sure Russia has
        ## more battlegrounds than America. Second statement makes sure that Russia
        ## controls more countries in the region than America. Third statement
        ## makes sure Russia has at least one nonbattleground (total controlled
        ## minus controlled battlegrounds needs to be more than 0). Fourth
        ## statment requires at least one battleground to be controlled
        if ((R_control_count_bat > A_control_count_bat) and
            (R_control_count > A_control_count) and
            (R_control_count > R_control_count_bat) and
            (R_control_count_bat != 0)):
            R_score_type = 'domination'
    
        elif ((A_control_count_bat > R_control_count_bat) and
            (A_control_count > R_control_count) and
            (A_control_count > A_control_count_bat) and
            (A_control_count_bat != 0)):
            A_score_type = 'domination'
    
        ## Determine control. Player must have all the battlegrounds controlled
        ## and more counties controled than their opponent
        if ((R_control_count_bat == number_bat) and
            (R_control_count > A_control_count)):
            R_score_type = 'control'
    
        elif ((A_control_count_bat == number_bat) and
            (A_control_count > R_control_count)):
            A_score_type = 'control'
    
        ## Update the score
        R_score = scoring_table.loc[scoring_table.region == region_name,
                                           R_score_type].values[0]
        A_score = scoring_table.loc[scoring_table.region == region_name,
                                           A_score_type].values[0]
    
        ## Add battlegrounds to the score
        R_score = R_score + R_control_count_bat
        A_score = A_score + A_control_count_bat
    
        ## Add adjacency to the score. Sum all the items in the frame of
        ## controlled countries that have the opponent's adjacency
    
        R_adjacency = (R_frame.adjacent == 'A').sum()
        R_score = R_score + R_adjacency
    
        A_adjacency = (A_frame.adjacent == 'R').sum()
        A_score = A_score + A_adjacency
    
        ## Print the scores
        print('Russia scores',  R_score_type, 'for', R_score)
        print('America scores', A_score_type, 'for', A_score)
    

## Save game function (write to a csv)
def saveGame():
    save_filename = str(input('Enter your filename (.csv): '))
    countries.to_csv(save_filename, index=False)


## ------------------------------------------------------------------------- ##

## Start a new game. Should probably be a main, but I ran into issues with
## setting global variables
if setup_response == 'new':

    ## Setup Russia
    change('Syria', 0, 1)
    change('Iraq', 0, 1)
    change('N. Korea', 0, 3)
    change('E. Germany', 0, 3)
    change('Finland', 0, 1)

    ## Setup America
    change('Iran', 1, 0)
    change('Israel', 1, 0)
    change('Japan', 1, 0)
    change('Australia', 4, 0)
    change('Philippines', 1, 0)
    change('S. Korea', 1, 0)
    change('Panama', 1, 0)
    change('South Africa', 1, 0)
    change('UK', 5, 0)
