import pyfiglet
from termcolor import colored


def print_art(msg, co):
    valid_colors = ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white')

    if co not in valid_colors:
        print('Sorry, that color is not available. Default set to magenta')
        co = 'magenta'

    ascii_msg = pyfiglet.figlet_format(msg)
    ca = colored(ascii_msg, color=co)
    print(ca)

msg = input('What would you like to print?')
co = input('What color?')
print_art(msg, co)