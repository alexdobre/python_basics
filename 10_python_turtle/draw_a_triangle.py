import turtle


def main():
    s = turtle.Screen()
    s.bgcolor(0, 0, 0)

    t = turtle.Turtle()
    t.color('white')
    for i in range(3):
        t.forward(50)
        t.right(120)

    turtle.done()


if __name__ == '__main__':
    main()
