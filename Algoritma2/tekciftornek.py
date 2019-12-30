list1 = list(map(int,input("ilk listesi giriniz: ").split()))
list2 = list(map(int,input("ikinci listeyi giriniz: ").split()))
tekList = []
ciftList = []
for eleman in list1:
    if eleman % 2 == 0:
        ciftList.append(eleman)
    else:
        tekList.append(eleman)

for eleman in list2:
    if eleman % 2 == 0:
        ciftList.append(eleman)
    else:
        tekList.append(eleman)

print(tekList)
print(ciftList)
