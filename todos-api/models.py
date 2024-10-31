from database import Base
from sqlalchemy import Column, Integer, String, Boolean


class Todos(Base):
    __tabblename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    Complete = Column(Boolean, default=False)