from tkinter import *
import math
from tkinter import messagebox
import random
import time
#daire çizme fonksiyonu
def dolu(canvas,x,y,r,outline="black",fill="white"):
    canvas.create_oval(x-r, y-r, x+r, y+r, outline=outline, fill=fill)

#pencere 1 şablon kodları
window=Tk()
window.title("çark")
window.geometry("600x700+700+10")

def fonk(sayac=0):
    # İşlevin maksimum çalışma sayısı
    max_calisma_sayisi = 7

    # İşlevi tekrar çağırmak için gereken süre (milisaniye cinsinden)
    delay = 500  # 2 saniye

    # Liste elemanlarını karıştır
    random.shuffle(all_items)
    print(len(all_items))

    dilim_sayisi = len(all_items)
    aci = 360 / dilim_sayisi

    # Dilimleri çizme
    for i in range(dilim_sayisi):
        colors = ["red", "green", "blue", "yellow", "orange", "purple"]
        start_angle = i * aci  # Dilimin başlangıç açısı
        end_angle = (i + 1) * aci  # Dilimin bitiş açısı

        # Başlangıç ve bitiş noktalarını polar koordinatlardan hesaplama
        start_x = x + r * math.cos(math.radians(start_angle))
        start_y = y - r * math.sin(math.radians(start_angle))  # Tkinter canvas'inde y eksenine ters yönde hareket ettiği için - işareti kullanılır
        end_x = x + r * math.cos(math.radians(end_angle))
        end_y = y - r * math.sin(math.radians(end_angle))

        # Dilimi çizme
        # Renkler listesinden sırayla bir renk alınarak dilim çizilir
        canvas.create_arc(x-r, y-r, x+r, y+r, start=start_angle, extent=aci, outline="black", fill=colors[i % len(colors)])
        canvas.create_line(x, y, start_x, start_y, fill="black")

        # Dilim içine liste elemanını ekleme
        mid_angle = (start_angle + end_angle) / 2
        mid_x = x + (r/2) * math.cos(math.radians(mid_angle))
        mid_y = y - (r/2) * math.sin(math.radians(mid_angle))
        item = all_items[i % len(all_items)]  # Liste elemanları döngüyle dönüyor
        canvas.create_text(mid_x, mid_y, text=item, fill="black", angle=0)
        a, b, c = 500, 275, 10
        dolu(canvas, a, b, c, fill="black")
        dolu(canvas, 495, b, c, fill="black")
        dolu(canvas, 490, b, c, fill="black")
        dolu(canvas, 485, b, c, fill="red")


    # Fonksiyonu tekrar çağırma işlemi
    if sayac < max_calisma_sayisi - 1:
        window.after(delay, lambda: fonk(sayac + 1))


#pencere 2 açma fonksiyonu
def windows2():
    def devam():
        def cevir():
            fonk()


        window2.destroy()

        buton3=Button(window,text="başlat",command=cevir)
        buton3.pack()

    window.withdraw()  

    def kaydet():
        global all_items
        all_items = list(listbox.get(0, END))
        print(all_items)
        window.deiconify()
        devam()
        
    def sil():
        entry1.delete(0,END)
    #listbox ekleme komutu
    def ekle():
        deger=entry1.get()
        if deger=="":
            messagebox.showerror(title="hata",message="lütfen tüm alanları doldurun")
        else:
            listbox.insert(END,deger)

    # pencere2 şablon komutları
    window2=Tk()
    window2.geometry("800x400+600+100")
    window2.config(bg="orange")

    #listbox oluşturma
    listbox=Listbox(window2,width=40,height=400,selectmode=MULTIPLE)
    listbox.pack(side="right")

    #label oluşturma
    label2=Label(window2,text="seçimlerinizi buraya yazınız")
    label2.place(x=50,y=50)
    label2.config(bg="orange",fg="white",font="italic 20 bold")

    #entry oluşturma
    entry1=Entry(window2)
    entry1.place(x=150,y=80)
    entry1.focus_set()

    #buton oluşturma
    buton2=Button(window2,font="italic ",text="eklemek için tıklayın",command=ekle)
    buton2.place(x=140,y=150)

    buton3=Button(window2,font="italic ",text="kaydet",command=kaydet)
    buton3.place(x=200,y=200)

    buton3=Button(window2,font="italic ",text="temizle",command=sil)
    buton3.place(x=200,y=110)

    window2.mainloop()

#label oluşturma
label1=Label(text="çarkıfelek uygulamasına hoşgeldiniz",font="italic 20 bold")
label1.pack()

#ekranda çizim yapılacak olan alanın belirlendiği yer
canvas=Canvas(window,width=600,height=500)
canvas.pack()

#dairenin x,y merkez nokta ve r z yarıcap değeri
x,y,r,z=300,250,200,10

# İçi dolu daireyi çizme
dolu(canvas, x, y, r,fill="white")
dolu(canvas,x,y,z,fill="black")

#listbox oluşturma
buton=Button(text="eklemek istediğiniz şeyler için tıklayın",command=windows2)
buton.pack()

window.mainloop()  
