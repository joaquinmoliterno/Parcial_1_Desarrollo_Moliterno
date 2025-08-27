from app.models import Cargo
from app.repositories.cargo_repositorio import CargoRepository



class CargoService:

    @staticmethod
    def crear_cargo(cargo: Cargo):
        """
        :param cargo: Objeto Cargo a crear.
        :return: Objeto Cargo creado.
        """
        CargoRepository.crear(cargo)
    
    @staticmethod
    def buscar_por_id(id: int) -> Cargo:
        """
        :param cargo: Objeto Cargo a crear.
        :return: Objeto Cargo creado.
        """
        return CargoRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[Cargo]:
        """
        :return: Lista de objetos Cargo.
        """
        return CargoRepository.buscar_todos()
    
    @staticmethod
    def actualizar_cargo (id: int, cargo: Cargo) -> Cargo:
        """
        :param id: ID de la cargo a actualizar.
        :param cargo: Objeto Cargo con los nuevos datos.
        :return: Objeto Cargo actualizado.
        """
        cargo_existente = CargoRepository.buscar_por_id(id)
        if not cargo_existente:
            return None
        cargo_existente.nombre = cargo.nombre
        cargo_existente.categoria_cargo_id = cargo.categoria_cargo_id
        cargo_existente.tipo_dedicacion_id = cargo.tipo_dedicacion_id
        cargo_existente.id = cargo.id
        cargo_existente.puntos = cargo.puntos

        return cargo_existente
        
    @staticmethod
    def borrar_por_id(id: int) -> Cargo:
        """
        :param id: ID de la cargo a borrar.
        :return: Objeto Cargo borrado o None si no se encuentra.
        """
        cargo = CargoRepository.borrar_por_id(id)
        if not cargo:
            return None
        return cargo
    
        