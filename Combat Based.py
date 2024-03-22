# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 17:45:46 2024

@author: Mrang
"""

import random

class Character(object):
        
    def __init__(self):
        super().__init__()
        self.name = "Guy"
        self.health = 15
        self.hitchance = 75
        self.maxdamage = 4
        self.armor = 4
            
    
    def name(self):
       return self.__name 
            
    @name.setter
    def name(self, value):
        self.__name = value
                
    @property 
    def hitpoints(self):
        return self.__hitpoints 
            
    @hitpoints.setter 
    def hitpoints (self, value):
        value = self.testInt (value, 0, 1000, 0)
        self._hitpoints = value 
                
 
    def attack(self,character):
        hit = random.randint(1,100)
        if (hit <= self.hitchance):
            strike = random.randint(1, self.maxdamage)
            if strike > character.armor:
                character.hitpoint -= (strike-character.armor) 
        else: 
           print("Missed Me")
            
    def printStats(self):
        print(
        f"""
        {self.name}
        Health: {self.health}
        Hit Chance: {self.hitchance}%
        Maximum damage: {self.maxdamage}
        Armor: {self.armor}
             """)
    
def main():
    c = Character()
    m = Character()
    c.printStats()
    input("Press Enter to ATTACK. ")
    c.attack(m)

main()
                    
            