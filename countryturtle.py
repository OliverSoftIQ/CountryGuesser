import turtle

whole_world = "images/World_map.gif"
brazil = "images/brazil.gif"


t = turtle.Turtle()
window = turtle.Screen()
window.setup(1920, 1080)


class World:
    def DrawWorld():
        window.addshape(whole_world)
        turtle.shape(whole_world)

    def DrawBrazil():
        window.addshape(brazil)
        turtle.shape(brazil)

World.DrawWorld()

country = input("Enter a country: ")

if country == "Brazil":
    World.DrawBrazil()
else:
    pass

turtle.mainloop()
