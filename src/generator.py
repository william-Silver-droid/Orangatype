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
  def load_words(self, words, n_words):

    # Path to your CSV file
    csv_file_path = 'words.csv'

    # List variable to store the contents of the CSV file
    words = []

    # Read from the CSV file and store its contents in the list variable
    with open(csv_file_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            words.append(row)
    n_words = len(words)
    def generate_text(self, words, n_words):
      for i in range(30):
        type_words += words[random.randint(0, n_words)]
        type_words += " "
        return type_words

