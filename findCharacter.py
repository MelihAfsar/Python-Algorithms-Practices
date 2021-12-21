## Kullanicidan  metin girilmesi istenmistir.
mesaj = input("Lutfen bir mesaj giriniz:")
print("Girmis oldugunuz mesaj: \n" , mesaj)
karakter = input("Mesaj icerisinde aramak istediginiz karakteri giriniz: ")

## karakterBul fonksiyonu ile metinde tek tek gezilerek istenen karakter aranir.
def karakterBul(mesaj , karakter):
    bulunduMu = 0
    for i in range(len(mesaj)):
        if mesaj[i] == karakter:
            bulunduMu = 1
            print("Aradiginiz ", karakter, " karakteri ", i, ". indiste bulunmustur")

    if (bulunduMu == 0):
        print("Aradiginiz karakter malesef bulunamadi")

karakterBul(mesaj,karakter)