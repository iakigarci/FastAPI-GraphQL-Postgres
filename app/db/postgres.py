from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from doctest import master
from sqlalchemy import Column, Integer, String
Base = declarative_base()

engine = create_engine('postgresql://user:password@localhost:5432/db_scrapad')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# with session_maker() as session:
#     for ad in ads:
#         session.add(ad)
#     session.commit()

# with session_maker() as session:
#     records = session.query(Ad).all()
#     for ad in records:
#         print(ad.name)

def get_db():
    # db = SessionLocal()
    # try:
    #     yield db
    # finally:
    #     db.close()
    return SessionLocal()
