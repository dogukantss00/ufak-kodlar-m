import turtle

#pencere oluşturma kodu
drawing_board = turtle.Screen()
#arka plan rengini burda belirliyoruz
drawing_board.bgcolor("green")
#pencere başlığı
drawing_board.title("turtle")
#turtle nesnemizi oluşuturuyoruz
turtle_instance = turtle.Turtle()

#kaplumbağa hereketi
def turtle_forward():
    turtle_instance.forward(100)
#sağa döndürme
def rotate_right():
    turtle_instance.setheading(turtle_instance.heading()-10)
#sola döndürme
def  rotate_left():
    turtle_instance.setheading(turtle_instance.heading()+10)
#ekran temizleme
def clear_screen():
    turtle_instance.clear()
#başa dönme
def turtle_home():
    turtle_instance.up()
    turtle_instance.home()
    turtle_instance.down()
#tuş atama komutları
drawing_board.listen()
drawing_board.onkey(fun=turtle_forward,key="space")
drawing_board.onkey(fun=rotate_right,key="Down")
drawing_board.onkey(fun=rotate_left,key="Up")
drawing_board.onkey(fun=clear_screen,key="c")
drawing_board.onkey(fun=turtle_home,key="h")

turtle.done()