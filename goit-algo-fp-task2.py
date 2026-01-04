import turtle

def draw_p_tree(branch_length, angle, level):
    if level == 0:
        return

    turtle.forward(branch_length)
    
    current_pos = turtle.pos()
    current_heading = turtle.heading()

    turtle.right(angle)
    draw_p_tree(branch_length * 0.7, angle, level - 1)

    turtle.seth(current_heading)
    turtle.penup()
    turtle.goto(current_pos)
    turtle.pendown()

    turtle.left(angle)
    draw_p_tree(branch_length * 0.7, angle, level - 1)

    turtle.penup()
    turtle.goto(current_pos)
    turtle.seth(current_heading)
    turtle.backward(branch_length)
    turtle.pendown()

def main():
    try:
        level = int(input("Вкажіть рівень рекурсії: "))
    except ValueError:
        return
    
    window = turtle.Screen()
    window.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed(0)
    t.left(90)
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.color("green")

    draw_p_tree(100, 30, level)
    window.mainloop()

if __name__ == "__main__":
    main()