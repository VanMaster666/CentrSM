# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import psycopg2


DATABASE_URL = "postgresql+psycopg2://postgres_user:postgres_password@host.docker.internal:5432/postgres"
# работает при подключении с компа
#DATABASE_URL = "postgresql+psycopg2://postgres_user:postgres_password@localhost:5432/postgres" 

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

