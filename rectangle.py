import turtle

# Create the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")  # Background color

# Create a turtle object
pen = turtle.Turtle()
pen.color("blue")        # Pen color
pen.pensize(3)           # Pen thickness
pen.speed(2)             # Drawing speed (1–10, or 0 for fastest)

# Draw a square
for _ in range(4):
    pen.forward(100)     # Move forward by 100 units
    pen.right(90)        # Turn right by 90 degrees

# Finish
turtle.done()
