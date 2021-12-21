import sys

sistem = int(input("Celcius --> Fahrenheit  icin 1 : Fahrenheit --> Celcius icin: 2 tuslamasi yapiniz:"))                    #Kullanicidan hangi donusumu yapmak istedigi soruluyor
if sistem == 1 or sistem == 2:                                                                                               #Program tarafindan 1 ve 2 girisi disinda giris yapilmasi istenmiyor
    sicaklik = float(input("Sicaklik degerini giriniz:"))                                                                    # 1 ya da 2 tuslanirsa sicaklik degerisoruluyor.
    if sistem == 1 :
        F = (sicaklik*9)/5+32                                                                                                #Fahrenheit tan Celcius donusum hesaplamsi
        print(sicaklik," °C, Fahrenheit çevrilmiş hali --> " , F , " °F")
    else:
        C = (sicaklik-32)*5/9                                                                                                 #Celcius tan Fahrenheit donusum hesaplamsi
        print(sicaklik, " °F, Celcius çevrilmiş hali --> ", C, " °C")
else:
    print("Hatali tuslama yaptiniz. Program sonlandiriliyor.")
    sys.exit(0)