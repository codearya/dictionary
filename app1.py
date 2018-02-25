import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys()))>0:
        uinput = input("possible alternate matches are : %s , do you want to continue?" %get_close_matches(w,data.keys())[0])
        if uinput.upper() == 'Y':
            return data[get_close_matches(w,data.keys())[0]]
        elif uinput.upper() == 'N':
            return "The Word doesnt exist. Please check agian."
        else:
            return "Invalid Answer. 'Y' & 'N' are the only acceptable answers"
    else:
        return " The Word doesnt exist. Please check again."


word = input("Enter a word:")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
