from tkinter import *


pencere=Tk()
pencere.title("haftalık program")
pencere.geometry("1400x500+300+0")



    

class Frames():
    def __init__(self,frame,x,y):
        self.frame=frame
        self.x=x
        self.y=y
    def frames(self):
        for i in range(7):
            if i%2==0:
                self.frame=Frame(pencere,width=200,height=500,bg="grey")
                self.frame.place(x=self.x,y=self.y)
                self.x+=200
            elif self.x==600:
                self.frame=Frame(pencere,width=200,height=500,bg="#09f1f9")
                self.frame.place(x=self.x,y=self.y)
                self.x+=200

            else:

                self.frame=Frame(pencere,width=200,height=500,bg="white")
                self.frame.place(x=self.x,y=self.y)
                self.x+=200

frame1=Frames("frame1",0,0)
frame1.frames()

#konular

class Gunler():

    def __init__(self,baslik,x,y,text):
        self.baslik=baslik
        self.x=x
        self.y=y
        self.text=text
    def gun(self):
        def command():
            class Ders():
                def __init__(self,isim,a,b,konu):
                    self.isim=isim
                    self.a=a 
                    self.b=b
                    self.konu=konu
                def yaz(self):
                    self.isim=Label(pencere,text=self.konu,font="italic 10",width=12)
                    self.isim.place(x=self.a,y=self.b)
                    self.b+=50
            if self.text=="Pazartesi":
               ders1=Ders("ders1",50,60,"veri dersine gir")
               ders1.yaz()
               ders2=Ders("ders2",50,110,"veri çalış")
               ders2.yaz()
               ders3=Ders("ders3",50,160,"mat1 çalış")
               ders3.yaz()
               ders4=Ders("ders4",50,210,"lojik çalış")
               ders4.yaz()
               ders5=Ders("ders5",50,260,"siber güvenlik ")
               ders5.yaz()
               ders6=Ders("ders6",50,310,"ingilizce ")
               ders6.yaz()
               ders7=Ders("ders7",50,360,"kalvye")
               ders7.yaz()   
               ders8=Ders("ders8",50,410,"python")
               ders8.yaz()                                           
            elif self.text=="Salı":
               ders1=Ders("ders1",250,60,"lineer çalış")
               ders1.yaz()
               ders2=Ders("ders2",250,110,"nesne dersine gir")
               ders2.yaz()
               ders3=Ders("ders3",250,160,"nesne çalış")
               ders3.yaz()
               ders4=Ders("ders4",250,210,"siber güvenlik")
               ders4.yaz()
               ders5=Ders("ders5",250,260,"ingilizce")
               ders5.yaz()
               ders6=Ders("ders6",250,310,"klavye")
               ders6.yaz()
               ders7=Ders("ders7",250,360,"html")
               ders7.yaz()        
            elif self.text=="Çarşamba":
               ders1=Ders("ders1",450,60,"ayrık çalış")
               ders1.yaz()
               ders2=Ders("ders2",450,110,"mikro dersine gir")
               ders2.yaz()
               ders3=Ders("ders3",450,160,"mikro çalış")
               ders3.yaz()
               ders4=Ders("ders4",450,210,"siber güvenlik")
               ders4.yaz()
               ders5=Ders("ders5",450,260,"python")
               ders5.yaz()
               ders6=Ders("ders6",450,310,"ingilizce")
               ders6.yaz()
               ders7=Ders("ders7",450,360,"klavye")
               ders7.yaz()  
               ders8=Ders("ders8",450,410,"bilimsel etik çalış")
               ders8.yaz()                     
            elif self.text=="Perşembe":
               ders1=Ders("ders1",650,60,"siber güvenlik")
               ders1.yaz()
               ders2=Ders("ders2",650,110,"python")
               ders2.yaz()
               ders3=Ders("ders3",650,160,"html")
               ders3.yaz()
               ders4=Ders("ders4",650,210,"ctf")
               ders4.yaz()
               ders5=Ders("ders5",650,260,"ingilizce")
               ders5.yaz()
               ders6=Ders("ders6",650,310,"klavye")
               ders6.yaz()
      
            elif self.text=="Cuma":
               ders1=Ders("ders1",850,60,"veri çalış")
               ders1.yaz()
               ders2=Ders("ders2",850,110,"lojik çalış")
               ders2.yaz()
               ders3=Ders("ders3",850,160,"mat1 çalış")
               ders3.yaz()
               ders4=Ders("ders4",850,210,"inilizce")
               ders4.yaz()
               ders5=Ders("ders5",850,260,"siber güvenlik")
               ders5.yaz()
               ders6=Ders("ders6",850,310,"klavye")
               ders6.yaz()
               ders7=Ders("ders7",850,360,"python")
               ders7.yaz() 
               ders8=Ders("ders8",850,410,"ctf")
               ders8.yaz()                         
            elif self.text=="Cumartesi":
               ders1=Ders("ders1",1050,60,"ayrık çalış")
               ders1.yaz()
               ders2=Ders("ders2",1050,110,"nesne çalış")
               ders2.yaz()
               ders3=Ders("ders3",1050,160,"siber güvenlik")
               ders3.yaz()
               ders4=Ders("ders4",1050,210,"ctf")
               ders4.yaz()
               ders5=Ders("ders5",1050,260,"ingilizce")
               ders5.yaz()
               ders6=Ders("ders6",1050,310,"klavye")
               ders6.yaz()
               ders7=Ders("ders7",1050,360,"html")
               ders7.yaz()                                                                    
            elif self.text=="Pazar":
               ders1=Ders("ders1",1250,60,"mikro çalış")
               ders1.yaz()
               ders2=Ders("ders2",1250,110,"etik çalış")
               ders2.yaz()
               ders3=Ders("ders3",1250,160,"ayrık çalış")
               ders3.yaz()
               ders4=Ders("ders4",1250,210,"siber güvenlik")
               ders4.yaz()
               ders5=Ders("ders5",1250,260,"ctf")
               ders5.yaz()
               ders6=Ders("ders6",1250,310,"ingilizce")
               ders6.yaz()
               ders7=Ders("ders7",1250,360,"klavye")
               ders7.yaz()  
               ders8=Ders("ders8",1250,410,"python")
               ders8.yaz()                                 
        self.baslik=Button(pencere,text=self.text,font="italic 10",width=8,command=command)
        self.baslik.place(x=self.x,y=self.y)

        

baslik1=Gunler("baslik1",50,10,"Pazartesi")
baslik1.gun()
baslik2=Gunler("baslik2",250,10,"Salı")
baslik2.gun()
baslik3=Gunler("baslik3",450,10,"Çarşamba")
baslik3.gun()
baslik4=Gunler("baslik4",650,10,"Perşembe")
baslik4.gun()
baslik5=Gunler("baslik5",850,10,"Cuma")
baslik5.gun()
baslik6=Gunler("baslik6",1050,10,"Cumartesi")
baslik6.gun()
baslik7=Gunler("baslik7",1250,10,"Pazar")
baslik7.gun()



    

pencere.mainloop()