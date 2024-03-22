# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 17:46:21 2024

@author: rjmle
"""


import random

class Character(object):
        
    def __init__(self,name = "guy", hitPoints=0, hitChance=0, maxDamage=0, armor=0):
        super().__init__()
        self.name = name
        self.hitPoints = hitPoints
        self.hitChance = hitChance
        self.maxDamage = maxDamage
        self.armor = armor
            
    @property
    def name(self):
       return self.__name 
            
    @name.setter
    def name(self, value):
        self.__name = value
                
    @property 
    def hitPoints(self):
        return self.__hitPoints
            
    @hitPoints.setter 
    def hitPoints (self, value):
        value = self.testInt (value, 0, 1000, 0)
        self.__hitPoints = value 
        
    def testInt(self, value, min = 0, max = 100, default = 0):
        """ takes in value 
            checks to see if it is an int between
            min and max.  If it is not a legal value
            set it to default """
    
        out = default
    
        if type(value) == int:
            if value >= min:
                if value <= max:
                    out = value 
                else:
                    print("Too large")
            else:
                print("Too small")
        else:
            print("Must be an int")
    
        return out       
                
 
    def attack(self,character):
        hit = random.randint(1,100)
        if (hit <= self.hitChance):
            strike = random.randint(1, self.maxDamage)
            if strike > character.armor:
                character.hitPoints -= (strike-character.armor) 
        else: 
           print("Missed Me")
            
    def printStats(self):
        print(
        f"""
        {self.name}
        Health: {self.hitPoints}
        Hit Chance: {self.hitChance}%
        Maximum damage: {self.maxDamage}
        Armor: {self.armor}
             """)
def fight(player,monster):
    keepGoing= True
    while keepGoing:
        player.attack(monster)
        monster.attack(player)
        print (f"Player:{player.hitPoints} HP")
        print (f"Monster:{monster.hitPoints} HP")
        if player.hitPoints > 0:
            if monster.hitPoints > 0:
                userInput=input("play next round or press Q to quit")
                if userInput == "Q":
                    keepGoing = False
            else:
                print(f"The {player.name} has won! Great Work!")
                keepGoing = False
        
        else:
            print(f"The {monster.name} has won. Try again?")
            keepGoing = False
        
                    
        
        
        

def main():
    c = Character("jim",123,67)
    c.printStats()
   
if __name__ == "__main__":
    main()
