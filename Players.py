

class Players(object):

    def __init__(self):
        self.create()

    def __str__(self):
        return  '[Players playing: ' + ', '.join(str(player) for player in self.players) + ']'

    def create(self):
        self.players = []
        numPlayers = int(input("Number of players: "))
        
        for i in range(numPlayers):
            name = str(input("Enter player name: "))
            self.players.append(name)
        
                
