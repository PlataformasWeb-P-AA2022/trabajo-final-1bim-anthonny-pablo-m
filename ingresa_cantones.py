from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_tablas import Canton, Provincia
from configuracion import cadena_base_datos

import csv

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

with open("data/Listado-Instituciones-Educativas.csv", "r", encoding='utf-8') as File:
    read = csv.reader(File, delimiter='|')
    next(read)
    listacanton = []
    for i in read:
        cantonaux = i[2] + "|" + i[4] + "|" + i[5]
        listacanton.append(cantonaux)
    listacanton = list(set(listacanton))

    
    for i in listacanton:
        auxiliar = session.query(Provincia).filter_by(amie = i.split("|")[0]).first()
        can = Canton(amie = i.split("|")[1], canton = i.split("|")[2], provincia = aux)
        session.add(can)

session.commit()