from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from modelo import engine, Serie, Actor

Session = sessionmaker(bind=engine)
session = Session()
resultados = session.query(
    Serie.titulo, 
    func.avg(Actor.edad).label('promedio_edad')
).join(Actor).group_by(Serie.id).all()

for r in resultados:
    promedio = round(r.promedio_edad, 2) if r.promedio_edad else "Sin actores"
    print(f"Serie: {r.titulo} | Promedio de edad: {promedio}")
    print("-" * 54)
