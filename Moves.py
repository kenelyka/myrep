'''
Created on Mar 31, 2015

@author: alexandru
'''

import random

class Move(object):
    def __init__(self, damageAmmount, healAmmount):
        self.damageAmmount = damageAmmount
        self.healAmmount = healAmmount

class FirstMove(Move):
    def __init__(self):
        super().__init__(damageAmmount = random.randrange(18,26))

class SecondMove(Move):
    def __init__(self):
        super().__init__(damageAmmount = random.randrange(10,36))

class ThirdMove(Move):
    def __init__(self):
        super().__init__(healAmmount = random.randrange(18,26))