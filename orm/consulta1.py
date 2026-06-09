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


print("--- Usando el método de clase ---")
resultados1 = session.query(Serie).all()
for serie in resultados1:
    promedio = serie.obtener_edad_actores()
    cantidad_premios = serie.obtener_cantidad_premios()
    print(f"Serie: {serie.titulo} | Promedio (con método): {promedio:.2f} | Premios: {cantidad_premios}")