from app.models import Materia
from app.repositories.materia_repositorio import MateriaRepository

class MateriaService:

    @staticmethod
    def crear_materia(materia: Materia):
        """
        :param materia: Materia a crear.
        :return: Materia creada.
        """
        MateriaRepository.crear(materia)
    
    @staticmethod
    def buscar_por_id(id: int) -> Materia:
        """
        :param id: ID de la materia a buscar.
        :return: Materia encontrada o None si no se encuentra.
        """
        return MateriaRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[Materia]:
        """
        :return: Lista de materias.
        """
        return MateriaRepository.buscar_todos()
    
    @staticmethod
    def actualizar_materia(id: int, materia: Materia) -> Materia:
        """
        :param id: ID de la materia a actualizar.
        :param materia: Objeto Materia con los nuevos datos.
        :return: Objeto Materia actualizada.
        """
        materia_existente = MateriaRepository.buscar_por_id(id)
        if not materia_existente:
            return None
        materia_existente.nombre = materia.nombre
        materia_existente.codigo = materia.codigo
        materia_existente.observacion = materia.observacion
        
        return materia_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> Materia:
        """
        :param id: ID de la materia a borrar.
        :return: Objeto Materia borrado o None si no se encuentra.
        """

        materia = MateriaRepository.borrar_por_id(id)
        if not materia:
            return None
        return materia