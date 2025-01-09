from core.database import Base, engine
from . import user

Base.metadata.create_all(bind=engine)
