from countriesdatabase import*


Functions.resetCountriesList()


for i in range(0,196):
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