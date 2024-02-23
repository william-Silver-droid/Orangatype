import random
import numpy as np
import csv
class generator():
  words = []
  type_words = ""
  n_words = 0
  def __init__(self, words, n_words):
    self.words = words
    self.n_words = n_words
    self.words_path = ""
    self.type_words = ""
  def load_words(self):

    # Path to your CSV file
    self.words_path = 'words.csv'

    # List variable to store the contents of the CSV file
    self.words = []

    # Read from the CSV file and store its contents in the list variable
    with open(self.words_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            self.words.append(row)
    self.n_words = len(self.words)
    
  def generate_text(self):
    print(self.n_words)
    for i in range(5):
      self.type_words += self.words[random.randint(0, self.n_words)][0]
      self.type_words += " "
    return self.type_words
