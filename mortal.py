#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""mortal.py content all function"""

import os
import random
import image
import game

def menu():
    """
    Display the menu with the options that E-G can do
    """
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print("")
    print("Welcome to Mortal BuzzQuiz X-GAME")
    print("---------------------------------")
    print("1) Start a new game?")
    print("2) Continue to your game?")
    print("3) The best of palmares?")
    print("q) Quit.")



##
# Function for level 1
##
def levelOne():
    """function for levelOne"""

    print(image.levelOneImage())
    input("\nTryck 'Enter' för att försätta!")
    os.system('clear')

    print(game.resultat())
    print("\n")
    input("Tryck 'Enter' för att börja 'Quizz Buzz' del ett!")

    question = ["I vilken amerikansk stat ligger Las Vegas?", "Vilken stad utgör Danmarks sydligaste punkt?",\
     "En bergskedja i Asien som skiljer den idiska halvön från tibetplatån"]
    answer = ["nevada", "gedser", "himalaya"]
    os.system('clear')
    print("Geografi")
    print("--------")
    theQuestion = random.choice(question)
    print(theQuestion)

    spelareOneAnswer = input("--> ")

    rightAnswer = ""

    if theQuestion == question[0]:
        rightAnswer = answer[0]
    elif theQuestion == question[1]:
        rightAnswer = answer[1]
    elif theQuestion == question[2]:
        rightAnswer = answer[2]

    myAnswer = spelareOneAnswer.lower()

    levelMesure = 1

    ##spara vilket rum man befinner sig
    ##---------------------------------
    ##
    userRum = list()
    rum = 0
    userRum.append(rum)
    game.deleteContent('rum.data')
    for value in userRum:
        fhand = open('rum.data', 'a')
        fhand.write(str(value))
        fhand.close()
        userRum = list()

    count = 0
    chanser = 4
    while count <= 3:
        if ((myAnswer == 'i') or (myAnswer == 'info')):
            print("\nBuzzQuiz level ett. Temat är Geografi." +\
             " Rätt svar ge dig möjligt att gå vidare till level två.\nDu har "+ str(chanser) +" chanser.")
            input("\nTryck 'Enter' för att försätta!")
            os.system('clear')
            print(theQuestion)
            spelareOneAnswer = input("--> ")
            myAnswer = spelareOneAnswer.lower()
            continue

        elif ((myAnswer == 'h') or (myAnswer == 'hjälp')):
            print("Listan av alla kommando")
            print("-----------------------\n")
            print("i, info       Skriver ut beskrivning av 'level'.")
            print("h, hjälp      Skriver ut en lista av de kommandon som du kan göra.")
            print("fr, fram      Gå framåt till nästa rum, om det är upplåst.")
            print("ba, bak       Gå bakåt till föregående rum.")
            print("l, ledtråd    Ge en ledtråd, eller fler om det finns.")
            print("c, cheat      utför automatiskt alla frågor.")
            input("\nTryck 'Enter' för att försätta!")
            os.system('clear')
            print(theQuestion)
            spelareOneAnswer = input("--> ")
            myAnswer = spelareOneAnswer.lower()
            continue

        elif ((myAnswer == 'fr') or (myAnswer == 'fram')):
            fhand = open('openrum.data')
            data = fhand.readlines()
            fhand.close()
            myData = len(data)
            if myData == 0:
                print("Du kan inte gå till nästa rum! Svara rätt på frågan först!")
                input("\nTryck 'Enter' för att försätta!")
                os.system('clear')
                print(theQuestion)
                spelareOneAnswer = input("--> ")
                myAnswer = spelareOneAnswer.lower()
                continue
            else:
                input("\nTryck 'Enter' för gå till nästa rum!")
                os.system('clear')
                levelMesure = 1
                print(game.startGame(levelMesure))
                return



        elif ((myAnswer == 'ba') or (myAnswer == 'bak')):
            print("Inga föregående rum! Du befinner dig på level 1!")
            input("\nTryck 'Enter' för att försätta!")
            os.system('clear')
            print(theQuestion)
            spelareOneAnswer = input("--> ")
            myAnswer = spelareOneAnswer.lower()
            continue

        elif ((myAnswer == 'l') or (myAnswer == 'ledtråd')):
            alternativOne = ["Huvudstad är Carson City", "'NE' de två första bokstaver",\
             "Staden som Andre Agassi är född"]
            alternativTwo = ["är en viktig hamn för vägfarande från Skandinavien till Berlin",\
            "inspelningen av några scener av den klassiska danska TV-serien Matador", "'ER' de två sista bokstaver"]
            alternativThree = ["De högsta på planeten med fjorton bergstoppar över 8 000 meter",\
            "Namnet betyder 'snöns boning'.", "'HI' de två första bokstaver."]
            if theQuestion == question[0]:
                ledtrod = random.choice(alternativOne)
                print("\n" + ledtrod + "\n")
                input("\nTryck 'Enter' för att försätta!")
                os.system('clear')
                print(theQuestion)
                spelareOneAnswer = input("--> ")
                myAnswer = spelareOneAnswer.lower()
                continue
            elif theQuestion == question[1]:
                ledtrod = random.choice(alternativTwo)
                print("\n" + ledtrod + "\n")
                input("\nTryck 'Enter' för att försätta!")
                os.system('clear')
                print(theQuestion)
                spelareOneAnswer = input("--> ")
                myAnswer = spelareOneAnswer.lower()
                continue
            else:
                ledtrod = random.choice(alternativThree)
                print("\n" + ledtrod + "\n")
                input("\nTryck 'Enter' för att försätta!")
                os.system('clear')
                print(theQuestion)
                spelareOneAnswer = input("--> ")
                myAnswer = spelareOneAnswer.lower()
                continue
        elif ((myAnswer == 'c') or (myAnswer == 'cheat')):
            print("haha :-D din lilla fuskare!")

            ##spara betyg
            ##-----------
            ##
            fhand = open('openrum.data')
            data = fhand.readlines()
            fhand.close()
            myData = len(data)

            betyg = 10
            userBetyg = list()
            userBetyg.append(betyg)

            if int(myData) == 0:
                game.deleteContent('openrum.data')
                for value in userBetyg:
                    fhand = open('openrum.data', 'a')
                    fhand.write(str(value))
                    fhand.close()
                    userBetyg = list()
            elif int(data[0]) > betyg:
                pass
            else:
                game.deleteContent('openrum.data')
                for value in userBetyg:
                    fhand = open('openrum.data', 'a')
                    fhand.write(str(value))
                    fhand.close()
                    userBetyg = list()


            input("\nTryck 'Enter' för att börja på level två!")
            os.system('clear')
            levelMesure = 1
            print(game.startGame(levelMesure))
            return

        elif myAnswer == rightAnswer:
            print("\n%s är korrekt"%(spelareOneAnswer))

            ##spara betyg
            ##-----------
            ##

            fhand = open('openrum.data')
            data = fhand.readlines()
            fhand.close()
            myData = len(data)

            betyg = 10
            userBetyg = list()
            userBetyg.append(betyg)

            if int(myData) == 0:
                game.deleteContent('openrum.data')
                for value in userBetyg:
                    fhand = open('openrum.data', 'a')
                    fhand.write(str(value))
                    fhand.close()
                    userBetyg = list()
            elif int(data[0]) > betyg:
                pass
            else:
                game.deleteContent('openrum.data')
                for value in userBetyg:
                    fhand = open('openrum.data', 'a')
                    fhand.write(str(value))
                    fhand.close()
                    userBetyg = list()

            print("\nTryck 'f' för att försätta. 'a' för att avsluta. 's' för att spara.")
            choix = input("--> ")
            while ((choix != 's') and (choix != 'a') and (choix != 'f')):
                print("Fel val")
                choix = input("--> ")
            if choix == "a":
                print("\nAvsluta..")
                return
            elif choix == "s":
                print("\nSparat..")
                userListLevel = list()
                userListLevel.append(levelMesure)
                game.deleteContent('usersparalevel.data')
                for value in userListLevel:
                    fhand = open('usersparalevel.data', 'a')
                    fhand.write(str(value))
                    fhand.close()
                    userListLevel = list()
                return

            elif choix == 'f':
                os.system('clear')
                levelMesure = 1
                print(game.startGame(levelMesure))
                return
        else:
            if count == 3:
                break
            else:
                print("Försök igen!")
                spelareOneAnswer = input("--> ")
                myAnswer = spelareOneAnswer.lower()
                count = count + 1
                chanser = chanser - 1


    print("%s är fel"%(spelareOneAnswer))
    input("\nTryck 'Enter'")
    os.system('clear')
    print(image.gameOver())
    return




