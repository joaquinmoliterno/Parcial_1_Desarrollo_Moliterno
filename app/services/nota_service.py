from app.models import Nota
from app.repositories.nota_repositorio import NotaRepository

class NotaService:

    @staticmethod
    def crear_nota(nota: Nota):
        """
        :param nota: Nota a crear.
        :return: Nota creada.
        """
        NotaRepository.crear(nota)
    
    @staticmethod
    def buscar_por_id(id: int) -> Nota:
        """
        :param id: ID de la nota a buscar.
        :return: Nota encontrada o None si no se encuentra.
        """
        return NotaRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[Nota]:
        """
        :return: Lista de notas.
        """
        return NotaRepository.buscar_todos()
    
    @staticmethod
    def actualizar_nota(id: int, nota: Nota) -> Nota:
        """
        :param id: ID de la nota a actualizar.
        :param nota: Objeto Nota con los nuevos datos.
        :return: Objeto Nota actualizada.
        """
        nota_existente = NotaRepository.buscar_por_id(id)
        if not nota_existente:
            return None
        nota_existente.calificacion = nota.calificacion
        return nota_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> Nota:
        """
        :param id: ID de la nota a borrar.
        :return: Objeto Nota borrado o None si no se encuentra.
        """

        nota = NotaRepository.borrar_por_id(id)
        if not nota:
            return None
        return nota