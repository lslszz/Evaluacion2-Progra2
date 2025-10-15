from Ingrediente import Ingrediente

class Stock:
    def __init__(self):
        self.lista_ingredientes = []

    def agregar_ingrediente(self, ingrediente):
        for i in self.lista_ingredientes:
            if i.nombre == ingrediente.nombre:
                if hasattr(i, "unidad") and hasattr (ingrediente, "unidad"):
                    if i.unidad == ingrediente.unidad:
                        i.cantidad =str(int(i.cantidad) + int(ingrediente.cantidad))
                    else:
                        print( f"Las unidades de medida deben ser '{i.nombre}'({i.unidad } vs {ingrediente.unidad}) ")
                        return
                else:
                    i.cantidad =str(int(i.cantidad) + int(ingrediente.cantidad))
                    return
                return       
        self.lista_ingredientes.append(ingrediente)

    def eliminar_ingrediente(self, nombre_ingrediente):
        for i in self.lista_ingredientes:   
            if i.nombre == nombre_ingrediente:
                self.lista_ingredientes.remove(i)
                break
 

    def verificar_stock(self):
        return len(self.lista_ingredientes)


    def actualizar_stock(self, nombre_ingrediente, nueva_cantidad):
        for i in self.lista_ingredientes:
            if i.nombre == nombre_ingrediente:
                i.cantidad = nueva_cantidad
                break

    def obtener_elementos_menu(self):
        return [i for i in self.lista_ingredientes]

