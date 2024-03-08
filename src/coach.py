import time as t
import numpy as np
#this is the coach class made to be the timer and score keeper
class Coach:
    typed # the character typed by the user
    key # answer key the words the user is supposed to type
    def __init__(self, key, typed=""):
        self.typed = typed
        self.key = key

  
