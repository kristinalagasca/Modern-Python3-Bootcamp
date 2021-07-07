import requests as r
from pyfiglet import figlet_format as f
from termcolor import colored
from random import choice as c


def dad_start():
    msg = f('DadJokes3000')
    valid = ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white')
    co = c(valid)
    dad = colored(msg, color=co)
    return dad


def get_dad_joke():
    url = 'https://icanhazdadjoke.com/search'

    print(dad_start())
    topic = input('Let me tell you a joke!! Pick a topic: ')
    res = r.get(
        url,
        headers={"Accept": "application/json"},
        params={"term": topic}
    ).json()

    total = res['total_jokes']

    results = res['results']

    if total > 1:
        print(f"I've got {total} jokes. Here's one': \n")
        joke = c(results)['joke']
        return print(joke)
    elif total == 1:
        print(f"I've only got 1 joke. Here it is: \n")
        joke = c(results['joke'])
        return print(joke)
    else:
        return print(f"Sorry there are no jokes for your term: {topic}x")


if __name__ == "__main__":
    get_dad_joke()
