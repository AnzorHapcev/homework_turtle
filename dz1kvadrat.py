print('Введите кол-во квадратов')
n=int(input())
print('Введите длину стороны квадрата')
r=int(input())
import turtle
pet=turtle.Turtle()
pet.up()
pet.width(2)
pet.screen.bgcolor("orange")

def draw_square(size_square_now):
    a=4
    while a>0:
        pet.fd(size_square_now)
        pet.left(90)
        a-=1
size_square_now=r

for _ in range(n):
    pet.up()
    pet.goto(-250,-250)
    pet.down()
    draw_square(size_square_now)
    size_square_now+=r

pet.hideturtle()
input()
