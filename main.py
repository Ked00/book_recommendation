import requests
import random
from colorama import Fore
import os

# api used: https://openlibrary.org/dev/docs/api/search

# topics im interested in
interesting_topics = ["trauma", "Spirituality", "classics", "horror", "assassination"]
random_topic = random.choice(interesting_topics)

# books I want to re-read or I want to read for the first time
book_shelf = ["slight edge", "The book of five rings", "A billion wicked thoughts", "the pale horse", "mein kempf",
              "the brothers karamazov", "king warrior magician lover"]


def get_random_book():
    url = f"https://openlibrary.org/search/authors.json?q=*"
    response = requests.get(url)
    json = response.json()
    recommendation = random.choice(json["docs"])
    random_pick_title = recommendation["top_work"]
    return random_pick_title


def random_book_based_on_a_topics_you_like():
    url = f"https://openlibrary.org/search/authors.json?q={random_topic}&language=en"
    response = requests.get(url)
    json = response.json()
    recommendation = random.choice(json["docs"])
    random_pick_title = recommendation["top_work"]
    return random_pick_title


def clear_terminal():
    os.system("clear")


def make_selection():
    print(
        " 0 = random pick from bookshelf.\n 1 = A random book in the topics you are interested in.\n 2 = Any random book.")
    user_selection = input(" Your pick: ")

    if (user_selection == "0"):
        pick_from_bookshelf = random.choice(book_shelf)
        clear_terminal()
        print(Fore.GREEN + f" you picked: {pick_from_bookshelf}")
        return
    elif (user_selection == "1"):
        random_pick = random_book_based_on_a_topics_you_like()
        clear_terminal()
        print(Fore.GREEN + f" you picked: {random_pick}")
        return
    elif (user_selection == "2"):
        random_book = get_random_book()
        clear_terminal()
        print(Fore.GREEN + f" you picked: {random_book}")
        return


make_selection()
