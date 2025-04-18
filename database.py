from sqlalchemy import Table, Column ,Integer , String, create_engine ,DateTime
from sqlalchemy.orm import Session , relationship , declarative_base , sessionmaker

engine = create_engine('sqlite:///hospital_database.db', echo=True)
base = declarative_base()

class Patient(base):
    __tablename__ = "patient"
    patientId = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname= Column(String)
    age = Column(Integer)
    gender = Column(String)
    emergencyNumber = Column(Integer)
    dateAndTime = Column(DateTime)
    hospitalName = Column(String, nullable=False)
    wardName = Column(String, nullable=False)
    bedNumber = Column(Integer, nullable=False)
    currentCondition = Column(String, nullable= False)
    fundRequired = Column(Integer,nullable=False)
    urgency = Column(String, nullable=False)
    intialDiagnosis = Column(String, nullable=False)

base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)
session = Session()
session.commit()
