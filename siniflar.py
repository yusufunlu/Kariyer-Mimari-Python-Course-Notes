'''
Sınıflar belirli amaçlara hizmet eden metodları ve değişkenleri içerisinde barındıran (gruplandıran) yapılardır.
Sınıfların çıkma amacı tamamen C dilindeki eksikliği tamamlamaktır.Hatta C++ dilinin açılımı Sınıflar ile C olarak geçer.
Microsoft tarafından rakip olarak üretilen C# dili C++++ daha sonradan + işaretleri # olarak değişmiştir.
Sınıf programlaması OOP(object orianted programming(Nesne tabanlı programala)) python ve c++ dilleri sınıf kullanmadan
yazılabilir(belli bir yere kadar) C#,Java gibi diller başlangıç itibariyle ağır derece de nesne tabanlı programlama modelini
kullanır.
i = futbol
char[] *i = [6];
*i = "futbol";

bir sınıf tanımlanırken ilk başta "class" anahtar kelimesi kullanılır.daha sonra sınıfın adı yazılır ve ":" atıp alta geçilir
'''
class araba:
    def __init__(self,m,y,g,v):
        '''
            init anahtar kelimesi bu sınıf nesne haline ilk getirildiğinde çalışacak olan metoddur.
            self anahtar kelimesi bu sınıf içerisinde ister değişken ister metoda erişirken kullanacağım
            anahtar kelime.Self anahtar kelimesi değiştirilemez ve her sınıfta olmak zorunda.

            *Nesne = bir sınıfın değişkene atanmasıdır.Sınıf değişkene atandığında o sınıf ram üzerinde bir object
            yani nesne olur.

            Nesne bir sınıfın değişkene atanmasıysa init metodu sınıf değişkene atandığı anda çalışacak metoddur.

            *Nesne Tabanlı Programlama(OOP) = Nesne tabanlı programlama modelinde herşey bir nesnedir.Örnek C# dilinde
            Console.WriteLine("") console yani terminal ekranına bir veri yazan metoddur.Burada Console kısmı sınıfın adı
            WriteLine ise o sınıf içerisindeki değişkenin adıdır.Aynı mantık Python dilinde de geçerlidir.

            Bu yapının ilerisi Design Pattern(Tasarım Şablonu) denilen yapılardır.Design pattern yapıları
            kullanım amacına göre farklı isimlerde ve farklı yapılarda olur.Bunlar dillerin kendi içerisinde gelen
            yapılar değil biz yazılımcıların üretip paylaştığı yapılardır.
        '''
        self.model = m
        self.yil = y
        #self.motorGucu = str(800)+"hp"
        self.motorGucu = g
        self.vites = v
        print("Değişkenler oluşturuldu.")

    def arabayiOlustur(self):
        print("Arabanın Modeli:"+self.model+"\nArabanın Yılı:"+str(self.yil)+"\n"+"Arabanın Motor Gücü:"+self.motorGucu+"\n"+"Arabanın Vitesi Tipi:"+self.vites)

    def verileriGir(self):
        self.model = input("Lütfen arabanın modelini girin:")
        self.yil = input("Lütfen arabanın yılını girin:")
        self.motorGucu = input("Lütfen arabanın motor gücünü girin:")
        self.vites = input("Lütfen arabanın vites tipini girin:")
        print("Taş Giribi Araba Oldu Be")

'''
car = araba()
car.arabayiOlustur()
car.verileriGir()
car.arabayiOlustur()
'''
'''
3 soru 
1-) sınıf adı arabayken neden içindeki şeylere car diye ulaştık
2-) car dan "." neyin nesi
3-) parantez aç kapa neyin nesi

1-) Bir sınıf değişkene atandığı zaman yani nesneye çevrildiği zaman hangi isimde oluşturulduya
o isimde kullanılır.Yukarıdaki örnekte nesne adı car. Bu sayede aynı sınıf duruma göre 2 ya da daha fazla kez nesne haline 
getirilebilir.Örnek
yagiz = araba()
semih = araba()
fatih = araba()
yusuf = araba()

2-) "." işareti bir nesne içerisinde bulunan ve erişim seviyesi olarak dışarıdan erişime izin verilen değişkenlere 
ya da metodlara erişmek için kullanılan anahtar kelimedir.Kod kısmnında bir "." görüyorsak solundaki sınıfın nesneye
çevrilmiş adıdır.Sağındaki ise sınıf içerisindeki bir değerdir.
Java,C#,Ruby,Python,Javascript gibi dillerde sınıf içerisindeki bir değişkene ya da bir metoda ulaşmak için "." kullanılır.
C,C++,Php gibi dillerde "." yerine "->" kullanılır.Bunun sebebi php dilinde "." python dilindeki "+" gibi çalışır
sadece toplama yapmaz.C/C++ dillerinde ise yine "->" ile kullanılır.


3-) parantezler sonuna konulduğu şeyin bir metod olduğunu belirtir.
'''

model = input("Lütfen arabanın modelini girin:")
yil = input("Lütfen arabanın yılını girin:")
motor = input("Lütfen arabanın motor gücünü girin:")
vites = input("Lütfen arabanın vites tipini girin:")
_araba = araba(model,yil,motor,vites)
_araba.arabayiOlustur()

























