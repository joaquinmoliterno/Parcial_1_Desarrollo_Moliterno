from dataclasses import dataclass
#from app import db
from app.models.grado import Grado


@dataclass(init=False, repr=True, eq=True)
class Grupo():#db.Model):
    #__tablename__= "grupos"

    id: int #= db.Column(db.Integer, primary_key=True)
    nombre:str #= db.Column(db.String(100), nullable= False)
    grado = Grado
    # grado_id = db.Column(db.Integer, db.ForeignKey('grados.id'))
    # grado = db.relationship('Grado', backref='grupos')

    
    