##
# Function for level 2
##
def levelTwo():
    """function for levelTWO"""

    print(image.levelTwoImage())
    input("\nTryck 'Enter' för att försätta!")
    os.system('clear')

    input("Tryck 'Enter' för att börja 'Quizz Buzz' del två!")

    question = ["När började första världskriget?(vilket år)",\
     "År 1874 blev Guldkusten en brittisk koloni. Vad heter detta land idag?",\
     "Vilket land har Namibia varit koloniserad av"]
    answer = ["1914", "ghana", "tyskland"]
    os.system('clear')
    print("Historia")
    print("--------")
    theQuestion = random.choice(question)
    print(theQuestion)

    spelareOneAnswer = input("--> ")

    rightAnswer = ""

    if theQuestion == question[0]:
        rightAnswer = answer[0]
    elif theQuestion == question[1]:
        rightAnswer = answer[1]
    elif theQuestion == question[2]:
        rightAnswer = answer[2]

    myAnswer = spelareOneAnswer.lower()

    levelMesure = 2

    ##spara vilket rum man befinner sig
    ##---------------------------------
    ##
    userRum = list()
    rum = 1
    userRum.append(rum)
    game.deleteContent('rum.data')
    for value in userRum:
        fhand = open('rum.data', 'a')
        fhand.write(str(value))
        fhand.close()
        userRum = list()

    count = 0
    chanser = 4
    while count <= 3:
        if ((myAnswer == 'i') or (myAnswer == 'info')):
            print("\nBuzzQuiz level två. Temat är Historia." +\
            " Rätt svar ge dig möjligt att gå vidare till level tre.\nDu får "+str(chanser)+" chanser.")
            input("\nTryck 'Enter' för att försätta!")
            os.system('clear')
            print(theQuestion)
            spelareOneAnswer = input("--> ")
            myAnswer = spelareOneAnswer.lower()
            continue

        elif ((myAnswer == 'h') or (myAnswer == 'hjälp')):
            print("Listan av alla kommando")
            print("-----------------------\n")
            print("i, info       Skriver ut beskrivning av 'level'.")
            print("h, hjälp      Skriver ut en lista av de kommandon som du kan göra.")
            print("fr, fram      Gå framåt till nästa rum, om det är upplåst.")
            print("ba, bak       Gå bakåt till föregående rum.")
            print("l, ledtråd    Ge en ledtråd, eller fler om det finns.")
            print("c, cheat      utför automatiskt alla frågor.")
            input("\nTryck 'Enter' för att försätta!")
            os.system('clear')
            print(theQuestion)
            spelareOneAnswer = input("--> ")
            myAnswer = spelareOneAnswer.lower()
            continue


        elif ((myAnswer == 'fr') or (myAnswer == 'fram')):
            fhand = open('openrum.data')
            data = fhand.readlines()
            fhand.close()
            #myData = len(data)
            if int(data[0]) < 20:
                print("Du kan inte gå till nästa rum! Svara rätt på frågan först!")
                input("\nTryck 'Enter' för att försätta!")
                os.system('clear')
                print(theQuestion)
                spelareOneAnswer = input("--> ")
                myAnswer = spelareOneAnswer.lower()
                continue
            else:
                input("\nTryck 'Enter' för gå till nästa rum!")
                os.system('clear')
                levelMesure = 2
                print(game.startGame(levelMesure))
                return



        elif ((myAnswer == 'ba') or (myAnswer == 'bak')):
            fhand = open('rum.data')
            data = fhand.readlines()
            fhand.close()

            os.system('clear')
            levelMesure = int(data[0]) - 1
            print(game.startGame(levelMesure))
            return


        elif ((myAnswer == 'l') or (myAnswer == 'ledtråd')):
            alternativOne = ["Ett sjukhus i London sätter in radium i cancerbehandlingen",\
             "Ett socialdemokratiskt arbetartåg samlar 50 000 arbetare i protest mot Bondetåget i Sverige",\
              "Selma Lagerlöf väljs som första kvinna in i Svenska akademien"]
            alternativTwo = ["En av de första afrikanska staterna att uppnå självständighet, år 1957",\
            "Ordet betyder 'krigarkonung'.", "Huvudstaden heter Accra"]
            alternativThree = ["Det gränsar i norr mot Danmark, i öster mot Polen," +\
             " i söder mot Schweiz, samt i väster mot Frankrike.",\
            "Är Europas sjunde största land.", "Styrs genom parlamentarisk demokrati."]
            if theQuestion == question[0]:
                ledtrod = random.choice(alternativOne)
                print("\n" + ledtrod + "\n")
                input("\nTryck 'Enter' för att försätta!")
                os.system('clear')
                print(theQuestion)
                spelareOneAnswer = input("--> ")
                myAnswer = spelareOneAnswer.lower()
                continue
            elif theQuestion == question[1]:
                ledtrod = random.choice(alternativTwo)
                print("\n" + ledtrod + "\n")
                input("\nTryck 'Enter' för att försätta!")
                os.system('clear')
                print(theQuestion)
                spelareOneAnswer = input("--> ")
                myAnswer = spelareOneAnswer.lower()
                continue
            else:
                ledtrod = random.choice(alternativThree)
                print("\n" + ledtrod + "\n")
                input("\nTryck 'Enter' för att försätta!")
                os.system('clear')
                print(theQuestion)
                spelareOneAnswer = input("--> ")
                myAnswer = spelareOneAnswer.lower()
                continue
        elif ((myAnswer == 'c') or (myAnswer == 'cheat')):
            print("haha :-D din lilla fuskare!")

            ##spara betyg
            ##-----------
            ##
            fhand = open('openrum.data')
            data = fhand.readlines()
            fhand.close()
            myData = len(data)

            betyg = 20
            userBetyg = list()
            userBetyg.append(betyg)

            if int(myData) == 0:
                game.deleteContent('openrum.data')
                for value in userBetyg:
                    fhand = open('openrum.data', 'a')
                    fhand.write(str(value))
                    fhand.close()
                    userBetyg = list()
            elif int(data[0]) > betyg:
                pass
            else:
                game.deleteContent('openrum.data')
                for value in userBetyg:
                    fhand = open('openrum.data', 'a')
                    fhand.write(str(value))
                    fhand.close()
                    userBetyg = list()

            input("\nTryck 'Enter' för att börja på level tre!")
            os.system('clear')
            levelMesure = 2
            print(game.startGame(levelMesure))
            return

        elif myAnswer == rightAnswer:
            print("\n%s är korrekt"%(spelareOneAnswer))

            ##spara betyg
            ##-----------
            ##
            fhand = open('openrum.data')
            data = fhand.readlines()
            fhand.close()
            myData = len(data)

            betyg = 20
            userBetyg = list()
            userBetyg.append(betyg)

            if int(myData) == 0:
                game.deleteContent('openrum.data')
                for value in userBetyg:
                    fhand = open('openrum.data', 'a')
                    fhand.write(str(value))
                    fhand.close()
                    userBetyg = list()
            elif int(data[0]) > betyg:
                pass
            else:
                game.deleteContent('openrum.data')
                for value in userBetyg:
                    fhand = open('openrum.data', 'a')
                    fhand.write(str(value))
                    fhand.close()
                    userBetyg = list()

            print("\nTryck 'f' för att försätta. 'a' för att avsluta. 's' för att spara.")
            choix = input("--> ")
            while ((choix != 's') and (choix != 'a') and (choix != 'f')):
                print("Fel val")
                choix = input("--> ")
            if choix == "a":
                print("\nAvsluta..")
                return
            elif choix == "s":
                print("\nSparat..")
                userListLevel = list()
                userListLevel.append(levelMesure)
                game.deleteContent('usersparalevel.data')
                for value in userListLevel:
                    fhand = open('usersparalevel.data', 'a')
                    fhand.write(str(value))
                    fhand.close()
                    userListLevel = list()
                return

            elif choix == 'f':
                os.system('clear')
                levelMesure = 2
                print(game.startGame(levelMesure))
                return
        else:
            if count == 3:
                break
            else:
                print("Försök igen!")
                spelareOneAnswer = input("--> ")
                myAnswer = spelareOneAnswer.lower()
                count = count + 1
                chanser = chanser - 1

    print("%s är fel"%(spelareOneAnswer))
    input("\nTryck 'Enter'")
    os.system('clear')
    print(image.gameOver())
    return



