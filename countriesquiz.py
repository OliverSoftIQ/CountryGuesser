from countriesdatabase import *
from ui import *


Functions.ResetCountriesList()
Welcome.beginning()


for i in range(0, 195):
    choice = str(input("Enter a country name: "))

    if choice in removedCountries:
        print("You have already said this country!")
    elif choice in countries:
        print(choice + " is in the world!")
        removedCountries.append(choice)
        countries.remove(choice)
        print(removedCountries)
    else:
        print(choice + " is not in the world!")
 #pussy       