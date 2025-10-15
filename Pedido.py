from ElementoMenu import CrearMenu 
class Pedido:
    def __init__(self):
        self.menus = []  

    def agregar_menu(self, menu: CrearMenu):
        for m in self.menus:
            if m.nombre ==menu.nombre:
                m.cantidad += 1
                return
            
        menu.cantidad=1
        self.menus.append(menu)

    def eliminar_menu(self, nombre_menu: str):
        for i, m in enumerate(self.menus):
            if m.nombre == nombre_menu:
                self.menus.pop(i)
                return True
        return False

    def mostrar_pedido(self):
        for m in self.menus:
            print (f"{m.nombre} x {m.cantidad} -${m.precio * m.cantidad} ")

    def calcular_total(self) -> float:
        total = 0
        for menu in self.menus:
            total += menu.precio * menu.cantidad
        return total
