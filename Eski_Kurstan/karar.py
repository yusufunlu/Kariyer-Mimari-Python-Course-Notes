'''
Programın karar verme yapısıdır.If olarak geçer ve aritmetik işlemler sayesinde karar verir.
Doğru ise if içerisine yazılan yanlış ise else içerisine yazılan kodlar çalışır.Her if için bir else olmak zorunda değildir.
Else içinde if açılabilir if eçerisinde if açılabilir.Uzayıp gider Ancak if olmadan else asla olmaz.

İki farklı if yazma şekli vardır
1-)
if (1==1):

2-) if 1==1:

Temporary if denilen bir işlem daha vardır tek içinde if ve else sorgusu yapmanızı sağlar.
Örn: sayi = 1==1 ? "doğru":"yanlış"
temporary if yazarken ilk başta sorgu yazılır daha sonra "?" atıır.Soru işaretinden sonra olan kısım sorgu doğrusa çalışır
yani normal kullanımdaki ifin içerisi.":" dan sonra olan kısım else kısmıdır yani yanlış durumunda çalışacak olan yerdir.

'''
'''
if 1 != 1:
    print("deneme")
else:
    print("sorgu doğru değil")
'''
age = int(input("Lütfen Yaşınızı Giriz:"))
if age >= 18:
    print("İçeri girebilirsin yaşın tutuyor")
elif age == 16:
    print("Yaşın küçük 2 sene sabret sonra ilk ziyaretin benden")
else:
    print("Bu yaşta ne bu hız.git 18 ol gel.Kreş değil lan burası")










