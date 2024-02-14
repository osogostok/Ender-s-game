import random
import grpc
from concurrent import futures
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from protos import file_pb2 as pb2
from protos import file_pb2_grpc as pb2_grpc

NAMES = ["Death Star", "Millennium Falcon",
         "Star Destroyer", "Normandy SR-2", "Unreliable"]
CLASSES = ["Corvette", "Frigate", "Cruiser",
           "Destroyer", "Carrier", "Dreadnought"]
FIRST_NAMES = ["Astrid", "Orion", "Nova", "Luna"]
SECOND_NAMES = ["Stellar", "Nebula", "Cosmos", "Galaxy"]
RANKS = ["Captain", "Admiral", "Commander"]


class Space(pb2_grpc.SpaceServicer):
    def get_ships(self, request, context):
        # print(f'Сoordinates: {request.pos}')
        return self.generate_ship()

    def generate_ship(self):
        for _ in range(random.randint(1, 10)):
            ship = pb2.Ship()
            ship.alignment = random.randint(0, 1)
            ship.name = random.choice(NAMES)
            ship.length = random.uniform(70, 21000)
            ship.class_ship = random.choice(CLASSES)
            ship.size = random.randint(2, 510)
            ship.armed = random.choice([True, False])
            min_officers = 0 if ship.alignment == pb2.Ship.Enemy else 1
            count_officers = random.randint(min_officers, 10)
            for _ in range(count_officers):
                officer = ship.oficer.add()
                officer.first_name = random.choice(FIRST_NAMES)
                officer.second_name = random.choice(SECOND_NAMES)
                officer.rank = random.choice(RANKS)
            yield ship


def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_SpaceServicer_to_server(Space(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    server()
