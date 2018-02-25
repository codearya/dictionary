import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        for i in data[w]:
            print(i)
    elif w.title() in data:
        for i in data[w.title()]:
            print(i)
    elif w.upper() in data:
        for i in data[w.upper()]:
            print(i)
    elif len(get_close_matches(w,data.keys()))>0:
        uinput = input("possible alternate matches are : %s , do you want to continue?" %get_close_matches(w,data.keys())[0])
        if uinput.upper() == 'Y':
            for i in data[get_close_matches(w,data.keys())[0]]:
                print(i)
        elif uinput.upper() == 'N':
             print("The Word doesnt exist. Please check agian.")
        else:
             print("Invalid Answer. 'Y' & 'N' are the only acceptable answers")
    else:
        print(" The Word doesnt exist. Please check again.")


word = input("Enter a word:")

translate(word)
