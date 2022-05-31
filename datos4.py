from sqlalchemy import create_engine, desc, and_
from sqlalchemy.orm import sessionmaker

from genera_tablas import *
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Los establecimientos ordenados por nombre de parroquia que tengan más de 40 profesores y la cadena "Educación regular" en tipo de educación.
establecimientos = session.query(Establecimiento).join(Parroquia).filter(and_(Establecimiento.nDocentes > 40 , Establecimiento.tipo.like("%Educación regular%"))).order_by(desc(Parroquia.parroquia)).all()
print("Los establecimientos ordenados por nombre de parroquia que tengan más de 40 profesores y la cadena Educación regular en tipo de educación")
for p in establecimientos:
    print(p,"\n")

# Todos los establecimientos ordenados por sostenimiento y tengan código de distrito 11D04.
establecimientos = session.query(Establecimiento).filter(Establecimiento.distrito == "11D04").order_by(desc(Establecimiento.sostenimiento)).all()
print("Todos los establecimientos ordenados por sostenimiento y tengan código de distrito 11D04.")
for p in establecimientos:
    print(p,"\n")