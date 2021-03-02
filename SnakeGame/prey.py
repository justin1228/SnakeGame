from random import randint

class Prey:
    def __init__(self):
        self.cord = []

    def addData(self, y_winSize, x_winSize):
        
        x_cord = randint(3, x_winSize - 3)
        y_cord = randint(3, y_winSize - 3)
        self.cord.append((y_cord, x_cord))
    
    def getData(self):
        return self.cord
    
    def popData(self):
        return self.cord.pop()
