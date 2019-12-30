#Burası tek satırlık yorum alanı. Tek satırlı yorumlar siyah temalarda gri olarak görünür.
'''

Çok satırlı yorumlar 6 tane tırnak işareti ile yapılır.Bunlar tek tırnak ya da çift tırnak olabilir.
Siyah temalarda genellikle yeşil olarak görünür ve yazı şekli italic olur.

Yorum satırları programcının yazdığı program hakkında kendisine ya da kendisinden başkasına işlemi hatırlatmak ya da açıklamak amaçlı
yazdığı metinlerdir.

Yorum satırları asla yazılımsal olarak ele alınmaz.İçerisine kod dahi yazılsa işlem görmeyecek.

Syntax = Söz dizimi ya da grammer olarak geçer.Yazım kanunudur.

Python'da ";" diye bir yapı yoktur.Bunu kullanmaya çalışırsanız syntax hatası alırsınız.
Python'da "{}" parantez yoktur (liste hariç).C tabanlı tüm yazılım dillerinde süslü parantezler blok görevi görür.
Ama python dilinde bunun yerine ":" işareti ve grid sistemi vardır.Grid sisteminde yapılacak en küçük hata bile
bütün programı bozacaktır.Grid sistemi genel olarak tab mantığıyla anlatılır.Bir kapsayıcı var ise onun altındaki eleman tab tuşu ile yazılır.Kapsayıcı örnekleri: if,else,while,for,def,class.
Grid örneği olarak:
if 1==1:
kodu buraya yazarsak grid hatası olacaktır.

if == 1:
    kodu buraya yazarsam doğru bir şekilde çalışacaktır.

Python'da değişkenlerin tipleri yoktur.Normalde Yorumlanan diller hariç tüm yazılım dillerinde değişkenlerin tipleri vardır.Örnek:sayısal için int yazısal için string tek karakterli işlem için char denilen tipler vardır.Python tüm bu işlemleri değişkenin değerine göre otomatik olarak yapar.Otomatik yapıldığı için milisaniyelikte olsa bir zaman kaybı yaratıyor.
Değişken değerlere isim verip daha sonra bu isimlerle o değerleri çağırmaktır.Bir değişken oluşturulduğunda bilgisayarın geçici hafızası olan Ram üzerine işlenir.Program kapatılıncaya ya da işlemi bitip çöp toplayıcısı tarafından RAM üzerinden silinene kadar hafıza da kalmaya devam eder.
Bir değişken tanımlanırken ilk başta değişkenin adı yazılır, daha sonra "=" işareti ile değişkenin değeri yazılır.
Eğer değişken değeri sayısal olacaksa sadece değeri yazmak yeterli.
Eğer değişken değeri yazısal olacaksa değer çift ya da tek arasına yazılır.
Bir metin eğer tırnak içerisinde yazılmadıysa ve kullanılan editor bunu(temaya göre değişir)  beyaz gösteriyor ise
bunun bir değişken adı olduğu anlamına gelir.

Değişken adı oluşturulurken Türkçe karakter kabul edilir ancak kullanmak tavsiye edilmez.Değişken adında asla ve asla boşluk kullanamayız.Örnek:degisken adi kesinlikle hatalıdır.degisken ayrı adi ayrı olarak görülecek ve snytax hatası alınacak.Olması gerekene örnek:degiskenAdi,DegiskenAdi,_degiskenAdi bu türevler doğrudur.Ancak bazı standartlar vardır ki bu standartlar yazılımcılar tarafından konulmuştur.
Eğer tek kelimelik bir değişken adı yazılacak ise bu tamamen küçük yazılır.
Eğer iki ya da daha fazla kelimelik bir değişken adı yazılacak ise bu durumda ilk kelime küçük diğer kelimelerin sadece baş harfi büyük yazılır.Örnek:degiskenAdi.


Yazılım dilleri yapı olarak derlenen ve yorumlanan diller olarak iki bölüme ayrılır.
Derlenen diller hangi platform üzerinde yazıldıysa derleme esnası sırasında direkt olarak o platformun işlemci diline çevrilir.Bu nedenden dolayı windows üzerinde derlenmiş bir program linux ya da mac üzerinde çalışmayacaktır.

Yorumlanan diller ise yazıldıktan sonra derlenmez, çalıştırma esnasında yorumlayıcı programı okur,yorumlamasını yapar ve hangi platform üzerinde çalışıyor ise anlık olarak o platformun işlemci diline çevirir.

Python dili "C" dili kullanılarak yazıldığı için yorumlama esnasında arkplanda C dilinin metodları çalışır.
'''
#ilkDegisken = "Python is Awesome"
#print(ilkDegisken)
#print("ilkDegisken")

sayi = 5
print("sonuc = "+str(sayi+5))

'''
+ oparatörünün kullanımı

1-) "+" öperatörü iki yazısal değer ile kullanıldığında iki değeri birleştirir.
2-) "+" öperatörü iki sayısal değer ile kullanıldığında iki değeri toplar.
3-) "+" öparetörü en az 1 yazısal ve sonrasında kaç tane olacağı önemli olmayan sayısal değerler ile kullanıldığında
sayısalları toplayıp yazısalla birleştirme işlemi yapar.Ancak bu esnada yazısal ve sayısal değer birleştirilmeyeceği için program hata verir.yapılması gereken sayısal değeri "str" metodu kullanılarak yazısala çevirmek.
100 = yüz 

'''

#Bir değişken adı tırnak içerisinde yazılırsa onun artık yazılımsal hiçbir hükmü kalmaz.Sadece düz yazı olur.
#python 2 versiyonunda print "yazı"



















