import os
import time

from core.models import Base
from db.conection import engine
from core.views import *

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)


def wait_and_clear(s: int) -> None:
    time.sleep(s)
    os.system("cls" if os.name == "nt" else "clear")


OPT: dict[str, callable] = {
    "1": crear_genero_view,
    "2": crear_actor_view,
    "3": crear_pelicula_view,
    "4": ver_generos_view,
    "5": ver_actores_view,
    "6": ver_peliculas_view,
    "7": actualizar_pelicula_view,
    "8": eliminar_pelicula_view,
}

#Menú
def main() -> None:
    while True:
        print("=== 🎬 CRUD de Películas y Series con SQLAlchemy ===\n")
        print("1. Crear Género")
        print("2. Crear Actor")
        print("3. Crear Película")
        print("4. Ver Géneros")
        print("5. Ver Actores")
        print("6. Ver Películas")
        print("7. Actualizar Película")
        print("8. Eliminar Película")
        print("0. Salir")

        opcion = input("\nSelecciona una opción: ").strip()

        if opcion == "0":
            print("👋 ¡Hasta pronto!")
            break
        elif opcion in OPT:
            wait_and_clear(0)
            OPT[opcion]()
            if opcion in {"4", "5", "6"}:
                input("\nPresiona ENTER para continuar...")
            wait_and_clear(1)
        else:
            print("❌ Opción inválida.")
            wait_and_clear(1)


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    main()
