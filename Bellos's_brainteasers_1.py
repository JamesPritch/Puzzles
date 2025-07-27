#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 13:23:11 2025

@author: jpritch
"""

# Andrew and Barbara play a game with 15 boxes arranged in a 3x5 grid 
# (3 columns, 5 rows). Prizes are put in two randomly chosen boxes. Andrew 
# searches by row, Barbara by column. They open their boxes together each turn.
# Who is more likely to win by finding a prize first?

import random

Andrew_wins, Barbara_wins = 0, 0

# Number of experimental repeats
N_iter = 100000

def Andrewstep(i):
    return i + 1

def Barbarastep(i):
    if i > 10:
        return i - 9
    return i + 5

for N in range(0,N_iter):
    Andrew, Barbara = 1, 1
    # Randomise the prizes
    prize_1, prize_2 = random.randint(1,15), random.randint(1,15)
    # Ensure two unique prizes
    while prize_1 == prize_2:
        prize_2 = random.randint(1,15)
        
    for i in range(0,15):
        # Draw so no win
        if (Andrew == prize_1 and Barbara == prize_1) or (Andrew == prize_2 and Barbara == prize_2) or (Andrew == prize_1 and Barbara == prize_2) or (Andrew == prize_2 and Barbara == prize_1):
            break
        # Andrew wins
        elif Andrew == prize_1 or Andrew == prize_2:
            Andrew_wins += 1
            break
        #Barbara wins
        elif Barbara == prize_1 or Barbara == prize_2:
            Barbara_wins += 1
            break
        
        # Andrew and Barbara look in next box
        Barbara = Barbarastep(Barbara)
        Andrew = Andrewstep(Andrew)

print("Andrew wins:", str(Andrew_wins) + ", Barbara wins:", str(Barbara_wins) + ".")
print("Andrew win ratio:", str(Andrew_wins/N_iter) + ", Barbara win ratio:", str(Barbara_wins/N_iter) + ".")

# Analysis: Andrew, since he opens one more box on turns 4, 5, and 10. All 
# other turns are drawn.
# Direct simulation: likelyhood of Andrew winning is ≈ 0.41, likelyhood of
# Barbara winning is ≈ 0.37.