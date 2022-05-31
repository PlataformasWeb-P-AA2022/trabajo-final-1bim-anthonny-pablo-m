from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_tablas import Provincia
from config import cadena_base_datos

import csv

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

with open("data/Listado-Instituciones-Educativas.csv", "r", encoding='utf-8') as File:
    read = csv.reader(File, delimiter='|')
    next(read)
    listaprov = []
    for i in read:
        provinciaaux = i[2] + "|" + i[3]
        listaprov.append(provinciaaux)
        listaprov = list(set(listaprov))

    for i in listaprov:
        prov = Provincia(amie = i.split("|")[0], provincia = i.split("|")[1])
        session.add(prov)

session.commit()