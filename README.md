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
* Yukarıdaki kodda `print` satır basından yani `if` den 1 tab kadar iceride yazılmıstır. `if` (eger 5 , 2 den büyükse bu koda gir demektir)
* Eger tab yapmazsanız hata verecektir. Çünkü `if` kosulu calısırsa calısacak kodu olmaz. Bunun icin `print` i 1 tab iceride yazdık.