##
# Function for level 3
##
def levelThree():
    """function for levelThree"""

    print(image.levelThreeImage())
    input("\nTryck 'Enter' för att försätta!")
    os.system('clear')

    input("Tryck 'Enter' för att börja 'Quizz Buzz' del tre!")

    question = ["Vilken sagohjälte är Shakespeares 'Hamlet' baserad på?",\
     "Vilken form har trollkarlen Gandalfs hatt?",\
     "Vad för slags djur är Jan Långben?"]
    answer = ["amleth", "spetsig", "hund"]
    os.system('clear')
    print("Litteratur")
    print("----------")
    theQuestion = random.choice(question)
    print(theQuestion)

    spelareOneAnswer = input("--> ")

    rightAnswer = ""

    if theQuestion == question[0]:
        rightAnswer = answer[0]
    elif theQuestion == question[1]:
        rightAnswer = answer[1]
    elif theQuestion == question[2]:
        rightAnswer = answer[2]

    levelMesure = 3

    myAnswer = spelareOneAnswer.lower()

    levelMesure = 3


    ##spara vilket rum man befinner sig
    ##---------------------------------
    ##
    userRum = list()
    rum = 2
    userRum.append(rum)
    game.deleteContent('rum.data')
    for value in userRum:
        fhand = open('rum.data', 'a')
        fhand.write(str(value))
        fhand.close()
        userRum = list()

    count = 0
    chanser = 3
    while count <= 2:
        if ((myAnswer == 'i') or (myAnswer == 'info')):
            print("\nBuzzQuiz level tre. Temat är Litteratur." +\
             " Rätt svar ge dig möjligt att gå vidare till level fyra.\nDu får "+str(chanser)+" chanser.")
            input("\nTryck 'Enter' för att försätta!")
            os.system('clear')
            print(theQuestion)
            spelareOneAnswer = input("--> ")
            myAnswer = spelareOneAnswer.lower()
            continue

        elif ((myAnswer == 'h') or (myAnswer == 'hjälp')):
            print("Listan av alla kommando")
            print("-----------------------\n")
            print("i, info       Skriver ut beskrivning av 'level'.")
            print("h, hjälp      Skriver ut en lista av de kommandon som du kan göra.")
            print("fr, fram      Gå framåt till nästa rum, om det är upplåst.")
            print("ba, bak       Gå bakåt till föregående rum.")
            print("l, ledtråd    Ge en ledtråd, eller fler om det finns.")
            print("c, cheat      utför automatiskt alla frågor.")
            input("\nTryck 'Enter' för att försätta!")
            os.system('clear')
            print(theQuestion)
            spelareOneAnswer = input("--> ")
            myAnswer = spelareOneAnswer.lower()
            continue

        elif ((myAnswer == 'fr') or (myAnswer == 'fram')):
            fhand = open('openrum.data')
            data = fhand.readlines()
            fhand.close()
            #myData = len(data)
            if int(data[0]) < 30:
                print("Du kan inte gå till nästa rum! Svara rätt på frågan först!")
                input("\nTryck 'Enter' för att försätta!")
                os.system('clear')
                print(theQuestion)
                spelareOneAnswer = input("--> ")
                myAnswer = spelareOneAnswer.lower()
                continue
            else:
                input("\nTryck 'Enter' för gå till nästa rum!")
                os.system('clear')
                levelMesure = 3
                print(game.startGame(levelMesure))
                return



        elif ((myAnswer == 'ba') or (myAnswer == 'bak')):
            fhand = open('rum.data')
            data = fhand.readlines()
            fhand.close()

            os.system('clear')
            levelMesure = int(data[0]) - 1
            print(game.startGame(levelMesure))
            return

        elif ((myAnswer == 'l') or (myAnswer == 'ledtråd')):
            alternativOne = ["Prins av Danmark ",\
             "Is a figure in a medieval Scandinavian legend",\
              "'TH' är de sista bokstaver"]
            alternativTwo = ["Det ka betyda vass",\
            "mindre än 90° (om vinkel)", "Som har en starkt avsmalnande punkt"]
            alternativThree = ["Är en domesticerad underart av varg.",\
            "Är en av människans äldsta ocg bästa följeslagare.", "Kan användas vid jakt."]
            if theQuestion == question[0]:
                ledtrod = random.choice(alternativOne)
                print("\n" + ledtrod + "\n")
                input("\nTryck 'Enter' för att försätta!")
                os.system('clear')
                print(theQuestion)
                spelareOneAnswer = input("--> ")
                myAnswer = spelareOneAnswer.lower()
                continue
            elif theQuestion == question[1]:
                ledtrod = random.choice(alternativTwo)
                print("\n" + ledtrod + "\n")
                input("\nTryck 'Enter' för att försätta!")
                os.system('clear')
                print(theQuestion)
                spelareOneAnswer = input("--> ")
                myAnswer = spelareOneAnswer.lower()
                continue
            else:
                ledtrod = random.choice(alternativThree)
                print("\n" + ledtrod + "\n")
                input("\nTryck 'Enter' för att försätta!")
                os.system('clear')
                print(theQuestion)
                spelareOneAnswer = input("--> ")
                myAnswer = spelareOneAnswer.lower()
                continue
        elif ((myAnswer == 'c') or (myAnswer == 'cheat')):
            print("haha :-D din lilla fuskare!")

            ##spara betyg
            ##-----------
            ##
            fhand = open('openrum.data')
            data = fhand.readlines()
            fhand.close()
            myData = len(data)

            betyg = 30
            userBetyg = list()
            userBetyg.append(betyg)

            if int(myData) == 0:
                game.deleteContent('openrum.data')
                for value in userBetyg:
                    fhand = open('openrum.data', 'a')
                    fhand.write(str(value))
                    fhand.close()
                    userBetyg = list()
            elif int(data[0]) > betyg:
                pass
            else:
                game.deleteContent('openrum.data')
                for value in userBetyg:
                    fhand = open('openrum.data', 'a')
                    fhand.write(str(value))
                    fhand.close()
                    userBetyg = list()

            input("\nTryck 'Enter' för att börja på level fyra!")
            os.system('clear')
            levelMesure = 3
            print(game.startGame(levelMesure))
            return

        elif myAnswer == rightAnswer:
            print("\n%s är korrekt"%(spelareOneAnswer))

            ##spara betyg
            ##-----------
            ##

            fhand = open('openrum.data')
            data = fhand.readlines()
            fhand.close()
            myData = len(data)

            betyg = 30
            userBetyg = list()
            userBetyg.append(betyg)

            if int(myData) == 0:
                game.deleteContent('openrum.data')
                for value in userBetyg:
                    fhand = open('openrum.data', 'a')
                    fhand.write(str(value))
                    fhand.close()
                    userBetyg = list()
            elif int(data[0]) > betyg:
                pass
            else:
                game.deleteContent('openrum.data')
                for value in userBetyg:
                    fhand = open('openrum.data', 'a')
                    fhand.write(str(value))
                    fhand.close()
                    userBetyg = list()

            print("\nTryck 'f' för att försätta. 'a' för att avsluta. 's' för att spara.")
            choix = input("--> ")
            while ((choix != 's') and (choix != 'a') and (choix != 'f')):
                print("Fel val")
                choix = input("--> ")
            if choix == "a":
                print("\nAvsluta..")
                return
            elif choix == "s":
                print("\nSparat..")
                userListLevel = list()
                userListLevel.append(levelMesure)
                game.deleteContent('usersparalevel.data')
                for value in userListLevel:
                    fhand = open('usersparalevel.data', 'a')
                    fhand.write(str(value))
                    fhand.close()
                    userListLevel = list()
                return

            elif choix == 'f':
                os.system('clear')
                levelMesure = 3
                print(game.startGame(levelMesure))
                return
        else:
            if count == 2:
                break
            else:
                print("Försök igen!")
                spelareOneAnswer = input("--> ")
                myAnswer = spelareOneAnswer.lower()
                count = count + 1
                chanser = chanser - 1


    print("%s är fel"%(spelareOneAnswer))
    input("\nTryck 'Enter'")
    os.system('clear')
    print(image.gameOver())
    return



