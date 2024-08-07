from pywebio.input import *
from pywebio.output import *
from pywebio import start_server

import randfacts

def app():
    choice = input("Would you like a fun fact?: ")
    while choice == "yes" or choice == "y" or choice == "Yes" or choice == "Y":
        fun_facts = randfacts.get_fact()
        put_text("Fun Fact: " + fun_facts)
        choice = input("Would you like another fun fact?: ")
    else:
        put_text("Goodbye!")
        exit()
if __name__ == '__main__':
    start_server(app, port=8080)