'''
Metodlar kendi içlerinde işlem yapmak için üretilmiş yapılardır.Amaçları yazılmış kodları gruplandırıp
sayfada kod tekrarının önüne geçmektir.
Temel olarak 4 farklı çeşitte metod yapısı vardır.
1-) Parametre alıp değer döndüren
2-) Parametre alıp değer döndürmeyen
3-) Parametre almayıp değer döndüren
4-) Parametre almayıp değer döndürmeyen

Parametre dediğimiz olay metod ya da fonksiyonlara değer göndermeye yarayan değişkenlerdir.
python dilinde bir metod oluşturmak için ilk olarak def(define kısaltılmışı) anahtar kelimesi yazılır.
daha sonra metod adı yazılır.Değişken isimlerinde geçerli olan kurallar metod isimlerinde de geçerlidir.
isim yazıldıktan sonra parantez açılır eğer parametre alınacak ise parametreler bu parantezin içerisine
virgül ile yazılır daha sonra parantez kapatılı ve ":" eklenir.

def metodAdi():

'''
#tip1
'''
return anahtar kelimesi bir metodun içerisinden değer döndürmeye yarar.Aynı zamanda metodu bitirme işlemi yapar.
bundan dolayı return anahtar kelimesinden sonra ne kadar kod yazarsanız yazın hiçbir anlamı olmaz.
Döndürmek deyimi bir değeri geri bildirim yapmak olarak anlatılabilir.

'''
def metod1(sayi1,sayi2):
    return sayi1+sayi2
'''
toplam = metod1(5,10)
print(toplam)
'''
#tip2
def metod2(sayi1,sayi2):
    print(sayi1+sayi2)

#metod2(10,20)

#tip3
def metod3():
    return 30+40

#print(metod3())

#tip4
def metod4():
    print(50*50)

metod4()












