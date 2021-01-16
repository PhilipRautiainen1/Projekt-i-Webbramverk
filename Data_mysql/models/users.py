from sqlalchemy import *
from sqlalchemy.orm import relationship
from Data_mysql.db import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(60),nullable=False)
    username = Column(String(20), nullable=False)
    password = Column(VARCHAR(255), nullable=False)
    score = Column(Integer, nullable=False)

    friends = relationship("Friend", secondary='friends')

    def __repr__(self):
        return f"{self.username} ({self.id})"
