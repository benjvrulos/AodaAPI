from database import Base
from sqlalchemy import Column, Integer, String, DateTime,Boolean
from datetime import datetime, timezone

class Derivation(Base):
    __tablename__ = "derivations"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)
    description = Column(String)
    state = Column(String, default="pendiente")
    migrate_situation = Column(Boolean,default=False)
    sex = Column(String)
    age = Column(Integer)
    comuna = Column(String)
    region = Column(String)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))