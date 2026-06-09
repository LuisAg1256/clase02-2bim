from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import create_engine

engine = create_engine('sqlite:///../bd/base.db')
Base = declarative_base()

class Pais(Base):
    __tablename__ = 'pais'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    continente = Column(String)

    plataformas = relationship("Plataforma", back_populates="pais")
    series = relationship("Serie", back_populates="pais")
    actores = relationship("Actor", back_populates="pais")

class Plataforma(Base):
    __tablename__ = 'plataforma'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    pais_id = Column(Integer, ForeignKey('pais.id'))
    suscriptores_millones = Column(Float)

    pais = relationship("Pais", back_populates="plataformas")
    series = relationship("Serie", back_populates="plataforma")

class Serie(Base):
    __tablename__ = 'serie'
    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    genero = Column(String)
    anio_estreno = Column(Integer)
    temporadas = Column(Integer)
    plataforma_id = Column(Integer, ForeignKey('plataforma.id'))
    pais_id = Column(Integer, ForeignKey('pais.id'))

    plataforma = relationship("Plataforma", back_populates="series")
    pais = relationship("Pais", back_populates="series")
    actores = relationship("Actor", back_populates="serie")
    premios = relationship("Premio", back_populates="serie")
    
    def obtener_edad_actores(self):
        edades = [e.edad for e in self.actores]
        if len(edades) > 0:
            suma = sum(edades)
            promedio = suma / len(edades)
            return promedio
        else:
            return 0

    def obtener_cantidad_premios(self):
        return len(self.premios)

class Actor(Base):
    __tablename__ = 'actor'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    edad = Column(Integer)
    rol = Column(String)
    pais_id = Column(Integer, ForeignKey('pais.id'))
    serie_id = Column(Integer, ForeignKey('serie.id'))

    pais = relationship("Pais", back_populates="actores")
    serie = relationship("Serie", back_populates="actores")

class Premio(Base):
    __tablename__ = 'premio'
    id = Column(Integer, primary_key=True)
    nombre_premio = Column(String, nullable=False)
    categoria = Column(String)
    anio = Column(Integer)
    serie_id = Column(Integer, ForeignKey('serie.id'))

    serie = relationship("Serie", back_populates="premios")

Base.metadata.create_all(engine)