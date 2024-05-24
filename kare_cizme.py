import turtle

#pencere oluşturma kodu
drawing_board = turtle.Screen()
#arka plan rengini burda belirliyoruz
drawing_board.bgcolor("green")
#pencere başlığı
drawing_board.title("square")


#turtle nesnemizi oluşuturuyoruz
turtle_instance = turtle.Turtle()

#nesnemizin hareketlerini belirlediğimiz kısım
#uzun yol
turtle_instance.forward(199)
turtle_instance.left(90)
turtle_instance.forward(199)
turtle_instance.left(90)
turtle_instance.forward(199)
turtle_instance.left(90)
turtle_instance.forward(199)

#kısa yol
for i in range(4):
    turtle_instance.forward(300)
    turtle_instance.right(90 )

#pencerenin kapanmamasını sağlar
turtle.done()