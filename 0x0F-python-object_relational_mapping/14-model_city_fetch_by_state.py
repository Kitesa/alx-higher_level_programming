#!/usr/bin/python3
'''
deletes of a state object that starts with nletter a
'''


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from model_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[0], argv[2], argv[3],
                               pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    query_rows = session.query(City, State).\
        filter(City.state_id == State.id).all()

    for city, state in query_rows:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))


    session.close()
