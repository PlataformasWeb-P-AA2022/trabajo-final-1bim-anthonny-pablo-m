from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_tablas import Establecimiento, Parroquia
from configuracion import cadena_base_datos

import csv

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

with open("data/Listado-Instituciones-Educativas.csv", "r", encoding='utf-8') as File:
    read = csv.reader(File, delimiter='|')
    next(read)
    
    for i in read:
        auxiliar = session.query(Parroquia).filter_by(codigo = i[6]).first()        
        est = Establecimiento(amie = i[0], nombre = i[1], distrito = i[8], sostenimiento = i[9], tipo = i[10]
        , modalidad = i[11], jornada = i[12], acceso = i[13], nEstudiantes = int(i[14]), nDocentes = int(i[15]), parroquia = auxiliar)
        session.add(est) 
 
session.commit()