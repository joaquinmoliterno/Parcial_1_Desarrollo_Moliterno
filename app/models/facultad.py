from dataclasses import dataclass


"""class Facultad():
    def __init__(self):
        self.nombre = None
        self.abreviatura = None
        self.directorio = None
        self.sigla = None
        self.codgopostal = None
        self.ciudad = None
        self.domicilio = None
        self.telefono = None
        self.contacto = None
        self.email = None"""
        

@dataclass(init=False,repr=True,eq=True)

class Facultad():
    nombre : str
    abreviatura : str
    directorio : str
    sigla : str
    codigoPostal : str
    ciudad : str
    domicilio : str
    telefono : str
    contacto : str
    email : str