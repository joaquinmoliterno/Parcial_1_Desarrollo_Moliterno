from dataclasses import dataclass, asdict
from typing import Optional

from app.repositories.alumno_repositorio import AlumnoRepository

@dataclass
class FichaAlumnoDTO:
    id: int
    nro_legajo: int
    apellido: str
    nombre: str
    nro_documento: str
    fecha_nacimiento: str
    sexo: str
    fecha_ingreso: str
    facultad: Optional[str] = None  

    def to_dict(self) -> dict:
        return asdict(self)

class FichaAlumnoService:
    @staticmethod
    def obtener_ficha(alumno_id: int) -> Optional[FichaAlumnoDTO]:
        alumno = AlumnoRepository.buscar_por_id(alumno_id)
        if not alumno:
            return None

        return FichaAlumnoDTO(
            id=alumno.id,
            nro_legajo=alumno.nro_legajo,
            apellido=alumno.apellido,
            nombre=alumno.nombre,
            nro_documento=alumno.nro_documento,
            fecha_nacimiento=str(alumno.fecha_nacimiento),
            sexo=alumno.sexo,
            fecha_ingreso=str(alumno.fecha_ingreso),
            facultad=None,
        )
