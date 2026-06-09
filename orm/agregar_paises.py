from sqlalchemy.orm import sessionmaker
from modelo import engine, Pais
import csv

Session = sessionmaker(bind=engine)
session = Session()

with open('../data/paises.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        pais = session.query(Pais).filter_by(id=int(row['id'])).first()
        if not pais:
            pais = Pais(
                id=int(row['id']),
                nombre=row['nombre'],
                continente=row['continente']
            )
            session.add(pais)

session.commit()