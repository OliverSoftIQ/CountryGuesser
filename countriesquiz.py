from countriesdatabase import *
from ui import *


Functions.Restart()
Welcome.beginning()


for i in range(0, 195):
    choice = str(input("Enter a country name: "))
    choice = choice.lower()
    if choice == "quit" or choice == "stop":
        quit()
    elif choice == "restart":
        print("Game Will Restart")
        Functions.Restart()
    elif choice in removedCountries:
        print("You have already said this country!")
        print(f"Your score is still {len(removedCountries)}")
    elif choice in countries:
        print(choice + " is in the world!")
        removedCountries.append(choice)
        countries.remove(choice)
        print(f"Your score is {len(removedCountries)}")
    else:
        print(choice + " is not in the world!")
        