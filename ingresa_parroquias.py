from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_tablas import Parroquia, Canton
from config import cadena_base_datos

import csv

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

with open("data/Listado-Instituciones-Educativas.csv", "r", encoding='utf-8') as File:
    read = csv.reader(File, delimiter='|')
    next(read)
    listapar = []
    for i in read:
        parroquiaaux = i[4] + "|" + i[6] + "|" + i[7]
        listapar.append(parroquiaaux)
    listapar = list(set(listapar))

    for i in listapar:
        auxiliar = session.query(Canton).filter_by(amie = i.split("|")[0]).first()
        cant = Parroquia(amie = i.split("|")[1], parroquia = i.split("|")[2], canton = auxiliar)
        session.add(cant)

session.commit()