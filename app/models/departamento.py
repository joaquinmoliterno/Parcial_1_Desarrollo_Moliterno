from dataclasses import dataclass  
from app.models.orientacion import Orientacion

@dataclass(init=False, repr=True, eq=True)
class Departamento:
    id: int
    nombre: str
    orientacion: Orientacion