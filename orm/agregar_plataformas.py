from sqlalchemy.orm import sessionmaker
from modelo import engine, Plataforma, Pais
import csv

Session = sessionmaker(bind=engine)
session = Session()

with open('../data/plataformas.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        pais = session.query(Pais).filter_by(nombre=row['pais']).first()
        if not pais:
            pais = Pais(nombre=row['pais'])
        
        plataforma = Plataforma(
            id=int(row['id']),
            nombre=row['nombre'],
            pais=pais,
            suscriptores_millones=float(row['suscriptores_millones']) if row['suscriptores_millones'] else None
        )
        session.add(plataforma)

session.commit()