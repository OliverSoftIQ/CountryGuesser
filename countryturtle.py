import turtle

whole_world = "CountryGuesser/images/World_map.gif"
brazil = "CountryGuesser/images/brazil.gif"
joao = "CountryGuesser/images/joaomaze.gif"
test = "CountryGuesser/images/test.gif"

t = turtle.Turtle()
window = turtle.Screen()
window.setup(1920, 1080)


class World:
    def DrawWorld():
        turtle.bgpic(whole_world)

    def DrawBrazil():
        window.addshape(brazil)
        turtle.shape(brazil)
    
    def DrawTest():
        window.addshape(test)
        turtle.shape(test)

World.DrawWorld()


country = input("Enter a country: ")

if country == "Brazil":
    World.DrawBrazil()
    World.DrawTest()
else:
    pass

turtle.mainloop()
