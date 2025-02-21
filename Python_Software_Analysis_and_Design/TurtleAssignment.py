import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")  

# Create the first turtle for the star
star = turtle.Turtle()
star.color("yellow")  
star.pensize(3)  
star.speed(5)  

# Draw a star
for _ in range(5):
    star.forward(150)
    star.right(144)

# Hide the star turtle
star.hideturtle()

# Create a second turtle for other shapes
t = turtle.Turtle()
t.pensize(3)  
t.speed(3)

# Draw a square (Blue)
t.color("blue")  
for _ in range(4):
    t.forward(100)
    t.right(90)

# Move turtle to a new position
t.penup()
t.goto(-150, 100)
t.pendown()

# Draw a triangle (Green)
t.color("green")  
for _ in range(3):
    t.forward(100)
    t.left(120)

# Move turtle to a new position
t.penup()
t.goto(150, 100)
t.pendown()

# Draw a hexagon (Red)
t.color("red")  
for _ in range(6):
    t.forward(100)
    t.right(60)

# Move turtle to a new position
t.penup()
t.goto(0, -150)
t.pendown()

# Draw a circle (Purple)
t.color("purple")  
t.circle(100)

# Draw a flower pattern
t.color("magenta")
for _ in range(36):  # 36 circles to create a flower
    t.circle(50)
    t.right(10)  # Rotate slightly after each circle

# Hide the turtle
t.hideturtle()

# Keep the window open
turtle.done()
