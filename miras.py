'''
Miras verme işlemi kendisini miras alan sınıfa kendi içerisindeki verileri aktarma
Örnek olarak bir çocuk düşünün saçları annesinden göz rengi babasından alınmış.Çocuk miras alan anne ve baba miras veren oluyor
'''
class ebeveyn:
    def anneSacRengi(self):
        return "sarı"

    def babaGozRengi(self):
        return "mavi"

class cocuk(ebeveyn):
    def __init__(self):
        print("Çocuğun saç rengi:"+self.anneSacRengi()+"\nÇocuğun göz rengi:"+self.babaGozRengi())

bebek = cocuk()