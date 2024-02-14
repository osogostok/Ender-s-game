import sqlalchemy as db
from sqlalchemy.orm import declarative_base, Session, aliased
import sys
import os
import json
import argparse
import grpc
from dotenv import load_dotenv
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ex00.reporting_client import get_ships
from ex01.reporting_client_v2 import check_ship

load_dotenv()
user = os.getenv("USET_DB")
password = os.getenv("PASSWORD")
host = os.getenv("HOST_DB")
port = os.getenv("PORT")
database = os.getenv("DATABASE")

metadata = db.MetaData()
connection_str = f'postgresql://{user}:{password}@{host}:{port}/{database}'

engine = db.create_engine(connection_str)
Base = declarative_base()


class Ships(Base):
    __tablename__ = "table_ship"

    id = db.Column(db.Integer, primary_key=True)
    alignment = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text, nullable=False)
    class_ship = db.Column(db.Text, nullable=False)
    length = db.Column(db.Float, nullable=False)
    crew_size = db.Column(db.Integer, nullable=False)
    armed = db.Column(db.Boolean, nullable=False)


class Officers(Base):
    __tablename__ = "table_officers"

    id = db.Column(db.Integer, primary_key=True)
    id_ship = db.Column(db.Integer, db.ForeignKey("table_ship.id"))
    first_name = db.Column(db.Text, nullable=False)
    second_name = db.Column(db.Text, nullable=False)
    rank = db.Column(db.Text, nullable=False)


Base.metadata.create_all(engine)


def parse_arg():
    parser = argparse.ArgumentParser(description="Coordinate")
    parser.add_argument('action', choices=['scan', 'list_traitors'])
    parser.add_argument('coordinate', type=float, nargs='*')
    return parser.parse_args()


def insert_table_ships(ship):
    ship_data = json.loads(ship)
    if not is_dublicate(ship_data):
        session = Session(bind=engine)
        new_ship = Ships(
            alignment=ship_data['alignment'],
            name=ship_data['name'],
            class_ship=ship_data['class_ship'],
            length=ship_data['length'],
            crew_size=ship_data['crew_size'],
            armed=ship_data['armed']
        )
        session.add(new_ship)
        session.commit()
        session.refresh(new_ship)
        for officer in ship_data['officers']:
            new_officer = Officers(
                id_ship=new_ship.id,
                first_name=officer['first_name'],
                second_name=officer['last_name'],
                rank=officer['rank']
            )
            session.add(new_officer)
        session.commit()


def is_dublicate(ship):
    session = Session(bind=engine)
    select_ships = session.query(Ships).filter(Ships.name == ship['name'])
    for s in select_ships:
        select_officers = session.query(
            Officers).filter(Officers.id_ship == s.id)
        list_select = []
        for officer in select_officers:
            list_select.append({"first_name": officer.first_name,
                                "last_name": officer.second_name,
                                "rank": officer.rank})
        flag_res = True
        for i in ship['officers']:
            if i not in list_select:
                flag_res = False
                break
        if flag_res:
            return True
    return False


def find_traitors():
    session = Session(bind=engine)
    officers_alias_ally = aliased(Officers)
    officers_alias_enemy = aliased(Officers)
    query_ally = get_officers(officers_alias_ally, 'Ally')
    query_enemy = get_officers(officers_alias_enemy, 'Enemy')
    final_query = query_ally.intersect(query_enemy)
    result = final_query.all()
    if result:
        result_dicts = [
            {"first_name": row[0], "last_name": row[1], "rank": row[2]}
            for row in result
        ]
        for officer_dict in result_dicts:
            print(officer_dict)


def get_officers(officers_alias, alignment):
    session = Session(bind=engine)
    return (
        session.query(
            officers_alias.first_name,
            officers_alias.second_name,
            officers_alias.rank
        )
        .join(Ships)
        .filter(officers_alias.id_ship == Ships.id)
        .filter(Ships.alignment == alignment)
    )


if __name__ == '__main__':
    parse = parse_arg()
    try:
        if parse.action == 'scan':
            with grpc.insecure_channel('localhost:50051') as chanel:
                for message in get_ships(chanel, parse.coordinate):
                    if check_ship(message):
                        insert_table_ships(message)
                        print(message)
        if parse.action == 'list_traitors':
            find_traitors()
    except Exception as e:
        print(f"Error: {e}")
