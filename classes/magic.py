# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 00:37:47 2018

@author: Fran
"""
import random

class Spell:
    def __init__(self, name, cost, dmg, type):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type = type
        
    def generate_damage(self):
        low = self.dmg - 15
        high = self.dmg + 15
        return random.randrange(low,high)