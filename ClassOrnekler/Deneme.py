from ClassOrnekler.Automobil import Automobil
from ClassOrnekler.Car import Car
from ClassOrnekler.Computer.Computer import Computer
from ClassOrnekler.Laptop.Laptop import Laptop

bilgisayar = Computer('lenovo', 2, 512)
print('This computer is:', bilgisayar.brand)
print('This computer has ram of', bilgisayar.ram)
print('This computer has ssd of', bilgisayar.ssd)

lenovo = Laptop('lenovo', 2, 512, 'l420')
print('This computer is:', lenovo.brand)
print('This computer has ram of', lenovo.ram)
print('This computer has ssd of', lenovo.ssd)
print('This computer has this model:', lenovo.model)

car = Car()
auto = Automobil()


# Computer isimli bir class yani bir tanım yaptık ilk önce
# Daha sonra gene bir bilgisayar olan Lenovo class'ını yarattık
# Lenovo class'ını Computer class'ından türettik bu sayede Lenovo Computer'ın yaptığı herşeyi yapar