##
# Function for level 4
##
def levelFour():
    """function for levelFour"""

    print(image.levelFourImage())
    input("\nTryck 'Enter' för att försätta!")
    os.system('clear')

    input("Tryck 'Enter' för att börja 'Quizz Buzz' del fyra!")

    question = ["Vad är titeln på den brittiska sångerskan Adeles debutalbum?",\
     "När bildades The Beatles?",\
     "De har tagit sitt bandnamn från Harry Dean Stantons karaktär, Travis Henderson," +\
      " i filmen 'Paris,Texas'. Vad heter bandet?"]
    answer = ["19", "1958", "travis"]
    os.system('clear')
    print("Musik")
    print("-----")
    theQuestion = random.choice(question)
    print(theQuestion)

    spelareOneAnswer = input("--> ")

    rightAnswer = ""

    if theQuestion == question[0]:
        rightAnswer = answer[0]
    elif theQuestion == question[1]:
        rightAnswer = answer[1]
    elif theQuestion == question[2]:
        rightAnswer = answer[2]

    myAnswer = spelareOneAnswer.lower()

    levelMesure = 4

    ##spara vilket rum man befinner sig
    ##---------------------------------
    ##
    userRum = list()
    rum = 3
    userRum.append(rum)
    game.deleteContent('rum.data')
    for value in userRum:
        fhand = open('rum.data', 'a')
        fhand.write(str(value))
        fhand.close()
        userRum = list()

    count = 0
    chanser = 3
    while count <= 2:
        if ((myAnswer == 'i') or (myAnswer == 'info')):
            print("\nBuzzQuiz level fyra. Temat är Musik. "+\
            " Rätt svar ge dig möjligt att gå vidare till level fem.\nDu får "+str(chanser)+" chanser.")
            input("\nTryck 'Enter' för att försätta!")
            os.system('clear')
            print(theQuestion)
            spelareOneAnswer = input("--> ")
            myAnswer = spelareOneAnswer.lower()
            continue

        elif ((myAnswer == 'h') or (myAnswer == 'hjälp')):
            print("Listan av alla kommando")
            print("-----------------------\n")
            print("i, info       Skriver ut beskrivning av 'level'.")
            print("h, hjälp      Skriver ut en lista av de kommandon som du kan göra.")
            print("fr, fram      Gå framåt till nästa rum, om det är upplåst.")
            print("ba, bak       Gå bakåt till föregående rum.")
            print("l, ledtråd    Ge en ledtråd, eller fler om det finns.")
            print("c, cheat      utför automatiskt alla frågor.")
            input("\nTryck 'Enter' för att försätta!")
            os.system('clear')
            print(theQuestion)
            spelareOneAnswer = input("--> ")
            myAnswer = spelareOneAnswer.lower()
            continue


        elif ((myAnswer == 'fr') or (myAnswer == 'fram')):
            fhand = open('openrum.data')
            data = fhand.readlines()
            fhand.close()
            #myData = len(data)
            if int(data[0]) < 40:
                print("Du kan inte gå till nästa rum! Svara rätt på frågan först!")
                input("\nTryck 'Enter' för att försätta!")
                os.system('clear')
                print(theQuestion)
                spelareOneAnswer = input("--> ")
                myAnswer = spelareOneAnswer.lower()
                continue
            else:
                input("\nTryck 'Enter' för gå till nästa rum!")
                os.system('clear')
                levelMesure = 4
                print(game.startGame(levelMesure))
                return



        elif ((myAnswer == 'ba') or (myAnswer == 'bak')):
            fhand = open('rum.data')
            data = fhand.readlines()
            fhand.close()

            os.system('clear')
            levelMesure = int(data[0]) - 1
            print(game.startGame(levelMesure))
            return

        elif ((myAnswer == 'l') or (myAnswer == 'ledtråd')):
            alternativOne = ["Albumet släpptes den 28 januari 2008",\
             "Det är ett udda tal mindre än 25",\
              "Ett år efter du blev myndig"]
            alternativTwo = ["MCMLVIII 'i romarska siffror'.",\
            "Sveriges första kvinnliga poliser börjar tjänstgöra i Stockholm",\
             "Sverige deltar för första gången i Eurovision Song Contest,"+\
             " där Alice Babs sjunger Lilla stjärna och slutar på fjärde plats."]
            alternativThree = ["Som består av Fran Healy, Dougie Payne, Andy Dunlop och Neil Primrose.",\
            "'Sing, Side, Closer, Why Does it Always Rain on Me?' är deras hitlåtar",\
             "Harry Dean Stantons efternamn på filmen."]
            if theQuestion == question[0]:
                ledtrod = random.choice(alternativOne)
                print("\n" + ledtrod + "\n")
                input("\nTryck 'Enter' för att försätta!")
                os.system('clear')
                print(theQuestion)
                spelareOneAnswer = input("--> ")
                myAnswer = spelareOneAnswer.lower()
                continue
            elif theQuestion == question[1]:
                ledtrod = random.choice(alternativTwo)
                print("\n" + ledtrod + "\n")
                input("\nTryck 'Enter' för att försätta!")
                os.system('clear')
                print(theQuestion)
                spelareOneAnswer = input("--> ")
                myAnswer = spelareOneAnswer.lower()
                continue
            else:
                ledtrod = random.choice(alternativThree)
                print("\n" + ledtrod + "\n")
                input("\nTryck 'Enter' för att försätta!")
                os.system('clear')
                print(theQuestion)
                spelareOneAnswer = input("--> ")
                myAnswer = spelareOneAnswer.lower()
                continue
        elif ((myAnswer == 'c') or (myAnswer == 'cheat')):
            print("haha :-D din lilla fuskare!")

            ##spara betyg
            ##-----------
            ##
            fhand = open('openrum.data')
            data = fhand.readlines()
            fhand.close()
            myData = len(data)

            betyg = 40
            userBetyg = list()
            userBetyg.append(betyg)

            if int(myData) == 0:
                game.deleteContent('openrum.data')
                for value in userBetyg:
                    fhand = open('openrum.data', 'a')
                    fhand.write(str(value))
                    fhand.close()
                    userBetyg = list()
            elif int(data[0]) > betyg:
                pass
            else:
                game.deleteContent('openrum.data')
                for value in userBetyg:
                    fhand = open('openrum.data', 'a')
                    fhand.write(str(value))
                    fhand.close()
                    userBetyg = list()


            input("\nTryck 'Enter' för att börja på level fem!")
            os.system('clear')
            levelMesure = 4
            print(game.startGame(levelMesure))
            return

        elif myAnswer == rightAnswer:
            print("\n%s är korrekt"%(spelareOneAnswer))

            ##spara betyg
            ##-----------
            ##
            fhand = open('openrum.data')
            data = fhand.readlines()
            fhand.close()
            myData = len(data)

            betyg = 40
            userBetyg = list()
            userBetyg.append(betyg)

            if int(myData) == 0:
                game.deleteContent('openrum.data')
                for value in userBetyg:
                    fhand = open('openrum.data', 'a')
                    fhand.write(str(value))
                    fhand.close()
                    userBetyg = list()
            elif int(data[0]) > betyg:
                pass
            else:
                game.deleteContent('openrum.data')
                for value in userBetyg:
                    fhand = open('openrum.data', 'a')
                    fhand.write(str(value))
                    fhand.close()
                    userBetyg = list()


            print("\nTryck 'f' för att försätta. 'a' för att avsluta. 's' för att spara.")
            choix = input("--> ")
            while ((choix != 's') and (choix != 'a') and (choix != 'f')):
                print("Fel val")
                choix = input("--> ")
            if choix == "a":
                print("\nAvsluta..")
                return
            elif choix == "s":
                print("\nSparat..")
                userListLevel = list()
                userListLevel.append(levelMesure)
                game.deleteContent('usersparalevel.data')
                for value in userListLevel:
                    fhand = open('usersparalevel.data', 'a')
                    fhand.write(str(value))
                    fhand.close()
                    userListLevel = list()
                return

            elif choix == 'f':
                os.system('clear')
                levelMesure = 4
                print(game.startGame(levelMesure))
                return
        else:
            if count == 2:
                break
            else:
                print("Försök igen!")
                spelareOneAnswer = input("--> ")
                myAnswer = spelareOneAnswer.lower()
                count = count + 1
                chanser = chanser - 1


    print("%s är fel"%(spelareOneAnswer))
    input("\nTryck 'Enter'")
    os.system('clear')
    print(image.gameOver())
    return



