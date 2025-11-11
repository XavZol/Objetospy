class Restaurant:

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre # Atributo
        self.categoria = categoria
        self._precio = precio # Default: Public, PROTECTED 

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self._precio}')

#Instanciar la clase
restaurant = Restaurant('Pizzeria Mexico', 'Comida Italiana', 50)

print(restaurant._precio)
restaurant._precio = 80
restaurant.mostrar_informacion()


restaurant2 = Restaurant('Hamburguesas Python', 'Comida Casual', 20)
print(restaurant2._precio)
restaurant2._precio = 40
restaurant2.mostrar_informacion()