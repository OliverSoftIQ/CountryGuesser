import turtle




whole_world = "CountryGuesser/images/World_map.gif"
brazil = "CountryGuesser/images/brazil.gif"
test = "CountryGuesser/images/test.gif"

t = turtle.Turtle()
window = turtle.Screen()
window.setup(1920, 1080)


class World:
    def DrawWorld():
        turtle.bgpic(whole_world)

    def DrawBrazil():
        window.register_shape(brazil)
        t.shape(brazil)
    
    def DrawTest():
        turtle.Turtle()
        window.register_shape(test)
        turtle.shape(test)

World.DrawWorld()


country = input("Enter a country: ")

if country == "Brazil":
    World.DrawBrazil()
else:
    pass

turtle.mainloop()

