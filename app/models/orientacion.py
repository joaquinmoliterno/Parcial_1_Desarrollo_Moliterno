from dataclasses import dataclass  
from app.models.plan import Plan
from app.models.materia import Materia
from app.models.especialidad import Especialidad

@dataclass(init=False, repr=True, eq=True)
class Orientacion:
    id: int
    nombre: str
    plan: Plan
    materia: Materia
    especialidad: Especialidad
    