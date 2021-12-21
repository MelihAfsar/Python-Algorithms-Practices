import random
## Dizi boyutu kullanicidan alinmistir.
boyut = int(input("Olusturmak istedigininz dizinin boyutunu giriniz:"))
dizi = []

## Dizi boyutuna gore icerisine rastgele sayilar yerlestirilmistir.
for i in range(boyut):
    dizi.append(random.randint(0,50))
print("Rastgele olusturulan dizi: \n",dizi)

##Toplama carpma ve ortalama islemlerini apan fonksiyon
def islemler(dizi):
    toplam = 0
    carpim = 1
    for i in range(len(dizi)):
        toplam += dizi[i]
        carpim *= dizi[i]

    ortalama = toplam / len(dizi)

    print("Toplam:\n", toplam)
    print("CarpÄ±m:\n", carpim)
    print("Ortalama:\n", ortalama)

## Dizinin buyukten kucuge siralanmasi
def diziSirala(islem):
    for i in range(len(islem)):
        for j in range(len(islem)):
            if dizi[i] > dizi[j]:
                gecici = dizi[i]
                dizi[i] = dizi[j]
                dizi[j] = gecici

    print("\nDizinin buyukten kucuge siralanmis hali:\n", dizi)

##dizide aranan degerin bulunmasi
def arananiBul(dizi):
    aranan = int(input("\nLutfen aranacak tamsayi degerinin giriniz:"))
    for i in range(len(dizi)):
        if aranan == dizi[i]:
            print("\nAradiginiz deger dizi de bulunmustur. Indis degeri: ", i)
            break
        else:
            print(i, ". indiste aradiginiz deger bulunamamistir.")

## dizideki en buyuk ve en kucuk sayilar bulunmaktadir
def kucukBuyukBul(dizi):
    i=0
    enKucuk = dizi[i]
    enBuyuk = dizi[i]
    for i in range(boyut):
        if dizi[i] >= enBuyuk:
            enBuyuk = dizi[i]
        if dizi[i] <= enKucuk:
            enKucuk = dizi[i]

    print("En buyuk eleman:" , enBuyuk)
    print("En kucuk eleman:" , enKucuk)


islemler(dizi)
diziSirala(dizi)
arananiBul(dizi)
kucukBuyukBul(dizi)