class Computer():
    def __init__(self, computer, ram, ssd):
        self.computer = computer
        self.ram = ram
        self.ssd = ssd

class Laptop(Computer):
    def __init__(self, computer, ram, ssd, model):
        super().__init__(computer, ram, ssd)
        self.model = model

lenovo = Laptop('lenovo', 2, 512, 'l420')
print('This computer is:', lenovo.computer)
print('This computer has ram of', lenovo.ram)
print('This computer has ssd of', lenovo.ssd)
print('This computer has this model:', lenovo.model)

# Computer isimli bir class yani bir tanım yaptık ilk önce
# Daha sonra gene bir bilgisayar olan Lenovo class'ını yarattık
# Lenovo class'ını Computer class'ından türettik bu sayede Lenovo Computer'ın yaptığı herşeyi yapar