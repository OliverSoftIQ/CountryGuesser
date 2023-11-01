import turtle

whole_world = "CountryGuesser/images/World_map.gif"
brazil = "CountryGuesser/images/brazil.gif"
joao = "CountryGuesser/images/joaomaze.gif"

t = turtle.Turtle()
window = turtle.Screen()
window.setup(1920, 1080)


class World:
    def DrawWorld():
        turtle.bgpic(whole_world)

    def DrawBrazil():
        window.addshape(brazil)
        turtle.shape(brazil)
        window.addshape(joao)
        turtle.addshape(joao)

World.DrawWorld()

country = input("Enter a country: ")

if country == "Brazil":
    World.DrawBrazil()
else:
    pass

turtle.mainloop()
