#!/usr/bin/python3

import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def findmeaning(word):

    word = word.lower()

    if word in data:
         return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if Yes, or N if No: " % get_close_matches(word, data.keys())[0])
        if yn == 'Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your choice."
    else:
        return "The word doesn't exist. Please double check it."
   
word = input("Enter a Word: ")

output = findmeaning(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)