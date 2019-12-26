# kariyer-mimari-python
## Genel
* Python script temelli bir programlama dilidir.
* Yazdıgınız kodlar python kurulu ise direk çalışır
* Python bilgisayara kurmanız gerekmektedir.
* `python --version` komutunu cmd'ye yazarsanız kurulu olan versionu ve kurulu olup olmadıgını anlayabilirsiniz.
* Python kodları yazmak icin 2 yöntem vardır. 
1. komut satırına `python` komutu ile python'ın kabuguna inip orada deneme yapabilirsiniz.
    * `print("Hello, World!")`
2. Phyton kodlarını .py uzantısı ile kaydedip calıstırabilirsiniz.
    * Bir dosyaya `print("Hello, World!")` yazıp `helloworld.py` ismi ile kaydedelim
    * `python helloworld.py` komutu ile dosyaya yazdıgımız python scriptini calıstırmıs oluruz.
* `print` komut satırına verdigimiz yazıyı yazar. Cok onemli bir komuttur ve sayesinde kodun ne yaptıgını ve elindeki verileri yazdırıp problemi bulabiliriz.
* Denemek için python kabugu kullanırız, proje olarak birşey yapıyorsak dosyaya kaydedip çalıştırırız genelde.
* python kabugu size `>>>` ve `$` gibi karakterleri basa kotup anlatabilir, gösterebilir ama siz komut yazarken bunları basa koymayın
* Python'da satır baslarındaki girintiler koddan önceki bosluklar cok önemlidir. Bu boslukları genelde `tab` tusu ile yaparız.
* `tab` tusunun kac bosluk bırakacagı kullandıgınız editore göre degisebilir ama cok onemli degildir. 4 veya 5 bosluk olabilir ama önemli olan bir kere 4 bosluk kullanılırsa bundan sonra da 4 bosluk kullanılmalıdır.
* Aynı islemi siz 4 kere bosluk tusuna basarak da yapabilirsiniz ama `tab` kullanmanız daha dogru olur
* Bu bosluklar altta yazan kodun üstteki icine mi girince calısacagı yoksa üstteki kod bittikten sonra mı calısacagını belirtir.

## Kosullar
* Kod yazmak aslında bilgisayara hangi durumda ne yapacagını anlatmaktır. Bu yüzden farklı durumları ve yapacagı davranısı kod olarak yazarız.
* En temel kosul kullanımı `if` ve `else` dir. `if` (eger) 
* `if 5 > 2: ` gibi kullanılabilir. Eger 5 , 2'den büyükse `if` den sonraki kodu calıstır demektir.
```
if 5 > 2: 
    print("5 sayısı 2 den büyüktür")
```
* Yukarıdaki kodda `print` satır basından yani `if` den 1 tab(genelde 4 bosluk karakteri demektir) kadar iceride yazılmıstır. `if` (eger 5 , 2 den büyükse bu koda gir demektir)
* Eger tab yapmazsanız hata verecektir. Çünkü `if` kosulu calısırsa calısacak kodu olmaz. Bunun icin `print` i 1 tab iceride yazdık.
## Değişkenler
* Bir sayı veya yazı üzerinde işlem yapacaksanız bunlara isim vermeniz gerekir yoksa bu sayı değişince nasıl tanıyacaksınız ?
* Bu sayı veya yazı veya başka bir değeri hafızada tutan ve ismi olan bu şeylere değişken denir. Diğer bir deyişle variable
* ``yas = 3`` ifadesi ile yas isimli bir değişken yarattık ve değerini 3 yaptık. Python'da sağdan sola değer atama yaparız `=` kullanarak.
* `yas = yas + 1` burada sağ taraftan yas+1(4) yas degiskenine atama yapılıyor.
* Diger programalama dillerine degiskenlere bu degiskenin yaz mı, tam sayı mı , kusurlu sayı mı oldugunu anlatan kelimeler yazarız. Mesela yukarıdaki kodu JAVA'da şu şekilde yazardık.
```
int yas = 3;
yas = yas + 1;
```
* Python'da int ifadesine gerek yoktur. Bunun yas degiskeninin sayı olduğunu python kendisi anlar ve tipini belirler. Bundan sonra yas sayı olduğu için toplama gibi matematiksel operasyonlara katılabilir.
* `yas = "3"` yanlara koyulan `""` ifadeleri ile python 3'ü yazı olarak tipini belirler. Bu durumda `yas = yas + 1` nin bir anlamı kalmaz çünkü herhangi bir yazı ile sayıyı toplamak mantıklı bir işlem değildir. Sonuçta Python hata verir ve hatanın ayrıntısını bize yazar.
* Bütün programlama dillerinde olduğu gibi Python'da da veri tipleri vardır. Bunlardan 2'sini yukarıda belirttiğim gibi yazı ve tam sayı tipleridir. 
* Yazı veri tipi `str` dir. Mesela yazı veri tipi Java'da `String` olarak isimlendirilir.
## Veri Tipleri
* Veri tipleri bütün programlama dillerinde önemli bir kavramdır. Yazılan kodun 1. performansını doğrudan etkiler.
```
Yazı Tipi:	str
Sayısal Tipler:	int, float, complex
Sıralı Tipler:	list, tuple, range
Map Tipi:	dict
Set(Küme) Tipleri:	set, frozenset
Boolean(1,0) tipi:	bool
Binary Tipleri:	bytes, bytearray, memoryview 
```
* Python'da veri tipini bizim belirtmemize gerek yok ama gene de onun bir veri tipi belirlenir Python yorumlayıcısı tarafından(Interpreter)
* Veri tipi değer atama yani `x = 5` sırasında int olarak belirlenir. Ancak bu degiskenin tipini biz de `str` yani yazı tipi olarak belirleyebiliriz. 
`x = str(20)`
* Verinin tipini `type(a)` gibi öğrenebiliriz. Buradaki a herhangi bir değişkendir.
* Sayılarla ilgili bir örnek:
```
x = 20
y = 1.2
z = x + y
print(z)
```
Yukarıdaki örnek int ve float yani bir tam sayı ve bir küsürlü sayının toplamının float olduğunu gösterir. z değeri 21.2 olduğundan `float` olarak veri tipi belirlenmiştir. İsterseniz ````print(type(z))```` ile veri tipinin `float` olduğundan emin olabilirsiniz.


