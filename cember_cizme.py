import turtle

#pencere oluşturma kodu
drawing_board = turtle.Screen()
#arka plan rengini burda belirliyoruz
drawing_board.bgcolor("green")
#pencere başlığı
drawing_board.title("turtle")
#turtle nesnemizi oluşuturuyoruz
turtle_instance = turtle.Turtle()


#nesnemizin hareketlerini belirlediğimiz kısım
turtle_instance.circle(199)
#pencerenin kapanmamasını sağlar
turtle.done()