##
# Function for level 5
##
def levelFive():
    """function for levelFive"""

    print(image.levelFiveImage())
    input("\nTryck 'Enter' för att försätta!")
    os.system('clear')

    input("Tryck 'Enter' för att börja 'Quizz Buzz' del fem!")

    question = ["Hur många landskamper spelade den före detta svenska fotbollsspelaren Ralf Edström?",\
     "Vilket land dominerade och vann lagtävlingen vid 2013-års EM i dressyr som avgjordes i Danmark?",\
     "Vilket land tog silvermedalj vid 1994-års världsmästerskap i fotboll som spelades i USA?"]
    answer = ["40", "tyskland", "italien"]
    os.system('clear')
    print("Sport och fritid")
    print("----------------")
    theQuestion = random.choice(question)
    print(theQuestion)

    spelareOneAnswer = input("--> ")

    rightAnswer = ""

    if theQuestion == question[0]:
        rightAnswer = answer[0]
    elif theQuestion == question[1]:
        rightAnswer = answer[1]
    elif theQuestion == question[2]:
        rightAnswer = answer[2]

    myAnswer = spelareOneAnswer.lower()

    levelMesure = 5

    ##spara vilket rum man befinner sig
    ##---------------------------------
    ##
    userRum = list()
    rum = 4
    userRum.append(rum)
    game.deleteContent('rum.data')
    for value in userRum:
        fhand = open('rum.data', 'a')
        fhand.write(str(value))
        fhand.close()
        userRum = list()

    count = 0
    chanser = 2
    while count <= 1:
        if ((myAnswer == 'i') or (myAnswer == 'info')):
            print("\nBuzzQuiz level fem. Temat är Sport och fritid." +\
            " Rätt svar ge dig möjligt att gå vidare till level sex.\nDu får "+str(chanser)+" chanser.")
            input("\nTryck 'Enter' för att försätta!")
            os.system('clear')
            print(theQuestion)
            spelareOneAnswer = input("--> ")
            myAnswer = spelareOneAnswer.lower()
            continue

        elif ((myAnswer == 'h') or (myAnswer == 'hjälp')):
            print("Listan av alla kommando")
            print("-----------------------\n")
            print("i, info       Skriver ut beskrivning av 'level'.")
            print("h, hjälp      Skriver ut en lista av de kommandon som du kan göra.")
            print("fr, fram      Gå framåt till nästa rum, om det är upplåst.")
            print("ba, bak       Gå bakåt till föregående rum.")
            print("l, ledtråd    Ge en ledtråd, eller fler om det finns.")
            print("c, cheat      utför automatiskt alla frågor.")
            input("\nTryck 'Enter' för att försätta!")
            os.system('clear')
            print(theQuestion)
            spelareOneAnswer = input("--> ")
            myAnswer = spelareOneAnswer.lower()
            continue

        elif ((myAnswer == 'fr') or (myAnswer == 'fram')):
            fhand = open('openrum.data')
            data = fhand.readlines()
            fhand.close()
            #myData = len(data)
            if int(data[0]) < 50:
                print("Du kan inte gå till nästa rum! Svara rätt på frågan först!")
                input("\nTryck 'Enter' för att försätta!")
                os.system('clear')
                print(theQuestion)
                spelareOneAnswer = input("--> ")
                myAnswer = spelareOneAnswer.lower()
                continue
            else:
                input("\nTryck 'Enter' för gå till nästa rum!")
                os.system('clear')
                levelMesure = 5
                print(game.startGame(levelMesure))
                return



        elif ((myAnswer == 'ba') or (myAnswer == 'bak')):
            fhand = open('rum.data')
            data = fhand.readlines()
            fhand.close()

            os.system('clear')
            levelMesure = int(data[0]) - 1
            print(game.startGame(levelMesure))
            return

        elif ((myAnswer == 'l') or (myAnswer == 'ledtråd')):
            alternativOne = ["Min pappa har 8 gånger min ålder när jag var 5 år",\
             "Jag är född 1977, hur gammal är jag?",\
              "Ett jämnt tal mindre än 50"]
            alternativTwo = ["Det gränsar i norr mot Danmark, i öster mot Polen,"+\
            " i söder mot Schweiz, samt i väster mot Frankrike.",\
            "Är Europas sjunde största land.", "Styrs genom parlamentarisk demokrati."]
            alternativThree = ["I söder har landet även en maritim gräns mot Tunisien, Malta och Libyen.",\
            "Vatikan", "Liguam latina ardua est."]
            if theQuestion == question[0]:
                ledtrod = random.choice(alternativOne)
                print("\n" + ledtrod + "\n")
                input("\nTryck 'Enter' för att försätta!")
                os.system('clear')
                print(theQuestion)
                spelareOneAnswer = input("--> ")
                myAnswer = spelareOneAnswer.lower()
                continue
            elif theQuestion == question[1]:
                ledtrod = random.choice(alternativTwo)
                print("\n" + ledtrod + "\n")
                input("\nTryck 'Enter' för att försätta!")
                os.system('clear')
                print(theQuestion)
                spelareOneAnswer = input("--> ")
                myAnswer = spelareOneAnswer.lower()
                continue
            else:
                ledtrod = random.choice(alternativThree)
                print("\n" + ledtrod + "\n")
                input("\nTryck 'Enter' för att försätta!")
                os.system('clear')
                print(theQuestion)
                spelareOneAnswer = input("--> ")
                myAnswer = spelareOneAnswer.lower()
                continue
        elif ((myAnswer == 'c') or (myAnswer == 'cheat')):
            print("haha :-D din lilla fuskare!")

            ##spara betyg
            ##-----------
            ##
            fhand = open('openrum.data')
            data = fhand.readlines()
            fhand.close()
            myData = len(data)

            betyg = 50
            userBetyg = list()
            userBetyg.append(betyg)

            if int(myData) == 0:
                game.deleteContent('openrum.data')
                for value in userBetyg:
                    fhand = open('openrum.data', 'a')
                    fhand.write(str(value))
                    fhand.close()
                    userBetyg = list()
            elif int(data[0]) > betyg:
                pass
            else:
                game.deleteContent('openrum.data')
                for value in userBetyg:
                    fhand = open('openrum.data', 'a')
                    fhand.write(str(value))
                    fhand.close()
                    userBetyg = list()

            input("\nTryck 'Enter' för att börja på level fem!")
            os.system('clear')
            levelMesure = 5
            print(game.startGame(levelMesure))
            return

        elif myAnswer == rightAnswer:
            print("\n%s är korrekt"%(spelareOneAnswer))

            ##spara betyg
            ##-----------
            ##
            fhand = open('openrum.data')
            data = fhand.readlines()
            fhand.close()
            myData = len(data)

            betyg = 50
            userBetyg = list()
            userBetyg.append(betyg)

            if int(myData) == 0:
                game.deleteContent('openrum.data')
                for value in userBetyg:
                    fhand = open('openrum.data', 'a')
                    fhand.write(str(value))
                    fhand.close()
                    userBetyg = list()
            elif int(data[0]) > betyg:
                pass
            else:
                game.deleteContent('openrum.data')
                for value in userBetyg:
                    fhand = open('openrum.data', 'a')
                    fhand.write(str(value))
                    fhand.close()
                    userBetyg = list()

            print("\nTryck 'f' för att försätta. 'a' för att avsluta. 's' för att spara.")
            choix = input("--> ")
            while ((choix != 's') and (choix != 'a') and (choix != 'f')):
                print("Fel val")
                choix = input("--> ")
            if choix == "a":
                print("\nAvsluta..")
                return
            elif choix == "s":
                print("\nSparat..")
                userListLevel = list()
                userListLevel.append(levelMesure)
                game.deleteContent('usersparalevel.data')
                for value in userListLevel:
                    fhand = open('usersparalevel.data', 'a')
                    fhand.write(str(value))
                    fhand.close()
                    userListLevel = list()
                return

            elif choix == 'f':
                os.system('clear')
                levelMesure = 5
                print(game.startGame(levelMesure))
                return
        else:
            if count == 1:
                break
            else:
                print("Försök igen!")
                spelareOneAnswer = input("--> ")
                myAnswer = spelareOneAnswer.lower()
                count = count + 1
                chanser = chanser - 1

    print("%s är fel"%(spelareOneAnswer))
    input("\nTryck 'Enter'")
    os.system('clear')
    print(image.gameOver())
    return




