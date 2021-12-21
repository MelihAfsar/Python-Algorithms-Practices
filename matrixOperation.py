# #soru1
# print("***Soru1***")
# 
# def matrisOlustur(satir,sutun,matris):
#     for i in range(0, satir):
#         for j in range(0, sutun):
#             print(i, ". satir ", j, ". sutun elamanı:")
#             try:
#                 sayi = int(input())
#             except ValueError:
#                 print("Lutfen sayi deger girisi yapiniz!!!")
#             matris[i][j] = sayi
# 
# def matrisGoruntule(matris):
#     print("\nOlusturdugunuz matris:")
#     for i in range(0, satir):
#         for j in range(0, sutun):
#             print(matris[i][j], end=" ")
#         print()
# 
# def matrisKontrol(satir,sutun,matris):
#     sutunTotal = 0
#     for i in range(0, sutun):
#         total = 0
#         for j in range(0, satir):
#             if matris[j][i] != 0:
#                 break
#             else:
#                 total += 1
#         if total == sat:
#             sutunTotal += 1
#     print("\n0 iceren sutun sayisi:" ,sutunTotal)
# 
# try:
#     sutun = int(input("Lutfen olusturacaginiz matrisin sutun sayisini giriniz:"))
#     satir = int(input("Lutfen olusturacağiniz matrisin satir sayisini giriniz:"))
# except ValueError:
#     print("Lutfen sayi deger girisi yapiniz!!!")
#     exit(0)
# 
# sut = sutun
# sat = satir
# 
# matris = [[0 for x in range(sutun)] for y in range(satir)]
# 
# matrisOlustur(satir,sutun,matris)
# matrisGoruntule(matris)
# matrisKontrol(satir,sutun,matris)
# ##############################################################################################
# ##############################################################################################
# ## Soru2 f(x)=-4x2+2  ve g(x)=-x3-x2+3x+1  sonuç listesi = [2,6,-6,-14,4,4]
# 
# print("***Soru2***")
# print("f(x)=-4x2 +2  ve  g(x) = -x3 -x2 +3x +1 polinomlari carpimi:")
# f = [2, 0, -4]
# g = [1, 3, -1, -1]
# matrisUzun= [[0]*k+[i*j for i in f]+[0] * (len(g)-k) for k, j in enumerate(g)]
# uzun = len(g)-1 +len(f)
# sonuc = [sum(row[i] for row in matrisUzun) for i in range(uzun)]
# print(sonuc)
# 
# ##############################################################################################
# ##############################################################################################
# Bir a matrisinin satırlarında yanyana iki adet 0 olup olmadığını arayan ve bu duruma uyan satır
# adedini geri döndüren Python fonksiyonunu yazınız.
# (Örneğin; a = [[0,0,0,0],[0,4,0,2],[1,0,5,8],[0,0,2,3]] olarak verildiğinde, ilk ve son satırlarda yanyana
# 0 sayısı yer aldığı için fonksiyon 2 sonucunu döndürmelidir).
# ##############################################################################################
# #Soru3
# 
# print("***Soru3***")
# def matrisOlustur(satir,sutun,matris):
#     for i in range(0, satir):
#         for j in range(0, sutun):
#             print(i, ". satir ", j, ". sutun elamanı:")
#             try:
#                 sayi = int(input())
#             except ValueError:
#                 print("Lutfen sayi deger girisi yapiniz!!!")
#             matris[i][j] = sayi
# 
# def matrisGoruntule(matris):
#     print("\nOlusturdugunuz matris:")
#     for i in range(0, satir):
#         for j in range(0, sutun):
#             print(matris[i][j], end=" ")
#         print()
# 
# def matrisKontrol(satir,sutun,matris):
#     satirTotal = 0
#     for i in range(0, satir):
#         isZero = False
#         total = 0
#         for j in range(0, sutun):
#             if matris[i][j] != 0:
#                 isZero = False
#             else:
#                 if isZero:
#                     total += 1
#                 isZero = True
#             if total == 1:
#                 satirTotal += 1
#                 break
#     print("\nArt arda 0 iceren satir sayisi:" ,satirTotal)
# 
# try:
#     sutun = int(input("Lutfen olusturacaginiz matrisin sutun sayisini giriniz:"))
#     satir = int(input("Lutfen olusturacağiniz matrisin satir sayisini giriniz:"))
# except ValueError:
#     print("Lutfen sayi deger girisi yapiniz!!!")
#     exit(0)
# 
# sut = sutun
# sat = satir
# 
# matris = [[0 for x in range(sutun)] for y in range(satir)]
# 
# matrisOlustur(satir,sutun,matris)
# matrisGoruntule(matris)
# matrisKontrol(satir,sutun,matris)