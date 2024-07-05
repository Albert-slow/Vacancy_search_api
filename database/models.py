from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, Float, Date, Boolean, BigInteger
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String, unique=True)
    user_location = Column(String, nullable=False)
    tg_id = Column(Integer, nullable=False)
    reg_date = Column(DateTime)
    update_time = Column(DateTime)


class UserJob(Base):
    __tablename__ = "messages"
    job_id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    job_title = Column(String)
    job_city = Column(String)
    jobs_tag = Column(String)
    reg_date = Column(DateTime)
    update_time = Column(DateTime)

    user_fk = relationship(User, lazy="subquery")
