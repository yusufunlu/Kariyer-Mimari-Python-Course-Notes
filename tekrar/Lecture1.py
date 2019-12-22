#Python'da yorum # ile yapilir, bu isaretten sonrasi kod olarak calismaz
#if for gibi onemli kelimelerden sonra indent yani bosluk gereklidir
#bu bosluk en az 1 bosluktur
if 5 > 2:
    if 3 > 1:
     print("Five is greater than two!")

#Python'da diger dillerin aksine degisken tanimlarken basina hangi tiple oldugunu belirtmeye gerek yoktur
#degisken uzerine bir deger atandigi zaman tanimlanir
x = 4 # int tipinde degisken
x = "Sally" #str tipinde degisken
print(x)

x = "Hello World"	#str
x = 20	#int
x = 20.5	#float
x = 1j	#complex
x = ["apple", "banana", "cherry"]	#list
x = ("apple", "banana", "cherry")	#tuple
x = range(6)	#range
x = {"name" : "John", "age" : 36}	#dict
x = {"apple", "banana", "cherry"}	#set
x = frozenset({"apple", "banana", "cherry"})	#frozenset
x = True	#bool
x = b"Hello"	#bytes
x = bytearray(5)	#bytearray
x = memoryview(bytes(5))	#memoryview


print(type(x)) #degiskenin tipini ogerenebiliriz

