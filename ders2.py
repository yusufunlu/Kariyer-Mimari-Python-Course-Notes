'''
Kullanıcıdan veri alırken input dediğimiz bir yapı mevcuttur.Kullanıcıdan aldığı değeri bir değişkene gönderir.
input metodu string(yazısal) tipte geri dönüş yapan bir metoddur.Bu değer ile matematiksel bir işlem yapabilmek için
değerin mutlaka int(sayısal) tipe dönüşmesi gerekir.
string çevirmek istersek = str(değer)
int çevirmek istersek = int(değer)
Geri dönüş işlemi varsa ve değer daha sonradan kullanılacak ise mutlaka bir değişkene eşitlenir.Ama sadece tek bir yerde
kullanılacaksa sadece yazılır.

Python 2 de input metodu raw_input olarak geçer
Python 3 de direkt input olarak geçer.

'''
#isim = input("Lütfen ismini belirt:")
#print("Sen kimsin çık dışarı "+isim)
#print("blabalblablal ${0} ${1}",isim,)

sayi1 = input("Lütfen ilk sayıyı belirt:")
sayi2 = input("Lütfen ikinci sayıyı belirt:")

print("Toplam:"+str(int(sayi1)+int(sayi2)))















