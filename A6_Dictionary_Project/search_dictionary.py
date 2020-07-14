# Alaa' Omar
from json import load
from difflib import get_close_matches
import os

path = os.path.dirname(os.path.abspath(__file__))

os.chdir(path)


with open("data.json") as json_dectionary_file:
    json_dictionary_data = load(json_dectionary_file)


def find_close_Matches(word):
    """ This Functions search a json data format using a key word and returns the close match definition"""

    if word in json_dictionary_data:
        return json_dictionary_data[word]
    elif word.capitalize() in json_dictionary_data:
        return json_dictionary_data[word.capitalize()]
    elif len(get_close_matches(word, json_dictionary_data.keys(), cutoff=.0)) > 0:
        best_match = input("Do you mean [{:s}] ? [y/n]: ".format(get_close_matches(
            word, json_dictionary_data.keys())[0]))
        if (best_match == "y"):
            return json_dictionary_data[get_close_matches(word, json_dictionary_data.keys())[0]]
        elif (best_match == "n"):
            return ("The word Doesn't have a definition in the dictionary.")
    else:
        return ("The word Doesn't have a definition in the dictionary.")


while True:

    inquery_word = input('Please enter your word, "e" to exit : ')
    if inquery_word == 'E' or inquery_word == 'e':
        break
    else:
        word_definition = find_close_Matches(inquery_word.strip().lower())

        if type(word_definition) == list:

            print('='*100)
            for num, each_item in enumerate(word_definition, start=1):

                print("definition[{}]: {}".format(num, each_item))
                print('-'*100)
        else:
            print(" ", word_definition)
