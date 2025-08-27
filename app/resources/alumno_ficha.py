from flask import Blueprint, request
from app.services.ficha_alumno_service import FichaAlumnoService
from app.renderers import JSONFichaRenderer, PDFFichaRenderer

alumno_ficha_bp = Blueprint("alumno_ficha", __name__)

@alumno_ficha_bp.route("/alumnos/<int:alumno_id>/ficha", methods=["GET"])
def ficha_alumno(alumno_id: int):
    """
    GET /alumnos/<id>/ficha?formato=json|pdf
    - Por defecto: JSON
    """
    dto = FichaAlumnoService.obtener_ficha(alumno_id)
    if not dto:
        return {"mensaje": "Alumno no encontrado"}, 404

    formato = (request.args.get("formato") or "json").lower()
    if formato == "pdf":
        return PDFFichaRenderer().render(dto)
    return JSONFichaRenderer().render(dto)
