from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_

from genera_tablas import *
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Las parroquias que tienen establecimientos únicamente en la jornada "Matutina y Vespertina"
parroquias = session.query(Parroquia).join(Establecimiento).filter(Establecimiento.jornada == 'Matutina y Vespertina').all()
print("Las parroquias que tienen establecimientos únicamente en la jornada Matutina y Vespertina.")
for p in parroquias:
    print(p,"\n")


# Los cantones que tiene establecimientos como número de estudiantes tales como: 448, 450, 451, 454, 458, 459
cantones = session.query(Canton).join(Parroquia, Establecimiento).filter(or_(Establecimiento.nEstudiantes == 448 , 
    Establecimiento.nEstudiantes == 450,
    Establecimiento.nEstudiantes == 451,
    Establecimiento.nEstudiantes == 454,
    Establecimiento.nEstudiantes == 458,
    Establecimiento.nEstudiantes == 459
    )).all()
print("Los cantones que tiene establecimientos como número de estudiantes tales como: 448, 450, 451, 454, 458, 459")
for p in cantones:
    print(p,"\n")