import turtle

whole_world = "CountryGuesser/images/World_map_4500px.gif"


t = turtle.Turtle()
window = turtle.Screen()
window.setup(1920, 1080)


class World:
    def DrawWorld():
        window.addshape(whole_world)
        turtle.shape(whole_world)

World.DrawWorld()
turtle.mainloop()
