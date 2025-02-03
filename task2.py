import turtle
import math

# Функція для малювання "дерева Піфагора"
def pythagoras_tree(t, length, level, angle):
    if level == 0:
        t.forward(length)
        t.backward(length)
    else:
        # Малюємо стовбур
        t.forward(length)
        
        # Переходимо до лівої гілки
        t.left(angle)
        pythagoras_tree(t, length * math.sqrt(2) / 2, level - 1, angle)
        
        # Повертаємося до основи
        t.right(2 * angle)
        
        # Малюємо праву гілку
        pythagoras_tree(t, length * math.sqrt(2) / 2, level - 1, angle)
        
        # Повертаємося в початкову позицію
        t.left(angle)
        t.backward(length)


def draw_tree(level):
    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.title("Дерево Піфагора")
    t = turtle.Turtle()
    t.speed(0)
    t.color("brown")
    t.penup()
    t.goto(0, -300)
    t.pendown()
    t.left(90)  # Орієнтуємо turtle вгору

    pythagoras_tree(t, 200, level, 45)

    turtle.done()


if __name__ == "__main__":
    try:
        level = int(input("Введіть рівень рекурсії (наприклад, 5): "))
        if level < 0:
            raise ValueError("Рівень рекурсії повинен бути цілим додатнім числом.")
        
        draw_tree(level)

    except ValueError as e:
        print(f"Помилка вводу: {e}")
    except Exception as e:
        print(f"Невідома помилка: {e}")