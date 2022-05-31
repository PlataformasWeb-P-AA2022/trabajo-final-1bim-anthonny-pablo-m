from sqlalchemy import column, create_engine, false, null, true
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from config import cadena_base_datos

engine = create_engine(cadena_base_datos)
Base = declarative_base()

class Establecimiento(Base):
    __tablename__ = 'establecimiento'
    amie = Column(String(20), primary_key=True)
    nombre = Column(String(100), nullable=false)
    distrito = Column(String(30), nullable=false)
    sostenimiento = Column(String(30), nullable=false)
    tipo = Column(String(40), nullable=false)
    modalidad = Column(String(20), nullable=false)
    jornada = Column(String(30), nullable=false)
    acceso = Column(String(20), nullable=false)
    nEstudiantes = Column(Integer, nullable=false)
    nDocentes = Column(Integer, nullable=false)
    parroquia = relationship("Parroquia", back_populates="establecimientos")
    parroquiaid = Column(String(20), ForeignKey('parroquia.amie'), primary_key=True)
    
    def __repr__(self):
        return "Establecimiento: Nombre=%s - Numero de distrito=%s - Sostenimiento=%s - Tipo=%s - Modalidad=%s - Jornada=%s - Acceso=%s - Numero de Estudiantes=%d - Numero de Docenctes=%d"% (
                          self.nombre, 
                          self.distrito,
                          self.sostenimiento,
                          self.tipo,
                          self.modalidad,
                          self.jornada,
                          self.acceso,
                          self.nEstudiantes,
                          self.nDocentes)

class Parroquia(Base):
    __tablename__ = 'parroquia'
    amie = Column(String(20), primary_key=True)
    parroquia = Column(String(30), nullable=False)
    establecimientos = relationship("Establecimiento", back_populates="parroquia")
    canton = relationship("Canton", back_populates="parroquias")
    canton_id = Column(String(20), ForeignKey('canton.amie'), primary_key=True)

    def __repr__(self):
        return "Parroquia: Codigo Amie=%s - Nombre=%s"%(
            self.amie,
            self.parroquia
            )

class Canton(Base):
    __tablename__ = 'canton'
    amie = Column(String(20), primary_key=True)
    canton = Column(String(30), nullable=False)
    parroquias = relationship("Parroquia", back_populates="canton")
    provincia = relationship("Provincia", back_populates="cantones")
    provincia_id = Column(String(20), ForeignKey('provincia.amie'), primary_key=True)

    def __repr__(self):
        return "Canton: Codigo Amie=%s - Nombre=%s"%(
            self.amie,
            self.canton
            )


class Provincia(Base):
    __tablename__ = 'provincia'
    amie = Column(String(20), primary_key=True)
    provincia = Column(String(30), nullable=False)
    cantones = relationship("Canton", back_populates="provincia")

    def __repr__(self):
        return "Provincia: Codigo Amie=%s - Nombre=%s"%(
            self.amie,
            self.provincia
            )

Base.metadata.create_all(engine)