##
# Function for level 6
##
def levelSix():
    """function for levelSix"""

    print(image.levelSixImage())
    input("\nTryck 'Enter' för att försätta!")
    os.system('clear')

    input("Tryck 'Enter' för att börja 'Quizz Buzz' del sex!")

    question = ["Pentagrammet som symbol har en historia som går långt tillbaka"+\
    " i tiden, men hur många spetsar har den?",\
     "Vad är nästa tal i denna talföljd: 9, 18, 27..?",\
     "67 + 89 - 29 + 34 = ?"]
    answer = ["5", "36", "161"]
    os.system('clear')
    print("Naturvetenskap")
    print("--------------")
    theQuestion = random.choice(question)
    print(theQuestion)

    spelareOneAnswer = input("--> ")

    rightAnswer = ""

    if theQuestion == question[0]:
        rightAnswer = answer[0]
    elif theQuestion == question[1]:
        rightAnswer = answer[1]
    elif theQuestion == question[2]:
        rightAnswer = answer[2]

    myAnswer = spelareOneAnswer.lower()

    levelMesure = 6

    ##spara vilket rum man befinner sig
    ##---------------------------------
    ##
    userRum = list()
    rum = 5
    userRum.append(rum)
    game.deleteContent('rum.data')
    for value in userRum:
        fhand = open('rum.data', 'a')
        fhand.write(str(value))
        fhand.close()
        userRum = list()

    count = 0
    chanser = 2
    while count <= 1:
        if ((myAnswer == 'i') or (myAnswer == 'info')):
            print("\nBuzzQuiz level sex. Temat är Naturvetenskap."+\
            " Rätt svar ge dig möjligt att gå vidare till den sista level.\nDu får "+str(chanser)+" chanser.")
            input("\nTryck 'Enter' för att försätta!")
            os.system('clear')
            print(theQuestion)
            spelareOneAnswer = input("--> ")
            myAnswer = spelareOneAnswer.lower()
            continue

        elif ((myAnswer == 'h') or (myAnswer == 'hjälp')):
            print("Listan av alla kommando")
            print("-----------------------\n")
            print("i, info       Skriver ut beskrivning av 'level'.")
            print("h, hjälp      Skriver ut en lista av de kommandon som du kan göra.")
            print("fr, fram      Gå framåt till nästa rum, om det är upplåst.")
            print("ba, bak       Gå bakåt till föregående rum.")
            print("l, ledtråd    Ge en ledtråd, eller fler om det finns.")
            print("c, cheat      utför automatiskt alla frågor.")
            input("\nTryck 'Enter' för att försätta!")
            os.system('clear')
            print(theQuestion)
            spelareOneAnswer = input("--> ")
            myAnswer = spelareOneAnswer.lower()
            continue

        elif ((myAnswer == 'fr') or (myAnswer == 'fram')):
            fhand = open('openrum.data')
            data = fhand.readlines()
            fhand.close()
            #myData = len(data)
            if int(data[0]) < 60:
                print("Du kan inte gå till nästa rum! Svara rätt på frågan först!")
                input("\nTryck 'Enter' för att försätta!")
                os.system('clear')
                print(theQuestion)
                spelareOneAnswer = input("--> ")
                myAnswer = spelareOneAnswer.lower()
                continue
            else:
                input("\nTryck 'Enter' för gå till nästa rum!")
                os.system('clear')
                levelMesure = 6
                print(game.startGame(levelMesure))
                return



        elif ((myAnswer == 'ba') or (myAnswer == 'bak')):
            fhand = open('rum.data')
            data = fhand.readlines()
            fhand.close()

            os.system('clear')
            levelMesure = int(data[0]) - 1
            print(game.startGame(levelMesure))
            return

        elif ((myAnswer == 'l') or (myAnswer == 'ledtråd')):
            alternativOne = ["Lika mycket som en pentagon (polygon).",\
             "Bor, atomnummer.", "Ett udda tal mindre än 10."]
            alternativTwo = ["3..", "XXXVI (romerst)", "Krypton, atomnummer"]
            alternativThree = ["1..1", "CLXI (romerst)", "10100001 (binärt)"]
            if theQuestion == question[0]:
                ledtrod = random.choice(alternativOne)
                print("\n" + ledtrod + "\n")
                input("\nTryck 'Enter' för att försätta!")
                os.system('clear')
                print(theQuestion)
                spelareOneAnswer = input("--> ")
                myAnswer = spelareOneAnswer.lower()
                continue
            elif theQuestion == question[1]:
                ledtrod = random.choice(alternativTwo)
                print("\n" + ledtrod + "\n")
                input("\nTryck 'Enter' för att försätta!")
                os.system('clear')
                print(theQuestion)
                spelareOneAnswer = input("--> ")
                myAnswer = spelareOneAnswer.lower()
                continue
            else:
                ledtrod = random.choice(alternativThree)
                print("\n" + ledtrod + "\n")
                input("\nTryck 'Enter' för att försätta!")
                os.system('clear')
                print(theQuestion)
                spelareOneAnswer = input("--> ")
                myAnswer = spelareOneAnswer.lower()
                continue
        elif ((myAnswer == 'c') or (myAnswer == 'cheat')):
            print("haha :-D din lilla fuskare!")

            ##spara betyg
            ##-----------
            ##
            fhand = open('openrum.data')
            data = fhand.readlines()
            fhand.close()
            myData = len(data)

            betyg = 60
            userBetyg = list()
            userBetyg.append(betyg)

            if int(myData) == 0:
                game.deleteContent('openrum.data')
                for value in userBetyg:
                    fhand = open('openrum.data', 'a')
                    fhand.write(str(value))
                    fhand.close()
                    userBetyg = list()
            elif int(data[0]) > betyg:
                pass
            else:
                game.deleteContent('openrum.data')
                for value in userBetyg:
                    fhand = open('openrum.data', 'a')
                    fhand.write(str(value))
                    fhand.close()
                    userBetyg = list()


            input("\nTryck 'Enter' för att börja på level fem!")
            os.system('clear')
            levelMesure = 6
            print(game.startGame(levelMesure))
            return

        elif myAnswer == rightAnswer:
            print("\n%s är korrekt"%(spelareOneAnswer))

            ##spara betyg
            ##-----------
            ##
            fhand = open('openrum.data')
            data = fhand.readlines()
            fhand.close()
            myData = len(data)

            betyg = 60
            userBetyg = list()
            userBetyg.append(betyg)

            if int(myData) == 0:
                game.deleteContent('openrum.data')
                for value in userBetyg:
                    fhand = open('openrum.data', 'a')
                    fhand.write(str(value))
                    fhand.close()
                    userBetyg = list()
            elif int(data[0]) > betyg:
                pass
            else:
                game.deleteContent('openrum.data')
                for value in userBetyg:
                    fhand = open('openrum.data', 'a')
                    fhand.write(str(value))
                    fhand.close()
                    userBetyg = list()

            print("\nTryck 'f' för att försätta. 'a' för att avsluta. 's' för att spara.")
            choix = input("--> ")
            while ((choix != 's') and (choix != 'a') and (choix != 'f')):
                print("Fel val")
                choix = input("--> ")
            if choix == "a":
                print("\nAvsluta..")
                return
            elif choix == "s":
                print("\nSparat..")
                userListLevel = list()
                userListLevel.append(levelMesure)
                game.deleteContent('usersparalevel.data')
                for value in userListLevel:
                    fhand = open('usersparalevel.data', 'a')
                    fhand.write(str(value))
                    fhand.close()
                    userListLevel = list()
                return

            elif choix == 'f':
                os.system('clear')
                levelMesure = 6
                print(game.startGame(levelMesure))
                return
        else:
            if count == 1:
                break
            else:
                print("Försök igen!")
                spelareOneAnswer = input("--> ")
                myAnswer = spelareOneAnswer.lower()
                count = count + 1
                chanser = chanser - 1

    print("%s är fel"%(spelareOneAnswer))
    input("\nTryck 'Enter'")
    os.system('clear')
    print(image.gameOver())
    return



