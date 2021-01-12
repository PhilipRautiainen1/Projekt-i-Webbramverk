from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from Data_mysql.db import Base

class Friend(Base):
    __tablename__ = "friends"
    user_id = Column(Integer, ForeignKey("users.id", ondelete="Cascade", onupdate="Cascade"), nullable=False, primary_key=True)
    friend_id = Column(Integer, ForeignKey("users.id", ondelete="Cascade", onupdate="Cascade"), nullable=False, primary_key=True)

    user = relationship("User")
    friend = relationship("Friend")

    def __repr__(self):
        return f"Användare {self.user_id} är vän med {self.friend_id}."