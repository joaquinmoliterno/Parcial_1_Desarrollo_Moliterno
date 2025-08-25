from dataclasses import dataclass
from sqlalchemy import DateTime  

@dataclass(init=False, repr=True, eq=True)
class Plan:
    id: int
    nombre: str
    fecha_inicio: DateTime
    fecha_fin: DateTime
    observacion: str