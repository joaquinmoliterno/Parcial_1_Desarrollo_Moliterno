from dataclasses import dataclass
from sqlalchemy import DateTime

from app.models.documento import Documento

@dataclass(init=False, repr=True, eq=True)
class Alumno():
    id: int
    apellido: str
    nombre: str
    nro_documento: str
    tipo_documento: Documento
    fecha_nacimiento: DateTime        
    sexo: str
    nro_legajo : int
    fecha_ingreso: DateTime