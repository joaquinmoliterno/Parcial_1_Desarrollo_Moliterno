from dataclasses import dataclass  

@dataclass(init=False, repr=True, eq=True)
class Nota:
    id: int
    calificacion: str