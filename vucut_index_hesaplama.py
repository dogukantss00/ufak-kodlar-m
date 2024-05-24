from tkinter import *

# Tkinter penceresini oluşturun ve başlığını ve boyutunu ayarlayın
window = Tk()
window.title("Index Hesaplama")
window.geometry("300x300")

# Kullanıcıdan kilo girmesini isteyen bir etiket oluşturun ve pencereye yerleştirin
label1 = Label(text="Kilonuzu giriniz")
label1.pack()

# Kullanıcının kilosunu gireceği bir giriş kutusu oluşturun ve pencereye yerleştirin
entry1 = Entry(width=10)
entry1.pack()

# Kullanıcıdan boy girmesini isteyen bir etiket oluşturun ve pencereye yerleştirin
label2 = Label(text="Boyunuzu giriniz")
label2.pack()

# Kullanıcının boyunu gireceği bir giriş kutusu oluşturun ve pencereye yerleştirin
entry2 = Entry(width=10)
entry2.pack()

# İndeksi hesaplamak için bir fonksiyon oluşturun
def hesapla():
    # Kullanıcının girdiği kilo ve boy değerlerini alın
    kilo = entry1.get()
    boy = entry2.get()

    # Eğer herhangi bir giriş alanı boşsa, hata mesajı gösterin
    if kilo == "" or boy == "":
        label3.config(text="Lütfen alanları doldurunuz")
    else:
        # Kullanıcının boyunu cm cinsine dönüştürün
        cm_boy = int(boy) / 100
        
        # Vücut kitle indeksini hesaplayın
        Index = int(kilo) / (cm_boy * cm_boy)

        # Vücut kitle indeksi kategorilerini kontrol edin ve sonucu etikete yazdırın
        if float(Index) <= 18.4:
            label3.config(text="Zayıfsınız")
        elif 18.4 <= float(Index) <= 24.99:
            label3.config(text="Normalsiniz")    
        elif 25.00 <= float(Index) <= 29.99:
            label3.config(text="Fazla kilolusunuz")  
        elif 30.00 <= float(Index) <= 34.99:
            label3.config(text="1. Derece obezsınız")
        elif 35.00 <= float(Index) <= 44.99:
            label3.config(text="2. Derece obezsınız") 
        elif float(Index) >= 45.00:
            label3.config(text="3. Derece obezsınız") 

# Hesapla düğmesini oluşturun ve fonksiyonu bağlayın
buton1 = Button(text="Hesapla", command=hesapla)
buton1.pack()

# Sonuçları gösterecek bir etiket oluşturun
label3 = Label()
label3.pack()

# Pencereyi açın ve olay döngüsünü başlatın
window.mainloop()
