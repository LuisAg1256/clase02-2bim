from sqlalchemy.orm import sessionmaker
from modelo import engine, Actor, Pais, Serie
import csv

Session = sessionmaker(bind=engine)
session = Session()

with open('../data/actores.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        pais = session.query(Pais).filter_by(nombre=row['pais']).first()
        if not pais:
            pais = Pais(nombre=row['pais'], continente='Desconocido')
            
        serie = session.query(Serie).filter_by(titulo=row['serie']).first()
        if not serie:
            serie = Serie(titulo=row['serie'])
        
        actor = Actor(
            id=int(row['id']),
            nombre=row['nombre'],
            edad=int(row['edad']),
            rol=row.get('rol', ''),
            pais=pais,
            serie=serie
        )
        session.add(actor)

session.commit()