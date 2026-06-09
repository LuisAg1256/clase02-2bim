from sqlalchemy.orm import sessionmaker
from modelo import engine, Serie, Plataforma, Pais
import csv

Session = sessionmaker(bind=engine)
session = Session()

with open('../data/series.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        pais = session.query(Pais).filter_by(nombre=row['pais']).first()
        if not pais:
            pais = Pais(nombre=row['pais'])
            
        plataforma = session.query(Plataforma).filter_by(nombre=row['plataforma']).first()
        if not plataforma:
            plataforma = Plataforma(nombre=row['plataforma'])
        
        serie = Serie(
            id=int(row['id']),
            titulo=row['titulo'],
            genero=row['genero'],
            anio_estreno=int(row['anio_estreno']),
            temporadas=int(row['temporadas']),
            plataforma=plataforma,
            pais=pais
        )
        session.add(serie)

session.commit()