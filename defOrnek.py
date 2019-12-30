def ikinciBul(_elemanSayisi,_skorListesi):
    _skorListesi = list(_skorListesi)
    _skorListesi.sort(reverse = True)
    print(_skorListesi)

elemanSayisi = int(input("Kac skor gireceksin"))
skorListesi = map(int, input("skorlari bana birer bosluklu halde ver lutfen!").split(','))

ikinciBul(elemanSayisi,skorListesi)

