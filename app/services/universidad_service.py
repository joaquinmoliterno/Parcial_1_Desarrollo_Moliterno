from app.models import Universidad
from app.repositories.universidad_repositorio import UniversidadRepository

class UniversidadService:

    @staticmethod
    def crear_universidad(universidad: Universidad):
        """
        :param universidad: Universidad a crear.
        :return: Universidad creada.
        """
        UniversidadRepository.crear(universidad)
    
    @staticmethod
    def buscar_por_id(id: int) -> Universidad:
        """
        :param id: ID de la universidad a buscar.
        :return: Universidad encontrada o None si no se encuentra.
        """
        return UniversidadRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[Universidad]:
        """
        :return: Lista de universidad.
        """
        return UniversidadRepository.buscar_todos()
    
    @staticmethod
    def actualizar_universidad(id: int, universidad: Universidad) -> Universidad:
        """
        :param id: ID de la universidad a actualizar.
        :param universidad: Objeto Universidad con los nuevos datos.
        :return: Objeto Universidad actualizada.
        """
        universidad_existente = UniversidadRepository.buscar_por_id(id)
        if not universidad_existente:
            return None
        universidad_existente.nombre = universidad.nombre
        universidad_existente.sigla = universidad.sigla
        return universidad_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> Universidad:
        """
        :param id: ID de la universidad a borrar.
        :return: Objeto Universidad borrado o None si no se encuentra.
        """

        universidad = UniversidadRepository.borrar_por_id(id)
        if not universidad:
            return None
        return universidad