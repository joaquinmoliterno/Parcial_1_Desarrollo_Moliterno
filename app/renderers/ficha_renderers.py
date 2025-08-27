from abc import ABC, abstractmethod
from io import BytesIO
from flask import jsonify, send_file

class IFichaRenderer(ABC):
    @abstractmethod
    def render(self, ficha_dto):
        ...

class JSONFichaRenderer(IFichaRenderer):
    def render(self, ficha_dto):
        return jsonify(ficha_dto.to_dict()), 200

class PDFFichaRenderer(IFichaRenderer):
    def render(self, ficha_dto):
        # Requiere: pip install reportlab
        from reportlab.pdfgen import canvas
        from reportlab.lib.pagesizes import A4

        buffer = BytesIO()
        c = canvas.Canvas(buffer, pagesize=A4)
        width, height = A4

        def line(y, text):
            c.drawString(50, y, text)
            return y - 18

        y = height - 50
        c.setFont("Helvetica-Bold", 14)
        y = line(y, "Ficha del Alumno")
        c.setFont("Helvetica", 11)
        y = line(y, f"ID: {ficha_dto.id}")
        y = line(y, f"Nro de Legajo: {ficha_dto.nro_legajo}")
        y = line(y, f"Apellido y Nombre: {ficha_dto.apellido}, {ficha_dto.nombre}")
        y = line(y, f"Documento: {ficha_dto.nro_documento}")
        y = line(y, f"Fecha de Nacimiento: {ficha_dto.fecha_nacimiento}")
        y = line(y, f"Sexo: {ficha_dto.sexo}")
        y = line(y, f"Fecha de Ingreso: {ficha_dto.fecha_ingreso}")
        y = line(y, f"Facultad: {ficha_dto.facultad or 'No registrada'}")

        c.showPage()
        c.save()
        buffer.seek(0)

        filename = f"ficha_alumno_{ficha_dto.id}.pdf"
        return send_file(
            buffer,
            mimetype="application/pdf",
            as_attachment=True,
            download_name=filename
        )
