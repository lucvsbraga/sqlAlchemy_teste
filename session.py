from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class Banco:
    engine = create_engine(
        "mysql+pymysql://root:Senha2mysql.@localhost:3306/bigbox", echo=False)

    Session = sessionmaker(bind=engine)
    session = Session()
