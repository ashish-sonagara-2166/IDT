from sqlalchemy import Table, Column ,Integer , String, create_engine
from sqlalchemy.orm import Session , relationship , declarative_base

engine = create_engine('sqlite:///hospital_database.db', echo=True)
base = declarative_base()

class Patient(base):
    __table__ = "pateint"
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname= Column(String)
    age = Column(Integer)
    gender = Column(String)
    emergencyNumber = Column(Integer)
    dateAndTime = Column()
    hospitalName = Column(String, nullable=False)
    wardName = Column(String, nullable=False)
    bedNumber = Column(Integer, nullable=False)
    currentCondition = Column(String, nullable= False)
    fundRequired = Column(Integer,nullable=False)
    urgency = Column(String, nullable=False)
    intialDiagnosis = Column(String, nullable=False)