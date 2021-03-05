import csv
import random

nouns = [] # create an empty list of nouns
verbs = []
with open('words.csv') as words: # open the file "words.csv" and assign the contents to the variable "words"
    csv_reader = csv.reader(words, delimiter=',') # fields in each row are separated by commas
    word_count = 0
    for row in csv_reader: # each line of the file is a "row"
        if row[1] == "noun": # row[1] is the second field in the row
            nouns.append(row[0])
        elif row[1] == "verb":
            verbs.append(row[0])
        word_count += 1
    print(f'Loaded {word_count} words.')

for i in range(1,10): # do this ten times
    random_noun1 = random.choice(nouns) # pick a random value from the list
    random_verb = random.choice(verbs)
    random_noun2 = random.choice(nouns)
    print(random_noun1, random_verb, random_noun2)
