import random

from Card import Card
from Players import Players

class ShuffleMachine(object):


    def __init__(self):
        self.create()

    def __str__(self):
        return '[' + ', '.join(str(deck) for deck in self.decks) + ']'

    def create(self):
        self.decks = []
        for i in range(0,4):
            for j in range(0,14):
                self.decks.append(Card(i,j))
            

      
            


    def shuffle(self):
        n = len(self.decks)
        for i in range(n-1,0,-1): 
            j = random.randint(0,i+1) 
            self.decks[i],self.decks[j] = self.decks[j],self.decks[i]

    
            
                
