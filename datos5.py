from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker

from genera_tablas import *
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Los establecimientos ordenados por número de estudiantes; que tengan más de 100 profesores
establecimientos = session.query(Establecimiento).filter(Establecimiento.nDocentes > 100).order_by(desc(Establecimiento.nEstudiantes)).all()
print("Los establecimientos ordenados por número de estudiantes; que tengan más de 100 profesores.")
for p in establecimientos:
    print(p,"\n")


# Los establecimientos ordenados por número de profesores; que tengan más de 100 profesores
establecimientos = session.query(Establecimiento).filter(Establecimiento.nDocentes > 100).order_by(desc(Establecimiento.nDocentes)).all()
print("Los establecimientos ordenados por número de profesores; que tengan más de 100 profesores.")
for p in establecimientos:
    print(p,"\n")