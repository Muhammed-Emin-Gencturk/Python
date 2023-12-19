#Random Kütüphanesini Kodumuza Ekliyoruz
import random
#Kullanıcı Adı Sistemi(opsiyonel)
USERNAME = input("Kullanıcı Adı Belirle ")
PASSWORD = input("Şifre Adı Belirle ")
print("Sisteme Başarıyla Kaydoldun ")
#Başlangıç Komutu İstenmesi
ask = input("Giriş yapmak istiyormusun? ")
if ask == "evet":
    kullanıcı = input("Kullanıcı Adın Neydi ")
    if kullanıcı == USERNAME:
        print("Kullanıcı Adı Doğru ")
        sifre = input("Şifren Neydi ")
        if sifre == PASSWORD : 
            print("Sisteme Hoşgeldin ")
            #Döngüye Alınıp Sorulması İtenen Kelimeler İnput Olarak Alınyor
            bir = input("Atamak İstediğin İlk Kelime Nedir ")
            i1 = input("Türkçesi ")
            iki = input("Atamak İstediğin İkinci Kelime Nedir ")
            i2 = input("Türkçesi ")
            üç= input("Atamak İstediğin Üçüncü Kelime Nedir ")
            i3 = input("Türkçesi ")
            dört = input("Atamak İstediğin Dördüncü Kelime Nedir ")
            i4 = input("Türkçesi ")
            beş = input("Atamak İstediğin Beşinci Kelime Nedir ")
            i5 = input("Türkçesi ")
            altı = input("Atamak İstediğin Altıncı Kelime Nedir ")
            i6 = input("Türkçesi ")
            yedi = input("Atamak İstediğin Yedinci Kelime Nedir ")
            i7 = input("Türkçesi ")
            sekiz = input("Atamak İstediğin Sekizinci Kelime Nedir ")
            i8 = input("Türkçesi ")
            dokuz = input("Atamak İstediğin Dokuzuncu Kelime Nedir ")
            i9 = input("Türkçesi ")
            on = input("Atamak İstediğin Onuncu Kelime Nedir ")
            i10 = input("Türkçesi ")
            #Başlangıç Komutu İstenmesi
            başlangıç = input("Başlayalım mı?")
            if başlangıç == "evet":
                #Rastgele Sayılar Alınıyor ve Sayıların Kelimelere Karşılık Gelmesi Sağlanıyor(def komutu ile kısaltılıp loopa alınabilir, burada açıklayıcı olması adına tek tek yazılmıştır)
                seçim = random.randint(1,10)
                if seçim == 1:
                    print(bir , "Kelimesinin türkçesi nedir")
                    cevap1 = input("")
                    if cevap1 == i1:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i1)
                if seçim == 2:
                    print(iki , "Kelimesinin türkçesi nedir")
                    cevap2 = input("")
                    if cevap2 == i2:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i2)
                if seçim == 3:
                    print(üç , "Kelimesinin türkçesi nedir")
                    cevap3 = input("")
                    if cevap3 == i3:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i3)
                if seçim == 4:
                    print(dört , "Kelimesinin türkçesi nedir")
                    cevap4 = input("")
                    if cevap4 == i4:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i4)
                if seçim == 5:
                    print(beş , "Kelimesinin türkçesi nedir")
                    cevap5 = input("")
                    if cevap5 == i5:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i5)
                if seçim == 6:
                    print(altı , "Kelimesinin türkçesi nedir")
                    cevap6 = input("")
                    if cevap6 == i6:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i6)
                if seçim == 7:
                    print(yedi , "Kelimesinin türkçesi nedir")
                    cevap7 = input("")
                    if cevap7 == i7:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i7)
                if seçim == 8:
                    print(sekiz , "Kelimesinin türkçesi nedir")
                    cevap8 = input("")
                    if cevap8 == i8:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i8)
                if seçim == 9:
                    print(dokuz , "Kelimesinin türkçesi nedir")
                    cevap9 = input("")
                    if cevap9 == i9:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i9)
                if seçim == 10:
                    print(on , "Kelimesinin türkçesi nedir")
                    cevap10 = input("")
                    if cevap10 == i10:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i10)
                seçim = random.randint(1,10)
                if seçim == 1:
                    print(bir , "Kelimesinin türkçesi nedir")
                    cevap1 = input("")
                    if cevap1 == i1:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i1)
                if seçim == 2:
                    print(iki , "Kelimesinin türkçesi nedir")
                    cevap2 = input("")
                    if cevap2 == i2:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i2)
                if seçim == 3:
                    print(üç , "Kelimesinin türkçesi nedir")
                    cevap3 = input("")
                    if cevap3 == i3:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i3)
                if seçim == 4:
                    print(dört , "Kelimesinin türkçesi nedir")
                    cevap4 = input("")
                    if cevap4 == i4:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i4)
                if seçim == 5:
                    print(beş , "Kelimesinin türkçesi nedir")
                    cevap5 = input("")
                    if cevap5 == i5:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i5)
                if seçim == 6:
                    print(altı , "Kelimesinin türkçesi nedir")
                    cevap6 = input("")
                    if cevap6 == i6:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i6)
                if seçim == 7:
                    print(yedi , "Kelimesinin türkçesi nedir")
                    cevap7 = input("")
                    if cevap7 == i7:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i7)
                if seçim == 8:
                    print(sekiz , "Kelimesinin türkçesi nedir")
                    cevap8 = input("")
                    if cevap8 == i8:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i8)
                if seçim == 9:
                    print(dokuz , "Kelimesinin türkçesi nedir")
                    cevap9 = input("")
                    if cevap9 == i9:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i9)
                if seçim == 10:
                    print(on , "Kelimesinin türkçesi nedir")
                    cevap10 = input("")
                    if cevap10 == i10:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i10)
                seçim = random.randint(1,10)
                if seçim == 1:
                    print(bir , "Kelimesinin türkçesi nedir")
                    cevap1 = input("")
                    if cevap1 == i1:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i1)
                if seçim == 2:
                    print(iki , "Kelimesinin türkçesi nedir")
                    cevap2 = input("")
                    if cevap2 == i2:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i2)
                if seçim == 3:
                    print(üç , "Kelimesinin türkçesi nedir")
                    cevap3 = input("")
                    if cevap3 == i3:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i3)
                if seçim == 4:
                    print(dört , "Kelimesinin türkçesi nedir")
                    cevap4 = input("")
                    if cevap4 == i4:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i4)
                if seçim == 5:
                    print(beş , "Kelimesinin türkçesi nedir")
                    cevap5 = input("")
                    if cevap5 == i5:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i5)
                if seçim == 6:
                    print(altı , "Kelimesinin türkçesi nedir")
                    cevap6 = input("")
                    if cevap6 == i6:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i6)
                if seçim == 7:
                    print(yedi , "Kelimesinin türkçesi nedir")
                    cevap7 = input("")
                    if cevap7 == i7:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i7)
                if seçim == 8:
                    print(sekiz , "Kelimesinin türkçesi nedir")
                    cevap8 = input("")
                    if cevap8 == i8:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i8)
                if seçim == 9:
                    print(dokuz , "Kelimesinin türkçesi nedir")
                    cevap9 = input("")
                    if cevap9 == i9:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i9)
                if seçim == 10:
                    print(on , "Kelimesinin türkçesi nedir")
                    cevap10 = input("")
                    if cevap10 == i10:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i10)
                seçim = random.randint(1,10)
                if seçim == 1:
                    print(bir , "Kelimesinin türkçesi nedir")
                    cevap1 = input("")
                    if cevap1 == i1:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i1)
                if seçim == 2:
                    print(iki , "Kelimesinin türkçesi nedir")
                    cevap2 = input("")
                    if cevap2 == i2:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i2)
                if seçim == 3:
                    print(üç , "Kelimesinin türkçesi nedir")
                    cevap3 = input("")
                    if cevap3 == i3:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i3)
                if seçim == 4:
                    print(dört , "Kelimesinin türkçesi nedir")
                    cevap4 = input("")
                    if cevap4 == i4:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i4)
                if seçim == 5:
                    print(beş , "Kelimesinin türkçesi nedir")
                    cevap5 = input("")
                    if cevap5 == i5:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i5)
                if seçim == 6:
                    print(altı , "Kelimesinin türkçesi nedir")
                    cevap6 = input("")
                    if cevap6 == i6:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i6)
                if seçim == 7:
                    print(yedi , "Kelimesinin türkçesi nedir")
                    cevap7 = input("")
                    if cevap7 == i7:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i7)
                if seçim == 8:
                    print(sekiz , "Kelimesinin türkçesi nedir")
                    cevap8 = input("")
                    if cevap8 == i8:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i8)
                if seçim == 9:
                    print(dokuz , "Kelimesinin türkçesi nedir")
                    cevap9 = input("")
                    if cevap9 == i9:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i9)
                if seçim == 10:
                    print(on , "Kelimesinin türkçesi nedir")
                    cevap10 = input("")
                    if cevap10 == i10:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i10)
                seçim = random.randint(1,10)
                if seçim == 1:
                    print(bir , "Kelimesinin türkçesi nedir")
                    cevap1 = input("")
                    if cevap1 == i1:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i1)
                if seçim == 2:
                    print(iki , "Kelimesinin türkçesi nedir")
                    cevap2 = input("")
                    if cevap2 == i2:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i2)
                if seçim == 3:
                    print(üç , "Kelimesinin türkçesi nedir")
                    cevap3 = input("")
                    if cevap3 == i3:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i3)
                if seçim == 4:
                    print(dört , "Kelimesinin türkçesi nedir")
                    cevap4 = input("")
                    if cevap4 == i4:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i4)
                if seçim == 5:
                    print(beş , "Kelimesinin türkçesi nedir")
                    cevap5 = input("")
                    if cevap5 == i5:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i5)
                if seçim == 6:
                    print(altı , "Kelimesinin türkçesi nedir")
                    cevap6 = input("")
                    if cevap6 == i6:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i6)
                if seçim == 7:
                    print(yedi , "Kelimesinin türkçesi nedir")
                    cevap7 = input("")
                    if cevap7 == i7:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i7)
                if seçim == 8:
                    print(sekiz , "Kelimesinin türkçesi nedir")
                    cevap8 = input("")
                    if cevap8 == i8:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i8)
                if seçim == 9:
                    print(dokuz , "Kelimesinin türkçesi nedir")
                    cevap9 = input("")
                    if cevap9 == i9:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i9)
                if seçim == 10:
                    print(on , "Kelimesinin türkçesi nedir")
                    cevap10 = input("")
                    if cevap10 == i10:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i10)
                seçim = random.randint(1,10)
                if seçim == 1:
                    print(bir , "Kelimesinin türkçesi nedir")
                    cevap1 = input("")
                    if cevap1 == i1:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i1)
                if seçim == 2:
                    print(iki , "Kelimesinin türkçesi nedir")
                    cevap2 = input("")
                    if cevap2 == i2:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i2)
                if seçim == 3:
                    print(üç , "Kelimesinin türkçesi nedir")
                    cevap3 = input("")
                    if cevap3 == i3:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i3)
                if seçim == 4:
                    print(dört , "Kelimesinin türkçesi nedir")
                    cevap4 = input("")
                    if cevap4 == i4:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i4)
                if seçim == 5:
                    print(beş , "Kelimesinin türkçesi nedir")
                    cevap5 = input("")
                    if cevap5 == i5:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i5)
                if seçim == 6:
                    print(altı , "Kelimesinin türkçesi nedir")
                    cevap6 = input("")
                    if cevap6 == i6:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i6)
                if seçim == 7:
                    print(yedi , "Kelimesinin türkçesi nedir")
                    cevap7 = input("")
                    if cevap7 == i7:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i7)
                if seçim == 8:
                    print(sekiz , "Kelimesinin türkçesi nedir")
                    cevap8 = input("")
                    if cevap8 == i8:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i8)
                if seçim == 9:
                    print(dokuz , "Kelimesinin türkçesi nedir")
                    cevap9 = input("")
                    if cevap9 == i9:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i9)
                if seçim == 10:
                    print(on , "Kelimesinin türkçesi nedir")
                    cevap10 = input("")
                    if cevap10 == i10:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i10)
                seçim = random.randint(1,10)
                if seçim == 1:
                    print(bir , "Kelimesinin türkçesi nedir")
                    cevap1 = input("")
                    if cevap1 == i1:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i1)
                if seçim == 2:
                    print(iki , "Kelimesinin türkçesi nedir")
                    cevap2 = input("")
                    if cevap2 == i2:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i2)
                if seçim == 3:
                    print(üç , "Kelimesinin türkçesi nedir")
                    cevap3 = input("")
                    if cevap3 == i3:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i3)
                if seçim == 4:
                    print(dört , "Kelimesinin türkçesi nedir")
                    cevap4 = input("")
                    if cevap4 == i4:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i4)
                if seçim == 5:
                    print(beş , "Kelimesinin türkçesi nedir")
                    cevap5 = input("")
                    if cevap5 == i5:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i5)
                if seçim == 6:
                    print(altı , "Kelimesinin türkçesi nedir")
                    cevap6 = input("")
                    if cevap6 == i6:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i6)
                if seçim == 7:
                    print(yedi , "Kelimesinin türkçesi nedir")
                    cevap7 = input("")
                    if cevap7 == i7:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i7)
                if seçim == 8:
                    print(sekiz , "Kelimesinin türkçesi nedir")
                    cevap8 = input("")
                    if cevap8 == i8:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i8)
                if seçim == 9:
                    print(dokuz , "Kelimesinin türkçesi nedir")
                    cevap9 = input("")
                    if cevap9 == i9:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i9)
                if seçim == 10:
                    print(on , "Kelimesinin türkçesi nedir")
                    cevap10 = input("")
                    if cevap10 == i10:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i10)
                seçim = random.randint(1,10)
                if seçim == 1:
                    print(bir , "Kelimesinin türkçesi nedir")
                    cevap1 = input("")
                    if cevap1 == i1:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i1)
                if seçim == 2:
                    print(iki , "Kelimesinin türkçesi nedir")
                    cevap2 = input("")
                    if cevap2 == i2:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i2)
                if seçim == 3:
                    print(üç , "Kelimesinin türkçesi nedir")
                    cevap3 = input("")
                    if cevap3 == i3:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i3)
                if seçim == 4:
                    print(dört , "Kelimesinin türkçesi nedir")
                    cevap4 = input("")
                    if cevap4 == i4:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i4)
                if seçim == 5:
                    print(beş , "Kelimesinin türkçesi nedir")
                    cevap5 = input("")
                    if cevap5 == i5:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i5)
                if seçim == 6:
                    print(altı , "Kelimesinin türkçesi nedir")
                    cevap6 = input("")
                    if cevap6 == i6:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i6)
                if seçim == 7:
                    print(yedi , "Kelimesinin türkçesi nedir")
                    cevap7 = input("")
                    if cevap7 == i7:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i7)
                if seçim == 8:
                    print(sekiz , "Kelimesinin türkçesi nedir")
                    cevap8 = input("")
                    if cevap8 == i8:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i8)
                if seçim == 9:
                    print(dokuz , "Kelimesinin türkçesi nedir")
                    cevap9 = input("")
                    if cevap9 == i9:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i9)
                if seçim == 10:
                    print(on , "Kelimesinin türkçesi nedir")
                    cevap10 = input("")
                    if cevap10 == i10:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i10)
                seçim = random.randint(1,10)
                if seçim == 1:
                    print(bir , "Kelimesinin türkçesi nedir")
                    cevap1 = input("")
                    if cevap1 == i1:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i1)
                if seçim == 2:
                    print(iki , "Kelimesinin türkçesi nedir")
                    cevap2 = input("")
                    if cevap2 == i2:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i2)
                if seçim == 3:
                    print(üç , "Kelimesinin türkçesi nedir")
                    cevap3 = input("")
                    if cevap3 == i3:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i3)
                if seçim == 4:
                    print(dört , "Kelimesinin türkçesi nedir")
                    cevap4 = input("")
                    if cevap4 == i4:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i4)
                if seçim == 5:
                    print(beş , "Kelimesinin türkçesi nedir")
                    cevap5 = input("")
                    if cevap5 == i5:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i5)
                if seçim == 6:
                    print(altı , "Kelimesinin türkçesi nedir")
                    cevap6 = input("")
                    if cevap6 == i6:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i6)
                if seçim == 7:
                    print(yedi , "Kelimesinin türkçesi nedir")
                    cevap7 = input("")
                    if cevap7 == i7:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i7)
                if seçim == 8:
                    print(sekiz , "Kelimesinin türkçesi nedir")
                    cevap8 = input("")
                    if cevap8 == i8:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i8)
                if seçim == 9:
                    print(dokuz , "Kelimesinin türkçesi nedir")
                    cevap9 = input("")
                    if cevap9 == i9:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i9)
                if seçim == 10:
                    print(on , "Kelimesinin türkçesi nedir")
                    cevap10 = input("")
                    if cevap10 == i10:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i10)
                seçim = random.randint(1,10)
                if seçim == 1:
                    print(bir , "Kelimesinin türkçesi nedir")
                    cevap1 = input("")
                    if cevap1 == i1:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i1)
                if seçim == 2:
                    print(iki , "Kelimesinin türkçesi nedir")
                    cevap2 = input("")
                    if cevap2 == i2:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i2)
                if seçim == 3:
                    print(üç , "Kelimesinin türkçesi nedir")
                    cevap3 = input("")
                    if cevap3 == i3:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i3)
                if seçim == 4:
                    print(dört , "Kelimesinin türkçesi nedir")
                    cevap4 = input("")
                    if cevap4 == i4:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i4)
                if seçim == 5:
                    print(beş , "Kelimesinin türkçesi nedir")
                    cevap5 = input("")
                    if cevap5 == i5:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i5)
                if seçim == 6:
                    print(altı , "Kelimesinin türkçesi nedir")
                    cevap6 = input("")
                    if cevap6 == i6:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i6)
                if seçim == 7:
                    print(yedi , "Kelimesinin türkçesi nedir")
                    cevap7 = input("")
                    if cevap7 == i7:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i7)
                if seçim == 8:
                    print(sekiz , "Kelimesinin türkçesi nedir")
                    cevap8 = input("")
                    if cevap8 == i8:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i8)
                if seçim == 9:
                    print(dokuz , "Kelimesinin türkçesi nedir")
                    cevap9 = input("")
                    if cevap9 == i9:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i9)
                if seçim == 10:
                    print(on , "Kelimesinin türkçesi nedir")
                    cevap10 = input("")
                    if cevap10 == i10:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i10)
                seçim = random.randint(1,10)
                if seçim == 1:
                    print(bir , "Kelimesinin türkçesi nedir")
                    cevap1 = input("")
                    if cevap1 == i1:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i1)
                if seçim == 2:
                    print(iki , "Kelimesinin türkçesi nedir")
                    cevap2 = input("")
                    if cevap2 == i2:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i2)
                if seçim == 3:
                    print(üç , "Kelimesinin türkçesi nedir")
                    cevap3 = input("")
                    if cevap3 == i3:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i3)
                if seçim == 4:
                    print(dört , "Kelimesinin türkçesi nedir")
                    cevap4 = input("")
                    if cevap4 == i4:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i4)
                if seçim == 5:
                    print(beş , "Kelimesinin türkçesi nedir")
                    cevap5 = input("")
                    if cevap5 == i5:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i5)
                if seçim == 6:
                    print(altı , "Kelimesinin türkçesi nedir")
                    cevap6 = input("")
                    if cevap6 == i6:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i6)
                if seçim == 7:
                    print(yedi , "Kelimesinin türkçesi nedir")
                    cevap7 = input("")
                    if cevap7 == i7:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i7)
                if seçim == 8:
                    print(sekiz , "Kelimesinin türkçesi nedir")
                    cevap8 = input("")
                    if cevap8 == i8:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i8)
                if seçim == 9:
                    print(dokuz , "Kelimesinin türkçesi nedir")
                    cevap9 = input("")
                    if cevap9 == i9:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i9)
                if seçim == 10:
                    print(on , "Kelimesinin türkçesi nedir")
                    cevap10 = input("")
                    if cevap10 == i10:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i10)
                seçim = random.randint(1,10)
                if seçim == 1:
                    print(bir , "Kelimesinin türkçesi nedir")
                    cevap1 = input("")
                    if cevap1 == i1:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i1)
                if seçim == 2:
                    print(iki , "Kelimesinin türkçesi nedir")
                    cevap2 = input("")
                    if cevap2 == i2:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i2)
                if seçim == 3:
                    print(üç , "Kelimesinin türkçesi nedir")
                    cevap3 = input("")
                    if cevap3 == i3:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i3)
                if seçim == 4:
                    print(dört , "Kelimesinin türkçesi nedir")
                    cevap4 = input("")
                    if cevap4 == i4:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i4)
                if seçim == 5:
                    print(beş , "Kelimesinin türkçesi nedir")
                    cevap5 = input("")
                    if cevap5 == i5:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i5)
                if seçim == 6:
                    print(altı , "Kelimesinin türkçesi nedir")
                    cevap6 = input("")
                    if cevap6 == i6:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i6)
                if seçim == 7:
                    print(yedi , "Kelimesinin türkçesi nedir")
                    cevap7 = input("")
                    if cevap7 == i7:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i7)
                if seçim == 8:
                    print(sekiz , "Kelimesinin türkçesi nedir")
                    cevap8 = input("")
                    if cevap8 == i8:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i8)
                if seçim == 9:
                    print(dokuz , "Kelimesinin türkçesi nedir")
                    cevap9 = input("")
                    if cevap9 == i9:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i9)
                if seçim == 10:
                    print(on , "Kelimesinin türkçesi nedir")
                    cevap10 = input("")
                    if cevap10 == i10:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i10)
                seçim = random.randint(1,10)
                if seçim == 1:
                    print(bir , "Kelimesinin türkçesi nedir")
                    cevap1 = input("")
                    if cevap1 == i1:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i1)
                if seçim == 2:
                    print(iki , "Kelimesinin türkçesi nedir")
                    cevap2 = input("")
                    if cevap2 == i2:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i2)
                if seçim == 3:
                    print(üç , "Kelimesinin türkçesi nedir")
                    cevap3 = input("")
                    if cevap3 == i3:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i3)
                if seçim == 4:
                    print(dört , "Kelimesinin türkçesi nedir")
                    cevap4 = input("")
                    if cevap4 == i4:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i4)
                if seçim == 5:
                    print(beş , "Kelimesinin türkçesi nedir")
                    cevap5 = input("")
                    if cevap5 == i5:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i5)
                if seçim == 6:
                    print(altı , "Kelimesinin türkçesi nedir")
                    cevap6 = input("")
                    if cevap6 == i6:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i6)
                if seçim == 7:
                    print(yedi , "Kelimesinin türkçesi nedir")
                    cevap7 = input("")
                    if cevap7 == i7:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i7)
                if seçim == 8:
                    print(sekiz , "Kelimesinin türkçesi nedir")
                    cevap8 = input("")
                    if cevap8 == i8:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i8)
                if seçim == 9:
                    print(dokuz , "Kelimesinin türkçesi nedir")
                    cevap9 = input("")
                    if cevap9 == i9:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i9)
                if seçim == 10:
                    print(on , "Kelimesinin türkçesi nedir")
                    cevap10 = input("")
                    if cevap10 == i10:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i10)
                seçim = random.randint(1,10)
                if seçim == 1:
                    print(bir , "Kelimesinin türkçesi nedir")
                    cevap1 = input("")
                    if cevap1 == i1:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i1)
                if seçim == 2:
                    print(iki , "Kelimesinin türkçesi nedir")
                    cevap2 = input("")
                    if cevap2 == i2:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i2)
                if seçim == 3:
                    print(üç , "Kelimesinin türkçesi nedir")
                    cevap3 = input("")
                    if cevap3 == i3:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i3)
                if seçim == 4:
                    print(dört , "Kelimesinin türkçesi nedir")
                    cevap4 = input("")
                    if cevap4 == i4:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i4)
                if seçim == 5:
                    print(beş , "Kelimesinin türkçesi nedir")
                    cevap5 = input("")
                    if cevap5 == i5:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i5)
                if seçim == 6:
                    print(altı , "Kelimesinin türkçesi nedir")
                    cevap6 = input("")
                    if cevap6 == i6:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i6)
                if seçim == 7:
                    print(yedi , "Kelimesinin türkçesi nedir")
                    cevap7 = input("")
                    if cevap7 == i7:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i7)
                if seçim == 8:
                    print(sekiz , "Kelimesinin türkçesi nedir")
                    cevap8 = input("")
                    if cevap8 == i8:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i8)
                if seçim == 9:
                    print(dokuz , "Kelimesinin türkçesi nedir")
                    cevap9 = input("")
                    if cevap9 == i9:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i9)
                if seçim == 10:
                    print(on , "Kelimesinin türkçesi nedir")
                    cevap10 = input("")
                    if cevap10 == i10:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i10)
                seçim = random.randint(1,10)
                if seçim == 1:
                    print(bir , "Kelimesinin türkçesi nedir")
                    cevap1 = input("")
                    if cevap1 == i1:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i1)
                if seçim == 2:
                    print(iki , "Kelimesinin türkçesi nedir")
                    cevap2 = input("")
                    if cevap2 == i2:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i2)
                if seçim == 3:
                    print(üç , "Kelimesinin türkçesi nedir")
                    cevap3 = input("")
                    if cevap3 == i3:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i3)
                if seçim == 4:
                    print(dört , "Kelimesinin türkçesi nedir")
                    cevap4 = input("")
                    if cevap4 == i4:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i4)
                if seçim == 5:
                    print(beş , "Kelimesinin türkçesi nedir")
                    cevap5 = input("")
                    if cevap5 == i5:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i5)
                if seçim == 6:
                    print(altı , "Kelimesinin türkçesi nedir")
                    cevap6 = input("")
                    if cevap6 == i6:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i6)
                if seçim == 7:
                    print(yedi , "Kelimesinin türkçesi nedir")
                    cevap7 = input("")
                    if cevap7 == i7:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i7)
                if seçim == 8:
                    print(sekiz , "Kelimesinin türkçesi nedir")
                    cevap8 = input("")
                    if cevap8 == i8:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i8)
                if seçim == 9:
                    print(dokuz , "Kelimesinin türkçesi nedir")
                    cevap9 = input("")
                    if cevap9 == i9:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i9)
                if seçim == 10:
                    print(on , "Kelimesinin türkçesi nedir")
                    cevap10 = input("")
                    if cevap10 == i10:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i10)
                seçim = random.randint(1,10)
                if seçim == 1:
                    print(bir , "Kelimesinin türkçesi nedir")
                    cevap1 = input("")
                    if cevap1 == i1:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i1)
                if seçim == 2:
                    print(iki , "Kelimesinin türkçesi nedir")
                    cevap2 = input("")
                    if cevap2 == i2:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i2)
                if seçim == 3:
                    print(üç , "Kelimesinin türkçesi nedir")
                    cevap3 = input("")
                    if cevap3 == i3:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i3)
                if seçim == 4:
                    print(dört , "Kelimesinin türkçesi nedir")
                    cevap4 = input("")
                    if cevap4 == i4:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i4)
                if seçim == 5:
                    print(beş , "Kelimesinin türkçesi nedir")
                    cevap5 = input("")
                    if cevap5 == i5:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i5)
                if seçim == 6:
                    print(altı , "Kelimesinin türkçesi nedir")
                    cevap6 = input("")
                    if cevap6 == i6:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i6)
                if seçim == 7:
                    print(yedi , "Kelimesinin türkçesi nedir")
                    cevap7 = input("")
                    if cevap7 == i7:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i7)
                if seçim == 8:
                    print(sekiz , "Kelimesinin türkçesi nedir")
                    cevap8 = input("")
                    if cevap8 == i8:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i8)
                if seçim == 9:
                    print(dokuz , "Kelimesinin türkçesi nedir")
                    cevap9 = input("")
                    if cevap9 == i9:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i9)
                if seçim == 10:
                    print(on , "Kelimesinin türkçesi nedir")
                    cevap10 = input("")
                    if cevap10 == i10:
                        print("doğru")
                    else :
                        print("Cevap Yanlış, Doğrusu : ", i10)
                    print("Alıştırma Bitti Tebrikler")
            else:
                print("Tamam, Sonra Görüşürüz, Sistem Kapatılıyor")
                quit(0)
        else :
            print("Şifre Yanlış, Sistem Kapatılıyor ")
            quit(0)
    else :
        print("Kullanıcı Adı Yanlış, Sistem Kapatılıyor ")
        quit(0)
elif ask == "hayır":
    print("Tamam Sistemden Çıkılyor ")
else:
    print("Bu Bir Cevap Değil, Sistem Kapatılıyor ")