import turtle
import time

def draw_heart():
    """Draws a static heart shape."""
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.left(50)
    turtle.forward(133)
    turtle.circle(50, 200)
    turtle.right(140)
    turtle.circle(50, 200)
    turtle.forward(133)
    turtle.end_fill()

def move_heart():
    """Moves the heart and displays 'I LIKE You'."""
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Heart Animation")
    pen = turtle.Turtle()
    pen.speed(5)
    pen.hideturtle()
    
    # Move the heart in a loop
    for i in range(10):
        pen.clear()
        pen.penup()
        pen.goto(0, 0 + i * 10)  # Move upward
        pen.pendown()
        draw_heart()
        pen.penup()
        pen.goto(0, -150)
        pen.color("white")
        pen.write("I LIKE You", align="center", font=("Arial", 24, "bold"))
        time.sleep(0.5)

    # Hold the final heart
    screen.mainloop()

# Run the animation
move_heart()
