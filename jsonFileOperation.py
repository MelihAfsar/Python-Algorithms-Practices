
import json

yeniListe = []

#Kullanicidan cumle girisi
cumle = input("Lutfen cumle girisi yapiniz: ")

#Kelimelerin bas harflerinin buyuk hale gelmesi ve cumlenin kelimelere parcalanmasi
cumle = cumle.title()
liste = cumle.split()

#liste.json dosyasindan okuma yapma sirasinda olusabilecek hata bulma yapisi
try:
    f = open("liste.json","r")
except(NameError,FileNotFoundError):
    print("Okumak istediginiz dosya mevcut degildir. Ya da harf hatası vardır.\Sistem yeni dosya acacaktır. Ve islemlere devam edecektir.")
    #liste.json uzantili dosyaya kelimelerin yazdirilmasi
    with open("liste.json", "w") as outfile:
        json.dump(liste, outfile)
    # exit(1)

f = open("liste.json","r")

#json formatinin python formatina donusturulesi
jsonListe = json.load(f)

#json dosyasindaki kelimelerin yeniListe ye eklenmesi
for i in jsonListe:
    yeniListe.append(i)
f.close()

#Kelimelerin arada birer bosluk olacak şekilde birleştirilmei
yeniListe = " ".join(yeniListe)
yeniListe = yeniListe.upper()

#Cumlenin yazdirilmasi
print(yeniListe)