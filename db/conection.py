from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from contextlib import contextmanager

DATABASE_URL = "sqlite:///./db.sqlite"

# Creando el engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Creando la session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@contextmanager
def db_session():
    db: Session = SessionLocal()

    try:
        yield db
        db.commit
    except:
        db.rollback()
    finally:
        db.close()