##
# Function for level 7
##
def levelSeven():
    """function for levelSeven"""

    print(image.levelSevenImage())
    input("\nTryck 'Enter' för att försätta!")
    os.system('clear')

    input("Tryck 'Enter' för att börja 'Quizz Buzz' del sju!")

    question = ["Den 8 Juli år 2013 stängdes en klassisk sökmotor på Internet. Vilken? ",\
     "Vem utvecklade ARPANET som är föregångaren till dagens globala internet?",\
     "När dataspelet Grand Theft Auto V lanserades den 17 september år 2013 drog"+\
     " det in över $ 800.000.000 redan samma dag. Vad heter spelets utvecklare?"]
    answer = ["altavista", "usa", "rockstar"]
    os.system('clear')
    print("Dator-och internet")
    print("------------------")
    theQuestion = random.choice(question)
    print(theQuestion)

    spelareOneAnswer = input("--> ")

    rightAnswer = ""

    if theQuestion == question[0]:
        rightAnswer = answer[0]
    elif theQuestion == question[1]:
        rightAnswer = answer[1]
    elif theQuestion == question[2]:
        rightAnswer = answer[2]

    myAnswer = spelareOneAnswer.lower()

    levelMesure = 7

    ##spara vilket rum man befinner sig
    ##---------------------------------
    ##
    userRum = list()
    rum = 6
    userRum.append(rum)
    game.deleteContent('rum.data')
    for value in userRum:
        fhand = open('rum.data', 'a')
        fhand.write(str(value))
        fhand.close()
        userRum = list()

    count = 0
    chanser = 1
    while count < 1:
        if ((myAnswer == 'i') or (myAnswer == 'info')):
            print("\nBuzzQuiz Final. Temat är Dator-och internet."+\
            " Rätt svar ger möjligt att vinna hela spelet.\nDu får nu "+str(chanser)+" chans.")
            input("\nTryck 'Enter' för att försätta!")
            os.system('clear')
            print(theQuestion)
            spelareOneAnswer = input("--> ")
            myAnswer = spelareOneAnswer.lower()
            continue

        elif ((myAnswer == 'h') or (myAnswer == 'hjälp')):
            print("Listan av alla kommando")
            print("-----------------------\n")
            print("i, info       Skriver ut beskrivning av 'level'.")
            print("h, hjälp      Skriver ut en lista av de kommandon som du kan göra.")
            print("fr, fram      Gå framåt till nästa rum, om det är upplåst.")
            print("ba, bak       Gå bakåt till föregående rum.")
            print("l, ledtråd    Ge en ledtråd, eller fler om det finns.")
            print("c, cheat      utför automatiskt alla frågor.")
            input("\nTryck 'Enter' för att försätta!")
            os.system('clear')
            print(theQuestion)
            spelareOneAnswer = input("--> ")
            myAnswer = spelareOneAnswer.lower()
            continue


        elif ((myAnswer == 'fr') or (myAnswer == 'fram')):
            print("Du befinner dig på rum 7! Den sista nivån!")
            input("\nTryck 'Enter' för att försätta!")
            os.system('clear')
            print(theQuestion)
            spelareOneAnswer = input("--> ")
            myAnswer = spelareOneAnswer.lower()
            continue

        elif ((myAnswer == 'ba') or (myAnswer == 'bak')):
            fhand = open('rum.data')
            data = fhand.readlines()
            fhand.close()

            os.system('clear')
            levelMesure = int(data[0]) - 1
            print(game.startGame(levelMesure))
            return


        elif ((myAnswer == 'l') or (myAnswer == 'ledtråd')):
            alternativOne = ["Av Digital Equipment Corporation (DEC).",\
             "I maj 2008 bytte tjänsten namn till Yahoo! Babel Fish.",\
              "Köptes upp i februari 2003 av Overture Services."]
            alternativTwo = ["Yes we can", "John Kennedy", "Uncle sam"]
            alternativThree = ["Rockstjärna", "Rock and roll", "Elvis Presley"]
            if theQuestion == question[0]:
                ledtrod = random.choice(alternativOne)
                print("\n" + ledtrod + "\n")
                input("\nTryck 'Enter' för att försätta!")
                os.system('clear')
                print(theQuestion)
                spelareOneAnswer = input("--> ")
                myAnswer = spelareOneAnswer.lower()
                continue
            elif theQuestion == question[1]:
                ledtrod = random.choice(alternativTwo)
                print("\n" + ledtrod + "\n")
                input("\nTryck 'Enter' för att försätta!")
                os.system('clear')
                print(theQuestion)
                spelareOneAnswer = input("--> ")
                myAnswer = spelareOneAnswer.lower()
                continue
            else:
                ledtrod = random.choice(alternativThree)
                print("\n" + ledtrod + "\n")
                input("\nTryck 'Enter' för att försätta!")
                os.system('clear')
                print(theQuestion)
                spelareOneAnswer = input("--> ")
                myAnswer = spelareOneAnswer.lower()
                continue
        elif ((myAnswer == 'c') or (myAnswer == 'cheat')):
            print("haha :-D din lilla fuskare!")
            input("\nTryck 'Enter' för att börja på level fem!")
            os.system('clear')
            levelMesure = 7
            print(game.startGame(levelMesure))
            return

        elif myAnswer == rightAnswer:
            print("\n%s är korrekt"%(spelareOneAnswer))

            print("\nTryck 'f' för att försätta. 'a' för att avsluta. 's' för att spara.")
            choix = input("--> ")
            while ((choix != 's') and (choix != 'a') and (choix != 'f')):
                print("Fel val")
                choix = input("--> ")
            if choix == "a":
                print("\nAvsluta..")
                return
            elif choix == "s":
                print("\nSparat..")
                userListLevel = list()
                userListLevel.append(levelMesure)
                game.deleteContent('usersparalevel.data')
                for value in userListLevel:
                    fhand = open('usersparalevel.data', 'a')
                    fhand.write(str(value))
                    fhand.close()
                    userListLevel = list()
                return

            elif choix == 'f':
                os.system('clear')
                levelMesure = 7
                print(game.startGame(levelMesure))
                return
        else:
            print("Försök igen!")
            spelareOneAnswer = input("--> ")
            myAnswer = spelareOneAnswer.lower()
            count = count + 1
            chanser = chanser - 1
            continue

    print("%s är fel"%(spelareOneAnswer))
    input("\nTryck 'Enter'")
    os.system('clear')
    print(image.gameOver())
    return
