from app.models import Autoridad
from app.repositories.autoridad_repositorio import AutoridadRepository



class AutoridadService:

    @staticmethod
    def crear_autoridad(autoridad: Autoridad):
        """
        :param autoridad: Objeto Autoridad a crear.
        :return: Objeto Autoridad creado.
        """
        AutoridadRepository.crear(autoridad)
    
    @staticmethod
    def buscar_por_id(id: int) -> Autoridad:
        """
        :param autoridad: Objeto Autoridad a crear.
        :return: Objeto Autoridad creado.
        """
        return AutoridadRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[Autoridad]:
        """
        :return: Lista de objetos Autoridad.
        """
        return AutoridadRepository.buscar_todos()
    
    @staticmethod
    def actualizar_autoridad (id: int, autoridad: Autoridad) -> Autoridad:
        """
        :param id: ID de la autoridad a actualizar.
        :param autoridad: Objeto Autoridad con los nuevos datos.
        :return: Objeto Autoridad actualizado.
        """
        autoridad_existente = AutoridadRepository.buscar_por_id(id)
        if not autoridad_existente:
            return None
        autoridad_existente.nombre = autoridad.nombre
        autoridad_existente.id = autoridad.id
        autoridad_existente.cargo = autoridad.cargo
        autoridad_existente.cargo_id = autoridad.cargo_id
        autoridad_existente.telefono = autoridad.telefono
        autoridad_existente.email = autoridad.email
        return autoridad_existente
        
    @staticmethod
    def borrar_por_id(id: int) -> Autoridad:
        """
        :param id: ID de la autoridad a borrar.
        :return: Objeto Autoridad borrado o None si no se encuentra.
        """
        autoridad = AutoridadRepository.borrar_por_id(id)
        if not autoridad:
            return None
        return autoridad
    
        