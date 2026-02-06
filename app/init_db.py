from .database import Base, engine
from .models import Item # noqa: F401

Base.metadata.create_all(bind=engine)
