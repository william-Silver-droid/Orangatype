import time as t
import numpy as np
import nltk
#this is the coach class made to be the timer and score keeper
class coach:
    def __init__(self, key, user_typed) -> None:
        self.key = key
        self.user_typed = user_typed
    def calc_acc(self):
        oran_text = self.key.split()
        user_text = self.user_typed.split()
        oran_text = oran_text[0 :len(user_text)]
        print("user_text", user_text)
        print("oran_text", oran_text)
        BLEUscore = nltk.translate.bleu_score.sentence_bleu(oran_text, user_text) 
        
        Acc_score = BLEUscore*100

        print(Acc_score)
        return(Acc_score)

  
