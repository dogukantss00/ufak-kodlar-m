import turtle

#pencere oluşturma kodu
drawing_board = turtle.Screen()
#arka plan rengini burda belirliyoruz
drawing_board.bgcolor("green")
#pencere başlığı
drawing_board.title("square")


#turtle nesnemizi oluşuturuyoruz
turtle_instance = turtle.Turtle()
#çizim rengi değiştirme
turtle_instance.color("aqua")
#nesnemizin hareketlerini belirlediğimiz kısım
uzunluk= 300


def spiral (size):
    for j in range(4):

        turtle_instance.forward(size)
        turtle_instance.left(90)
        size=size-2

spiral(100)
spiral(90)
spiral(80)
spiral(70)
spiral(60)
#pencerenin kapanmamasını sağlar
turtle.done()