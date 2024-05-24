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


for i in range(4):
    for j in range(4):

        turtle_instance.forward(uzunluk)
        turtle_instance.right(90 )
    uzunluk=uzunluk-50


#pencerenin kapanmamasını sağlar
turtle.done()