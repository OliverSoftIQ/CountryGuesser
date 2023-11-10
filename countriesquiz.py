from countriesdatabase import *
from ui import *


Functions.RestartAll()
Welcome.beginning()

a = int(input(" "))
if a == 1:
    for i in range(0, 195):
        score = 0
        choice = str(input("Enter a country name: "))
        choice = choice.lower()
        if choice == "quit" or choice == "stop":
            quit()
        elif choice == "restart":
            print("Game Will Restart")
            Functions.RestartAll()
        elif choice in removedCountries:
            print("You have already said this country!")
            print(f"Your score is still {len(removedCountries)-1}")
        elif choice in countries:
            print(choice + " is in the world!")
            removedCountries.append(choice)
            countries.remove(choice)
            print(f"Your score is {len(removedCountries)}")
        else:
            print(choice + " is not in the world!")

elif a == 2:
    b = int(input("""                  Press 1 for Europe, 2 for Asia, 3 for Oceania, 4 for North America, 5 for South America and 6 for Africa(7 for a Bonus continents)"""))
    if b == 1:
        for i in range(0, len(countriesInEurope)):
            score = 0
            choice = str(input("Enter the name of a country in Europe"))
            choice = choice.lower()
            if choice == "quit" or choice == "stop":
                quit()
            elif choice == "restart":
                print("Game Will Restart")
                Functions.RestartEurope()
            elif choice in removedCountries:
                print("You have already said this country!")
                print(f"Your score is still {len(removedCountries)-1}")
            elif choice in countries:
                print(choice + " is in Europe!")
                removedCountries.append(choice)
                countries.remove(choice)
                print(f"Your score is {len(removedCountries)} in European countries")
            else:
                print(choice + " is not in Europe!")
else:
    print("Test")