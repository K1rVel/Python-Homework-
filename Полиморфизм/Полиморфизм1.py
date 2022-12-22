class Dug():
    def Krya(self):
        print('Кря')
    def clothes(self):
        print('Делает вид, что носит одежду')
class Chelovek():
    def Krya(self):
        print('Имитирует кря')
    def clothes(self):
        print('Носит одежду')

x1 = Dug()
x2 = Chelovek()
for i in (x1, x2):
    i.Krya()
    i.clothes()