# IMenu.py
from typing import Protocol, List, Optional
from Ingrediente import Ingrediente
from Stock import Stock

class IMenu(Protocol):
    """debes rellenar la Interfaz para los elementos del menú."""
    nombre:str
    precio: float
    ingredientes: List[Ingrediente]
    cantidad: int
    icon_path: Optional[str]

    def esta_disponible(self, stock: Stock)->bool:
        ...