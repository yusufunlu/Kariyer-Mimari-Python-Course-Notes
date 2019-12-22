import random
random.seed(2)

firma = "treks"
sube = 1
urunListesi = ['kazak','pantolon','mont','don','fantezi']
print(type(random.randint(0,5)))

while sube < 1000:
    print(firma + " sube: "+str(sube) + " haftanin urunu: "+urunListesi[random.randint(0,2)])
    sube += 1
    for i in urunListesi:
        print('katalog: '+ i)
