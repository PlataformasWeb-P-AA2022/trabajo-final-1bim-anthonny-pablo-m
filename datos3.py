from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_

from genera_tablas import *
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Los cantones que tiene establecimientos con 0 número de profesores, 5 profesores, 11, profesores
parroquias = session.query(Canton).join(Parroquia, Establecimiento).filter(Establecimiento.nDocentes == 0 and Establecimiento.nDocentes == 5 and Establecimiento.nDocentes == 11).all()
print("Los cantones que tiene establecimientos con 0 número de profesores, 5 profesores, 11 profesores")
for p in parroquias:
    print(p,"\n")

# Los establecimientos que pertenecen a la parroquia Pindal con estudiantes mayores o iguales a 21
cantones = session.query(Establecimiento).join(Parroquia).filter(and_(Parroquia.parroquia == "PINDAL", Establecimiento.nEstudiantes >= 21)).all()
print("Los establecimientos que pertenecen a la parroquia Pindal con estudiantes mayores o iguales a 21")
for p in cantones:
    print(p,"\n")