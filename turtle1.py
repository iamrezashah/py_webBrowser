import turtle # Allows us to use turtles

wn = turtle.Screen() # Creates a playground for turtles
wn.title('little turtle')
wn.bgcolor('lightgray')

alex = turtle.Turtle() # Create a turtle, assign to alex
alex.pensize(3)
alex.speed(10)

gam = 20
zaviye = 90
zaviye2 = 100
colors = ["red", "purple", "hotpink", "blue"]


for i in range(10):
        alex.color(colors[i%4])
        alex.forward(gam)
        alex.left(zaviye)
        alex.forward(gam)
        alex.left(zaviye)
        alex.forward(gam)
        alex.left(zaviye)
        alex.forward(gam)
        alex.left(zaviye2)
        gam += 10
        zaviye2 += 5

wn.mainloop() # Wait for user to close windo