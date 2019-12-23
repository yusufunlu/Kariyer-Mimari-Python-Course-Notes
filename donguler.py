'''

Döngüler bir koşul sağlanana kadar içerisine belirtilen işlemleri yapan yapılardır.
Günlük hayattan örnek vermek gerekirse mesaili çalışan bir işçi gibi.
Yazılım dillerinin çoğunda 4 temel döngü vardır
1-) while
2-) do-while (gereksiz)
3-) for
4-) foreach

Python dilinde ise while ve for vardır.For diğer dillerdeki for ve foreach döngüsünün aynısı yapar.
Örnek: C# dilinde for kullanımı
for(int i = 0; i<10;i++){
    belirilen sayı 10 dan küçük olduğu sürece işlem yapar ve her seferinde i değerini 1 arttırır.
    i++ = i değerini 1 arttır.
}
for i in range(10,20):
    yukarıdaki kodun python dilinde yazılışı bu şekildedir

------------------------------------------------------------------------------------------------------
foreach örnek:
C# dilinde
foreach(var item in listeAdi){

}

Python dilinde
for item in listeAdi:

//C#
for foreachin yapıtığı işlemin aynısını yapabilir.Genelde döngülerde eğer bir liste varsa foreach kullanılır.
foreach döngüsü çalışırken kendi içerisisinde tüm listeyi hafızaya alıyor.

kullanicilar{
    0{
        kadi:"emre",
        pass:"deneme",
        mail:"saala"
    }
    1{
        kadi:"yağız",
        pass:"deneme",
        mail:"saala"
    }
    2{
        kadi:"semih",
        pass:"deneme",
        mail:"saala"
    }
    3{
        kadi:"caner",
        pass:"deneme",
        mail:"saala"
    }

}
while döngüsünde ilk başta bir değer belirtilir ve bu değer döngüde kontrol edilir.Döngü her dönüşünde bu değeri arttırır.
'''
'''
sayi = 0
alinan = 10
while sayi<=alinan:
    print(sayi) #ekrana sayi değerini yazdırır.Ancak döngü esnasında sayi değişkeninin değeri artmazsa sonsuz döngü oluşur ve ekranda sürekli 0 yazar
    sayi +=1
'''
'''
for x in range(0,sayi,1):
    print(x)
'''

liste = []
liste.append("Bu ilk değer")
liste.append("Bu ikinci değer")
liste.append("Bu üçüncü değer")
'''
for item in liste:
    print(item)
'''
'''
i = 0
while i < len(liste):
    print(liste[i])
    i+=1
'''
alinan = input("Lütfen bir sayı belirtiniz:")
#for ile yapılan kısım
'''
for x in range(0,alinan):
    print(x)
'''
#while yapılan kısım
sayi = 0
print("Girdiğiniz sayı:"+str(alinan))
while sayi < int(alinan):
    print(sayi)
    sayi+=1






