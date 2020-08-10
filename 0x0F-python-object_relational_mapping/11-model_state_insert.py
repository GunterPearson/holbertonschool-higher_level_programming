#!/usr/bin/python3
""" add state """
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.
        format(sys.argv[1], sys.argv[2],
               sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    sesh = Session()
    louisiana = State(name="Louisiana")
    sesh.add(louisiana)
    sesh.commit()
    print(louisiana.id)
