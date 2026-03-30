from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# Carrega variáveis do .env
load_dotenv()

# Tentar conexão MySQL primeiro, se falhar usa SQLite
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "dados")

try:
    # Tenta conectar ao MySQL
    engine = create_engine(
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
        pool_pre_ping=True,
        pool_recycle=3600,
        echo=False
    )
    # Testa a conexão
    with engine.connect() as conn:
        print("✓ Conectado ao MySQL com sucesso!")
except Exception as e:
    print(f"⚠ Erro ao conectar ao MySQL: {e}")
    print("→ Usando SQLite como fallback...")
    # Fallback para SQLite
    engine = create_engine(
        "sqlite:///./mercearia.db",
        connect_args={"check_same_thread": False},
        echo=False
    )

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
