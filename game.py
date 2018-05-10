#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""game.py all others functions"""

import os
import datetime
import image
import mortal

"""
Min första spel i python3. "Buzz quiz!"
"""
##
# Spelare
##


levelMesure = 0


##
# Presentera resultat
##
def resultat():
    """Show the user's name"""
    usage = """
    Spelare
    -------
    """
    print(usage)

    fhand = open('username.data')
    data = fhand.readlines()
    fhand.close()

    for value in data:
        print("""    {name}"""\
        .format(name=value))


##
# för att se statistiken
##
def statistik():
    """för att se statistiken"""
    fhand = open('statistik.data')
    data = fhand.readlines()
    fhand.close()

    os.system('clear')
    print('Namn och datum på alla vinnare')
    print("==============================" + "\n")
    myData = len(data)
    if myData == 0:
        print("\nEmpty list!")
    else:
        for value in data:
            print(value)

##
# starta sparade spel
##
def sparadeSpel():
    """Starta ett spel som man sparat"""
    fhand = open('usersparalevel.data')
    data = fhand.readlines()
    fhand.close()
    myData = len(data)
    if myData == 0:
        print("Empty memory!")
    else:
        startGame(int(data[0]))




##
# empty file
##
def deleteContent(fName):
    """function för att ta bort items från filen"""
    with open(fName, "w"):
        pass

##
# create user
##
def pickUsername(theUser):
    """function for to create the users"""
    userList = list()
    userList.append(theUser)
    deleteContent('username.data')
    for value in userList:
        fhand = open('username.data', 'a')
        fhand.write(str(value)+'\n')
        fhand.close()
        userList = list()


##
# Start själva spelet
##
def startGame(levelId):
    """Game control"""
    deleteContent('usersparalevel.data')

    if levelId == -1:
        print(image.gameOver())
    elif levelId == 0:
        print(mortal.levelOne())
    elif levelId == 1:
        print(mortal.levelTwo())
    elif levelId == 2:
        print(mortal.levelThree())
    elif levelId == 3:
        print(mortal.levelFour())
    elif levelId == 4:
        print(mortal.levelFive())
    elif levelId == 5:
        print(mortal.levelSix())
    elif levelId == 6:
        print(mortal.levelSeven())
    elif levelId == 7:
        print(image.winner())
        fhand = open('username.data')
        data = fhand.readlines()
        fhand.close()
        input("Tryck 'Enter' för att gå vidare ")
        os.system('clear')
        print("Congratulation %s, you're genius!"%(data[0]))
        mylist = []
        today = datetime.date.today()
        mylist.append(today)
        info = "{name} {datum}".format(name=data[0], datum=mylist[0])

        archives = list()
        archives.append(info)

        for eachitem in archives:
            fhand = open('statistik.data', 'a')
            fhand.write(str(eachitem)+'\n')
            fhand.close()

    else:
        print("Fel parameters!")



##
# Skapa ett spel
##
def createGame():
    """
    Create a game.
    """
    os.system('clear')
    deleteContent('rum.data')
    deleteContent('openrum.data')
    print(image.welcome())
    input("Tryck 'Enter' för att gå vidare ")
    os.system('clear')
    print("\nSkriv din användarnamn : \n")
    playerName = input("--> ")
    print("\nVälkommen %s"%(playerName))
    print("\nTryck 's' för att spara eller 'a' för att avsluta")
    reponse = input("--> ")
    while ((reponse != 's') and (reponse != 'a')):
        print("Fel val")
        reponse = input("--> ")
    if reponse == "a":
        return
    else:
        os.system('clear')
        pickUsername(playerName)
        print(startGame(levelMesure))
