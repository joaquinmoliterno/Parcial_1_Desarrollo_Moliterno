from dataclasses import dataclass  
from app.models.nota import Nota

@dataclass(init=False, repr=True, eq=True)
class Materia:
    id: int
    nombre: str
    codigo: str
    observacion: str
    nota: Nota