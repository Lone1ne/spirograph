import turtle as t
import random
tim = t.Turtle()
tim.shape("circle")
tim.color("red")
t.colormode(255)


# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# colors = ["red", "blue", "green", "pink", "orange", "black", "purple"]
#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.left(angle)
# for shape_side in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color
#
# tim.pensize(10)
tim.speed(25)
# for _ in range(500):
#     #tim.color(random.choice(colors))
#     tim.color(random_color())
#     movements = [0, 90, 180, 270]
#     tim.forward(30)
#     tim.setheading(random.choice(movements))

# for _ in range(72):
#     tim.color(random_color())
#     tim.circle(100)
#     tim.left(5)
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
draw_spirograph(5)





screen = t.Screen()
screen.exitonclick()