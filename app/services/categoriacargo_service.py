from app.models import CategoriaCargo
from app.repositories.categoriacargo_repositorio import CategoriaCargoRepository



class CategoriaCargoService:

    @staticmethod
    def crear_categoria_cargo(categoria_cargo: CategoriaCargo):
        """
        :param categoria cargo: Objeto CategoriaCargo a crear.
        :return: Objeto CategoriaCargo creado.
        """
        CategoriaCargoRepository.crear(categoria_cargo)
    
    @staticmethod
    def buscar_por_id(id: int) -> CategoriaCargo:
        """
        :param categoria cargo: Objeto CategoriaCargo a crear.
        :return: Objeto CategoriaCargo creado.
        """
        return CategoriaCargoRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[CategoriaCargo]:
        """
        :return: Lista de objetos CategoriaCargo.
        """
        return CategoriaCargoRepository.buscar_todos()
    
    @staticmethod
    def actualizar_categoria_cargo (id: int, categoria_cargo: CategoriaCargo) -> CategoriaCargo:
        """
        :param id: ID de la categoria cargo a actualizar.
        :param categoria cargo: Objeto CategoriaCargo con los nuevos datos.
        :return: Objeto CategoriaCargo actualizado.
        """
        categoria_cargo_existente = CategoriaCargoRepository.buscar_por_id(id)
        if not categoria_cargo_existente:
            return None
        categoria_cargo_existente.nombre = categoria_cargo.nombre

        return categoria_cargo_existente
        
    @staticmethod
    def borrar_por_id(id: int) -> CategoriaCargo:
        """
        :param id: ID de la categoria cargo a borrar.
        :return: Objeto CategoriaCargo borrado o None si no se encuentra.
        """
        categoria_cargo = CategoriaCargoRepository.borrar_por_id(id)
        if not categoria_cargo:
            return None
        return categoria_cargo