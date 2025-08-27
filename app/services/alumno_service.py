from app.models import Alumno
from app.repositories.alumno_repositorio import AlumnoRepository

class AlumnoService:

    @staticmethod
    def crear_alumno(alumno: Alumno):
        """
        :param alumno: Alumno a crear.
        :return: Alumno creada.
        """
        AlumnoRepository.crear(alumno)
    
    @staticmethod
    def buscar_por_id(id: int) -> Alumno:
        """
        :param id: ID de la Alumno a buscar.
        :return: Alumno encontrada o None si no se encuentra.
        """
        return AlumnoRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[Alumno]:
        """
        :return: Lista de alumno.
        """
        return AlumnoRepository.buscar_todos()
    
    @staticmethod
    def actualizar_alumno(id: int, alumno: Alumno) -> Alumno:
        """
        :param id: ID de la alumno a actualizar.
        :param alumno: Objeto Alumno con los nuevos datos.
        :return: Objeto Alumno actualizada.
        """
        alumno_existente = AlumnoRepository.buscar_por_id(id)
        if not alumno_existente:
            return None
        alumno_existente.nombre = alumno.nombre
        alumno_existente.apellido = alumno.apellido
        alumno_existente.nro_legajo = alumno.nro_legajo
        alumno_existente.nro_documento = alumno.nro_documento
        alumno_existente.fecha_nacimiento = alumno.fecha_nacimiento
        alumno_existente.sexo = alumno.sexo
        alumno_existente.fecha_ingreso = alumno.fecha_ingreso
        return alumno_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> Alumno:
        """
        :param id: ID de la alumno a borrar.
        :return: Objeto Alumno borrado o None si no se encuentra.
        """

        alumno = AlumnoRepository.borrar_por_id(id)
        if not alumno:
            return None
        return alumno