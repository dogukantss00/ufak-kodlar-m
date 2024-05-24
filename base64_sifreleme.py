from tkinter import *
import hashlib
from tkinter import messagebox

p=Tk()
p.title("secret notes")

p.geometry("500x800+600+0")
p.resizable(width="FALSE", height="FALSE")

#hashleme
def encode():
    metin = text1.get("1.0", "end-1c")
    hash_obj = hashlib.sha256()
    hash_obj.update(metin.encode())  # Veriyi byte dizisine dönüştürüp hash'e ekliyoruz
    hash_degeri = hash_obj.hexdigest()  # Hash değerini al
    print( hash_degeri)
    #hata mesajı
    e=entr1.get()
    e1=hash_degeri
    e2=entr3.get()
    if len(e)==0 or len(e1)==0 or len(e2)==0:
        messagebox.showerror()
    else:

        try:
            with open("mysecret.txt","a")as data_file:
                data_file.write(f"\n{e}\n{e1}")
        except FileNotFoundError:
            with open("mysecret.txt","w")as data_file:
                data_file.write(f"\n{e}\n{e1}")
        finally:
            entr1.delete(0,END)
            text1.delete("1.0",END)
            entr3.delete(0,END)
    



#decode etme
def decode():
    pass

#resim ekleme
photo = PhotoImage(file="iconn.png") 
canvas=Canvas(height=300,width=200)
canvas.create_image(100,100,image=photo)
canvas.place(x=130,y=100)

#labeller entryler butonlar
label1=Label(p,text="başlik")
label1.place(x=220,y=300)

entr1=Entry(p,width=25)
entr1.place(x=130,y=330)

label2=Label(p,text="metin giriniz")
label2.place(x=200,y=360)

text1=Text(p,width=25,height=12)
text1.place(x=130,y=390)

label3=Label(p,text="şifre giriniz")
label3.place(x=200,y=620)

entr3=Entry(p,width=25)
entr3.place(x=130,y=650)

buton1=Button(p,text="şifrele",command=encode)
buton1.place(x=200,y=700)

buton2=Button(p,text="çözümle",command=decode)
buton2.place(x=190,y=750)


p.mainloop()
