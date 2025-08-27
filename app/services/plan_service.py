from app.models import Plan
from app.repositories.plan_repositorio import PlanRepository

class PlanService:

    @staticmethod
    def crear_plan(plan: Plan):
        """
        :param plan: Plan a crear.
        :return: Plan creada.
        """
        PlanRepository.crear(plan)
    
    @staticmethod
    def buscar_por_id(id: int) -> Plan:
        """
        :param id: ID de la plan a buscar.
        :return: Plan encontrada o None si no se encuentra.
        """
        return PlanRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[Plan]:
        """
        :return: Lista de plan.
        """
        return PlanRepository.buscar_todos()
    
    @staticmethod
    def actualizar_plan(id: int, plan: Plan) -> Plan:
        """
        :param id: ID de la plan a actualizar.
        :param plan: Objeto Plan con los nuevos datos.
        :return: Objeto Plan actualizada.
        """
        plan_existente = PlanRepository.buscar_por_id(id)
        if not plan_existente:
            return None
        plan_existente.nombre = plan.nombre
        plan_existente.fecha_inicio = plan.fecha_inicio
        plan_existente.fecha_fin = plan.fecha_fin
        plan_existente.observacion = plan.observacion
        return plan_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> Plan:
        """
        :param id: ID de la plan a borrar.
        :return: Objeto Plan borrado o None si no se encuentra.
        """

        plan = PlanRepository.borrar_por_id(id)
        if not plan:
            return None
        return plan