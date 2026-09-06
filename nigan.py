import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("RCB Design")

# Create the turtle
t = turtle.Turtle()
t.speed(3)
t.pensize(5)

# Draw Red and Gold/Yellow circular badge theme
t.penup()
t.goto(0, -100)
t.pendown()
t.color("#EC1C24")  # RCB Red
t.begin_fill()
t.circle(100)
t.end_fill()

# Draw inner black circle
t.penup()
t.goto(0, -70)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(70)
t.end_fill()

# Write RCB text
t.penup()
t.goto(0, -25)
t.color("gold")
t.align = "center"
t.write("RCB", align="center", font=("Arial", 36, "bold"))

# Hide turtle
t.hideturtle()
turtle.done()
