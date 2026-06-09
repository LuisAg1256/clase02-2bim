from sqlalchemy.orm import sessionmaker
from modelo import engine, Premio, Serie
import csv

Session = sessionmaker(bind=engine)
session = Session()

with open('../data/premios.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        serie = session.query(Serie).filter_by(titulo=row['serie']).first()
        if not serie:
            serie = Serie(titulo=row['serie'])
        
        premio = Premio(
            id=int(row['id']),
            nombre_premio=row['nombre_premio'],
            categoria=row['categoria'],
            anio=int(row['anio']),
            serie=serie
        )
        session.add(premio)

session.commit()