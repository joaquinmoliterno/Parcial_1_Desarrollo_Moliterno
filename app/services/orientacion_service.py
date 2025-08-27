from app.models import Orientacion
from app.repositories.orientacion_repositorio import OrientacionRepository

class OrientacionService:
    
    @staticmethod
    def crear_orientacion(orientacion: Orientacion):
        """
        :param orientacion: Orientacion a crear.
        :return: Orientacion creada.
        """
        OrientacionRepository.crear(orientacion)
    
    @staticmethod
    def buscar_por_id(id: int) -> Orientacion:
        """
        :param id: ID de la orientacion a buscar.
        :return: Orientacion encontrada o None si no se encuentra.
        """
        return OrientacionRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[Orientacion]:
        """
        :return: Lista de orientacion.
        """
        return OrientacionRepository.buscar_todos()
    
    @staticmethod
    def actualizar_orientacion(id: int, orientacion: Orientacion) -> Orientacion:
        """
        :param id: ID de la orientacion a actualizar.
        :param orientacion: Objeto Orientacion con los nuevos datos.
        :return: Objeto Orientacion actualizada.
        """
        orientacion_existente = OrientacionRepository.buscar_por_id(id)
        if not orientacion_existente:
            return None
        orientacion_existente.nombre = orientacion.nombre
        return orientacion_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> Orientacion:
        """
        :param id: ID de la orientacion a borrar.
        :return: Objeto Orientacion borrado o None si no se encuentra.
        """

        orientacion = OrientacionRepository.borrar_por_id(id)
        if not orientacion:
            return None
        return orientacion