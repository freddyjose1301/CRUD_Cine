import datetime
from db.conection import db_session
from core.controllers import *
from core.models import Genero, Pelicula, Actor

#Funciones
#Opcion 1: Crear Género
def crear_genero_view() -> None:
    print("=== Crear nuevo género ===")
    nombre = input("Nombre del género: ").strip()
    with db_session() as session:
        try:
            genero = crear_genero(session, nombre)
            print(f"✅ Género creado: {genero.nombre}")
        except ValueError as e:
            print(f"❌ Error: {e}")

# Opcion 2: Crear Actor
def crear_actor_view() -> None:
    print("=== Crear nuevo actor ===")
    nombre = input("Nombre del actor: ").strip()
    with db_session() as session:
        actor = crear_actor(session, nombre)
        print(f"✅ Actor creado: {actor.nombre}")

# Opcion 3: Crear Película
def crear_pelicula_view() -> None:
    print("=== Crear nueva película ===")
    titulo = input("Título: ").strip()

    with db_session() as session:
        generos = leer_todos_los_generos(session)
        actores = leer_todos_los_actores(session)

        if not generos:
            print("❌ No hay géneros disponibles.")
            return
        if not actores:
            print("❌ No hay actores disponibles.")
            return

        print("Géneros disponibles:")
        for g in generos:
            print(f"{g.id}: {g.nombre}")
        genero_id = int(input("ID del género: ").strip())
        genero = leer_genero_por_id(session, genero_id)
        if not genero:
            print("❌ Género no encontrado.")
            return

        print("Actores disponibles:")
        for a in actores:
            print(f"{a.id}: {a.nombre}")
        ids = input("IDs de actores separados por coma: ").strip()
        actor_ids = [int(i.strip()) for i in ids.split(",") if i.strip().isdigit()]
        actores_seleccionados = [
            a for a in actores if a.id in actor_ids
        ]

        try:
            pelicula = crear_pelicula(session, titulo, genero, actores_seleccionados)
            print(f"✅ Película creada: {pelicula.titulo}")
        except ValueError as e:
            print(f"❌ Error: {e}")

# Opcion 4: Ver Géneros
def ver_generos_view() -> None:
    print("=== Lista de Géneros ===")
    with db_session() as session:
        generos = leer_todos_los_generos(session)
        for g in generos:
            print(f"{g.id}: {g.nombre}")

# Opcion 5: Ver Actores
def ver_actores_view() -> None:
    print("=== Lista de Actores ===")
    with db_session() as session:
        actores = leer_todos_los_actores(session)
        for a in actores:
            print(f"{a.id}: {a.nombre}")

# Opcion 6: Ver Películas
def ver_peliculas_view() -> None:
    print("=== Lista de Películas ===")
    with db_session() as session:
        peliculas = leer_todas_las_peliculas(session)
        for p in peliculas:
            actores = ", ".join([a.nombre for a in p.actores])
            print(f"{p.id}: {p.titulo} | Género: {p.genero.nombre} | Actores: {actores}")

# Opcion 7: Actualizar Película
def actualizar_pelicula_view() -> None:
    print("=== Actualizar película ===")
    with db_session() as session:
        peliculas = leer_todas_las_peliculas(session)
        for p in peliculas:
            print(f"{p.id}: {p.titulo}")
        pelicula_id = int(input("ID de la película a actualizar: ").strip())

        pelicula = leer_pelicula_por_id(session, pelicula_id)
        if not pelicula:
            print("❌ Película no encontrada.")
            return

        nuevo_titulo = input("Nuevo título: ").strip()

        generos = leer_todos_los_generos(session)
        for g in generos:
            print(f"{g.id}: {g.nombre}")
        genero_id = int(input("Nuevo ID de género: ").strip())
        nuevo_genero = leer_genero_por_id(session, genero_id)
        if not nuevo_genero:
            print("❌ Género no válido.")
            return

        actores = leer_todos_los_actores(session)
        for a in actores:
            print(f"{a.id}: {a.nombre}")
        actor_ids = input("IDs de actores separados por coma: ").strip()
        nuevos_actores = session.query(Actor).filter(
            Actor.id.in_([int(i.strip()) for i in actor_ids.split(",") if i.strip().isdigit()])
        ).all()

        try:
            pelicula_actualizada = actualizar_pelicula(
                session,
                pelicula_id,
                nuevo_titulo,
                nuevo_genero,
                nuevos_actores
            )
            print(f"✅ Película actualizada: {pelicula_actualizada.titulo}")
        except ValueError as e:
            print(f"❌ Error: {e}")

# Opcion 8: Eliminar Película
def eliminar_pelicula_view() -> None:
    print("=== Eliminar película ===")
    with db_session() as session:
        peliculas = leer_todas_las_peliculas(session)
        for p in peliculas:
            print(f"{p.id}: {p.titulo}")
        pelicula_id = int(input("ID de la película a eliminar: ").strip())
        try:
            eliminar_pelicula(session, pelicula_id)
            print("✅ Película eliminada.")
        except ValueError as e:
            print(f"❌ Error: {e}")
