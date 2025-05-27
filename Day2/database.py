from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQL_DB = "sqlite:///./mytest.db"

engine = create_engine(
    SQL_DB, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative models
Base = declarative_base()

# Example usage: Define a function to get a database session
def get_connection():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()