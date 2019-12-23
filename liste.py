'''
Listeler tek bir değişken altında en az 1 bir adet değer bulunan yapılardır.
Örnek:veritabanınızda kullanılar listeniz var ve burada 10 bin tane kullanıcı var.Siz bir sorgu yapıyorsunuz
tüm kullanıcıları getir.Sorgunun sonunda 10 bin kullanıcı size liste halinde geliyor.

Listelerin belirli bir elemanına ulaşmak için o elemanın kaçıncı sırada olduğu belirtmemiz gerekiyor.

Listeler tüm yazılım dillerinde herzaman 0 dan başlar.Toplam 10 tane değeri olan bir listede ilk değerin sırası 0
son değerin sırası 9 olur.Listenin eleman sayısı sorgulandığında bize içerisindeki toplam eleman sayısını verir.
Son değerine ulaşmak için listenin toplamı "-1" işlemi kullanılır.
'''
liste = []
liste.append("Bu ilk değer")
liste.append("Bu ikinci değer")
liste.append("Bu üçüncü değer")
'''
Listelere eleman eklemek için append metodu kullanılır
'''
#print(liste)
#print("Listenin ikinci değeri:"+liste[1])
#listenin belirli bir sırasındaki elemanı almak için listenin adı yazılı ve köşeli parantezler açılır içerisine sıra yazılır
#belirtilen sıra listenin içerisinde yoksa hata alırız ve bu hata programı patlatacak tipten olur.
#print(liste[3])
#print(len(liste)) # len metodu içerisine parametre olarak verilen değerin toplamını döndürür.
#print("Son değer:"+liste[len(liste)-1])
liste.clear() #Listenin içerisindeki tüm elemanları temizler
#print(liste) ekranda sadece "[]" çıkar
#print(liste[0]) out of range hatası verir.







