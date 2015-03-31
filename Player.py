'''
Created on Mar 31, 2015

@author: alexandru
'''

class Player(object):
    def __init__(self, health):
        self.health = health

class ThePlayer(Player):
    def __init__(self):
        super().__init__(health=100)

    def is_alive(self):
        return self.health > 0

    def is_dead(self):
        return self.health <= 0

class Health(object):
    def __init__(self, totalHealth, remainingHealth):
        self.totalHealth = totalHealth
        self.remainingHealth = remainingHealth
        