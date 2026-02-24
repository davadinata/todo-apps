from sqlmodel import create_engine, Session
from app.core.settings import settings
# engine = create_engine("sqlite:///database.db")
engine = create_engine(settings.DB_URL)

def get_db():
    with Session(engine) as session:
        yield session