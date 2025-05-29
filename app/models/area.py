from dataclasses import dataclass
from app.models.grupo import Grupo  

@dataclass(init=False, repr=True, eq=True)
class Area:
    id: int
    nombre: str
    grupo: Grupo
