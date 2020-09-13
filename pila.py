class Pila:
     def __init__(self):
         self.items = []

     def estaVacia(self):
         return self.items == []

     def incluir(self, item):
         self.items.append(item)

     def extraer(self):
         return self.items.pop()

     def inspeccionar(self):
         return self.items[len(self.items)-1]

     def tamano(self):
         return len(self.items)

"""p=Pila()

print(p.estaVacia())
p.incluir(4)
p.incluir('perro')
#p.incluir(True)
print(p.tamano())
print(p.estaVacia())
#p.incluir(8.4)
#print(p.extraer())
print(p.inspeccionar())
print(p.extraer())
print(p.tamano())
print(p.inspeccionar())

if p.estaVacia() is True:
    print("Esta vacia")
else:
    print("Esta llena")

while p.estaVacia() is False:
    p.extraer()

if p.estaVacia() is True:
    print("Esta vacia")
else:
    print("Esta llena")

print(p.tamano())
"""
