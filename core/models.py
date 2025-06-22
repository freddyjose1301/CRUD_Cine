from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship

Base = declarative_base()

# Tabla asociativa para Película - Actor (M:N)
pelicula_actor = Table(
    "pelicula_actor", 
    Base.metadata,
    Column("pelicula_id", ForeignKey("peliculas.id"), primary_key=True),
    Column("actor_id", ForeignKey("actores.id"), primary_key=True)
)

# Tabla Género
class Genero(Base):
    __tablename__ = "generos"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(nullable=False, unique=True)

    peliculas: Mapped[list["Pelicula"]] = relationship(back_populates="genero")

    def __repr__(self):
        return f"<Genero(id={self.id}, nombre='{self.nombre}')>"

# Tabla Película
class Pelicula(Base):
    __tablename__ = "peliculas"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    titulo: Mapped[str] = mapped_column(nullable=False)
    genero_id: Mapped[int] = mapped_column(ForeignKey("generos.id"))

    genero: Mapped["Genero"] = relationship(back_populates="peliculas")

    actores: Mapped[list["Actor"]] = relationship(
        secondary=pelicula_actor,
        back_populates="peliculas"
    )

    def __repr__(self):
        return f"<Pelicula(id={self.id}, titulo='{self.titulo}')>"

# Tabla Actor
class Actor(Base):
    __tablename__ = "actores"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(nullable=False)

    peliculas: Mapped[list["Pelicula"]] = relationship(
        secondary=pelicula_actor,
        back_populates="actores"
    )

    def __repr__(self):
        return f"<Actor(id={self.id}, nombre='{self.nombre}')>"
