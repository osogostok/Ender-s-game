import grpc
import json
import argparse
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from protos import file_pb2_grpc as pb2_grpc
from protos import file_pb2 as pb2


def parse_coordinate():
    parser = argparse.ArgumentParser(description="Coordinates")
    parser.add_argument('coordinate', type=float,
                        nargs='+', help="Enter coordinates")
    return parser.parse_args().coordinate


def select_officers(officers):
    return [{"first_name": officer.first_name, "last_name": officer.second_name,
             "rank": officer.rank} for officer in officers]


def get_ships(chanel, coordinates):
    stub = pb2_grpc.SpaceStub(chanel)
    for ship in stub.get_ships(pb2.Coordinates(pos=coordinates)):
        ship_dict = {
            "alignment": pb2.Ship.AlignmentType.Name(ship.alignment),
            "name": ship.name,
            "class_ship": pb2.Ship.ClassShipType.Name(ship.class_ship),
            "length": ship.length,
            "crew_size": ship.size,
            "armed": ship.armed,
            "officers": select_officers(ship.oficer)
        }
        yield json.dumps(ship_dict, indent=2)


if __name__ == '__main__':
    coordinates = parse_coordinate()
    try:
        with grpc.insecure_channel('localhost:50051') as chanel:
            for message in get_ships(chanel, coordinates):
                print(message)
    except Exception as e:
        print(f"Error: {e}")
