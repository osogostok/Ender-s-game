from typing import List
import grpc
import sys
import os
from pydantic import BaseModel, model_validator, ValidationError, field_validator, root_validator
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ex00.reporting_client import get_ships, parse_coordinate


class Officer(BaseModel):
    first_name: str = None
    second_name: str = None
    rank: str = None


class BaseShip(BaseModel):
    alignment: str
    name: str
    length: float
    class_ship: str
    crew_size: int
    armed: bool
    officers: List[Officer]

    @model_validator(mode='after')
    def check_model(self):
        ship_classes = {
            'Corvette': lambda: 80 <= self.length <= 250 and
            4 <= self.crew_size <= 10 and self.armed
            and self.alignment == 'Ally',
            'Frigate': lambda: 300 <= self.length <= 600 and
            10 <= self.crew_size <= 15 and self.armed and
            not self.alignment == 'Ally',
            'Cruiser': lambda: 500 <= self.length <= 1000 and
            15 <= self.crew_size <= 30 and
            self.armed and self.alignment == 'Ally',
            'Destroyer': lambda: 800 <= self.length <= 2000 and
            50 <= self.crew_size <= 80 and self.armed and
            not self.alignment == 'Ally',
            'Carrier': lambda: 1000 <= self.length <= 4000 and
            120 <= self.crew_size <= 250 and
            not self.armed and self.alignment == 'Ally',
            'Dreadnought': lambda: 5000 <= self.length <= 20000 and
            300 <= self.crew_size <= 500 and self.armed and
            self.alignment == 'Ally'
        }

        if self.class_ship not in ship_classes:
            raise ValueError("")

        if not ship_classes[self.class_ship]():
            raise ValueError("")

        return self


def check_ship(ship):
    try:
        BaseShip.model_validate_json(ship)
        return True
    except ValueError as e:
        return False


if __name__ == '__main__':
    coordinates = parse_coordinate()
    try:
        with grpc.insecure_channel('localhost:50051') as chanel:
            for message in get_ships(chanel, coordinates):
                if check_ship(message):
                    print(message)
    except Exception as e:
        print(f"Error: {e}")
