from sqlalchemy.orm import Session
from core.models import Genero, Pelicula, Actor


# Géneros
def crear_genero(session: Session, nombre: str) -> Genero:
    existente = session.query(Genero).filter_by(nombre=nombre).first()
    if existente:
        raise ValueError("Ya existe un género con ese nombre.")

    genero = Genero(nombre=nombre)
    session.add(genero)
    session.commit()
    session.refresh(genero)
    return genero

# Actores
def crear_actor(session: Session, nombre: str) -> Actor:
    actor = Actor(nombre=nombre)
    session.add(actor)
    session.commit()
    session.refresh(actor)
    return actor

# Películas
def crear_pelicula(
    session: Session, titulo: str, genero: Genero, actores: list[Actor]
) -> Pelicula:
    existente = session.query(Pelicula).filter_by(titulo=titulo).first()
    if existente:
        raise ValueError("Ya existe una película con ese título.")

    pelicula = Pelicula(titulo=titulo, genero=genero, actores=actores)
    session.add(pelicula)
    session.commit()
    session.refresh(pelicula)
    return pelicula


# Leer
def leer_todos_los_generos(session: Session) -> list[Genero]:
    return session.query(Genero).all()


def leer_todos_los_actores(session: Session) -> list[Actor]:
    return session.query(Actor).all()


def leer_todas_las_peliculas(session: Session) -> list[Pelicula]:
    return session.query(Pelicula).all()


def leer_genero_por_id(session: Session, genero_id: int) -> Genero | None:
    return session.get(Genero, genero_id)


def leer_actor_por_id(session: Session, actor_id: int) -> Actor | None:
    return session.get(Actor, actor_id)


def leer_pelicula_por_id(session: Session, pelicula_id: int) -> Pelicula | None:
    return session.get(Pelicula, pelicula_id)


# Actualizar
def actualizar_genero(session: Session, genero_id: int, nuevo_nombre: str) -> Genero:
    genero = leer_genero_por_id(session, genero_id)
    if not genero:
        raise ValueError("Género no encontrado.")
    
    genero.nombre = nuevo_nombre
    session.commit()
    session.refresh(genero)
    return genero


def actualizar_actor(session: Session, actor_id: int, nuevo_nombre: str) -> Actor:
    actor = leer_actor_por_id(session, actor_id)
    if not actor:
        raise ValueError("Actor no encontrado.")
    
    actor.nombre = nuevo_nombre
    session.commit()
    session.refresh(actor)
    return actor


def actualizar_pelicula(
    session: Session,
    pelicula_id: int,
    nuevo_titulo: str,
    nuevo_genero: Genero,
    nuevos_actores: list[Actor],
) -> Pelicula:
    pelicula = leer_pelicula_por_id(session, pelicula_id)
    if not pelicula:
        raise ValueError("Película no encontrada.")

    pelicula.titulo = nuevo_titulo
    pelicula.genero = nuevo_genero
    pelicula.actores = nuevos_actores

    session.commit()
    session.refresh(pelicula)
    return pelicula


# Eliminar
def eliminar_genero(session: Session, genero_id: int) -> None:
    if not leer_genero_por_id(session, genero_id):
        raise ValueError("ID de género inválido.")

    session.query(Genero).filter_by(id=genero_id).delete()
    session.commit()


def eliminar_actor(session: Session, actor_id: int) -> None:
    if not leer_actor_por_id(session, actor_id):
        raise ValueError("ID de actor inválido.")

    session.query(Actor).filter_by(id=actor_id).delete()
    session.commit()


def eliminar_pelicula(session: Session, pelicula_id: int) -> None:
    if not leer_pelicula_por_id(session, pelicula_id):
        raise ValueError("ID de película inválido.")

    session.query(Pelicula).filter_by(id=pelicula_id).delete()
    session.commit()
