# buzzQuiz-

Spelet består på 7 nivåer. Du kommer få en fråga i varje nivå.
Svarar du rätt då går du vidare till nästa 'level'.
Du måsta ha rätt på  alla sju frågor för att vinna hela spelet.

Du startar spelet genom att skriva : "python3 adventure.py".
Det finns möjligt att skicka ett antal parametrar till programmet via getopt:

* -h, --help    skriver ut en beskrivning av programmet och vilka parametrar som fungerar.
* -i, --info    skriver ut en beskrivning av spelet.
* -v, --version skriver ut versionen av spelet.
* -a, --about   skriver ut en kort beskrivning av mig.
* -c, --cheat   skriver ut minsta möjliga väg för att klara spelet
 
När du startar spelet kommer du få tre alternativ:
1. För att starta ett nytt spel.
2. För att försätta på ett pågående spel
3. För att se alla tidigare vinare

Svarar man rätt då får man tre alternativ :

* f     för att första vidare 
* a     för att avsluta spelet
* s     för att spara spelet

Det finns ett antal kommando som fungerar när spelets inleds bland annat:

1) i, info       Skriver ut beskrivning av 'level'.
2) h, hjälp      Skriver ut en lista av de kommandon som du kan göra.
3) fr, fram      Gå framåt till nästa rum, om det är upplåst.
4) ba, bak       Gå bakåt till föregående rum.
5) l, ledtråd    Ge en ledtråd, eller fler om det finns.
6) c, cheat      utför automatiskt alla frågor.
