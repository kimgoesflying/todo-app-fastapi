from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#SQLALCHEMY_DATABASE_URL = 'sqlite:///./todos.db'
SQLALCHEMY_DATABASE_URL = 'mariadb+mariadbconnector://user:user123@192.168.2.116:3306/todoapp'

engine = create_engine(
    #SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
