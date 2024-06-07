from sqlalchemy import create_engine , ForeignKey , Column , String , Integer , CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Person (Base) :
    __tablename__ = "people"

    id = Column ("id" , Integer , primary_key=True)
    first_name = Column ("first_name" , String)
    last_name = Column ("last_name" , String)

    def __init__ (self, id , first_name , last_name) :
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
    
    def __repr__ (self) : 
        return f"id : {self.id} , first_name : {self.first_name} , last_name : {self.last_name}"

engine = create_engine('postgresql+psycopg2://postgres:QaZxcv54321@localhost/test' , echo=True)

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

person = Person(2 , "2" , "2")
session.add(person)
session.commit()
