from countriesdatabase import *
from ui import *


Welcome.beginning()

a = int(input(" "))
if a == 1:
    Functions.RestartAll()
    score = 0
    for i in range(0, 195):
        choice = str(input("Enter a country name: "))
        choice = choice.lower()
        if choice == "quit" or choice == "stop":
            quit()
        elif choice == "restart":
            print("Game Will Restart")
            Functions.RestartAll()
            score=0
        elif choice in removedCountries:
            score-=1
            print("You have already said this country!")
            print(f"Your score is now {score}")
        elif choice in countries:
            score+=1
            print(choice + " is in the world!")
            removedCountries.append(choice)
            countries.remove(choice)
            print(f"Your score is {score}")
        else:
            score-=1
            print(choice + " is not in the world!")
            print(f"Your score is now {score}")

elif a == 2:
    b = int(input("""                  Press 1 for Europe, 2 for Asia, 3 for Oceania, 4 for North America, 5 for South America and 6 for Africa(7 for a Bonus continents)"""))
    if b == 1:
        Functions.RestartEurope()
        score = 0
        for i in range(0, len(countriesInEurope)):
            choice = str(input("Enter the name of a country in Europe: "))
            choice = choice.lower()
            if choice == "quit" or choice == "stop":
                quit()
            elif choice == "restart":
                print("Game Will Restart")
                Functions.RestartEurope()
                score=0
            elif choice in removedCountries:
                score-=1
                print("You have already said this country!")
                print(f"Your score is still {score}")
            elif choice in countries:
                score+=1
                print(choice + " is in Europe!")
                removedCountries.append(choice)
                countries.remove(choice)
                print(f"Your score is {score}")
            else:
                score-=1
                print(choice + " is not in Europe!")
                print(f"Your score is now {score}")
else:
    quit()