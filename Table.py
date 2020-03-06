from ShuffleMachine import ShuffleMachine
from Players import Players

class Table(object):
    
    def __init__(self, people):
        self.people = people
        self.deals = []
        for j in range(len(self.people.players)):
            self.deals.append(ShuffleMachine())
            
    def __str__(self,people):
        return '[' + ','.join(str(deals) for players in self.people)
                
                

    
