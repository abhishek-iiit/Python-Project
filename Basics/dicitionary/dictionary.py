# Program : Dictionary from the dict_data.json
# User_Name : Abhishek jaiswal
# User_ID : https://github.com/abhishek-iiit
# 
# Feel Free for Pull Request and to contribute to this Project
 
import json
from difflib import get_close_matches

data = json.load(open("dict_data.json"))

def trans(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word ,data.keys())) >0:
        print("Did you mean %s instead" %get_close_matches(word , data.keys())[0])
        decision = input("Press Y/y for yes or N/n for no")
        if decision=="Y" or decision=="y":
            return data[get_close_matches(word ,data.keys())[0]]
        elif decision=="N" or decision=="n":
            return("You entered word other than the simlilar Word")
        else:
            return("You have entered Wrong Input,please enter either Y/y or N/n")
    else:
        print("You entered wrong word")

word = input("Enter the word you want to find\n")
output = trans(word)
if type(output) == list:
    for item in output:
        print("\nMEANING :\n" + item)
else:
    print(output)

