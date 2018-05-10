#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Min första spel i python3. "Mortal Kombat!"
"""



import sys
import os

import getopt
import mortal
import game



def main():
    """
    This is the main method, I call it main by convention.
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """
    while True:
        mortal.menu()
        choice = input("--> ")


        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            return

        elif choice == "1":
            game.createGame()

        elif choice == "2":
            game.sparadeSpel()

        elif choice == "3":
            game.statistik()

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")







#
#börja bygga mitt script
#


PROGRAM = os.path.basename(sys.argv[0])
AUTHOR = "Georges Kayembe"
EMAIL = "kayss.g@gmail.com"
VERSION = "1.0"
USAGE = """{program} - BuzzQuiz X-GAME!
By {author} ({email}),
version {version}.

Usage:
    {program} [options] name
Options:
-h, --help               Visa hjläptext.
-v, --version            Visa versionen av programmet.
-i, --info               Skriver ut en beskrivning av spelet och spelets ide.
-a, --about              Visa lite beskrivning om mig.
-c, --cheat              Visa hur du kan fuska dig fram.

""".format(program=PROGRAM, author=AUTHOR, email=EMAIL, version=VERSION)

MSG_VERSION = "{program} version {version}.".format(program=PROGRAM, version=VERSION)
MSG_USAGE = "Use {program} --help to get usage.\n".format(program=PROGRAM)


#parameters
EXIT_SUCCESS = 0
EXIT_USAGE = 1
EXIT_FAILED = 2



def printUsage():
    """
    informationen om scripten och exit
    """
    print("")
    print(USAGE)
    sys.exit(EXIT_USAGE)


def printVersion():
    """
    skriva ut versionen av programmet
    """
    print("")
    print(MSG_VERSION)
    sys.exit(EXIT_SUCCESS)

def printInfo():
    """
    Skriver ut en beskrivning av spelet och spelets ide.
    """
    print("")
    with open('info.txt', 'r') as f:
        line = f.read()
        print(line)
    sys.exit(EXIT_SUCCESS)


def printInfOmig():
    """
    Skriver ut en beskrivning om mig.
    """
    print("")
    with open('omig.txt', 'r') as f:
        line = f.read()
        print(line)
    sys.exit(EXIT_SUCCESS)

def printFusk():
    """
    Skriver ut en beskrivning på hur man kan fuska sig fram.
    """
    print("")
    with open('fusk.txt', 'r') as f:
        line = f.read()
        print(line)
    sys.exit(EXIT_SUCCESS)

try:
    opts, args = getopt.getopt(sys.argv[1:], 'hviac', ['help', 'version', 'info', 'about', 'cheat'])
except getopt.GetoptError:
    printUsage()
    sys.exit(EXIT_FAILED)

for opt, arg in opts:
    if opt in ('-h', '--help'):
        printUsage()
    elif opt in ('-v', '--version'):
        printVersion()
    elif opt in ('-i', '--info'):
        printInfo()
    elif opt in ('-a', '--about'):
        printInfOmig()
    elif opt in ('-c', '--cheat'):
        printFusk()
    else:
        printUsage()
        sys.exit(EXIT_FAILED)


if __name__ == "__main__":
    main()
