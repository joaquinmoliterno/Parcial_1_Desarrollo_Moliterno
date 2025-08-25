from dataclasses import dataclass  

@dataclass(init=False, repr=True, eq=True)
class TipoEspecialidad:
    id: int
    nombre: str
    nivel: str