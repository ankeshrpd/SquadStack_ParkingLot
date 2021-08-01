# Handles the core parking lot functionality

from typing import Any, List


class ParkingLot():
    def __init__(self, size: int) -> str:
        """ Initializes the parking lot """
        self.parking_lot = [None] * size
        self.size = size
        self.age_slot_map = {}
        self.carID_age_map = {}
        self.car_ids = set()

    def allot(self, car_id: str, age: int) -> Any:
        """ Allots the slot to the car """
        slot = self.get_lowest_parking()

        if slot == -1:
            return 'The parking slot is currently full!'
        else:
            if self.car_id_exists(car_id):
                return 'Car already exists!'
            else:
                self.car_ids.add(car_id)
                self.parking_lot[slot] = car_id
                self.map_age_and_slot(age, slot)
                self.map_age_and_carID(age, car_id)
                return f'Car with vehicle registration number "{car_id}" has been parked at slot number {slot+1}'

    def deallot(self, slot: int):
        """ Deallots the slot for the given car_id """
        if slot > self.size - 1:
            return 'Invalid slot!'
        else:
            car_id = self.parking_lot[slot-1]
            self.parking_lot[slot-1] = None
            self.car_ids.discard(car_id)
            agae = self.get_age_by_car_id(car_id)[0]
            return f'Slot number {slot} vacated, the car with vehicle registration number "{car_id}" left the space, the driver of the car was of age {agae}'

    def car_id_exists(self, car_id: str) -> bool:
        """ Checks if car_id exists in the parking lot """
        return car_id in self.car_ids

    def get_lowest_parking(self):
        """ Returns the nearest available parking slot """
        if None in self.parking_lot:
            return self.parking_lot.index(None)
        else:
            return -1

    def map_age_and_slot(self, age: int, slot: int) -> None:
        """ Maps age to slot """
        if self.age_slot_map.get(age) is None:
            self.age_slot_map[age] = [slot]
        else:
            self.age_slot_map[age].append(slot)

    def map_age_and_carID(self, age: int, car_id: int) -> None:
        """ Maps age to Car ID """
        # if self.carID_age_map.get(car_id) is None:
        self.carID_age_map[car_id] = [age]
        # else:
        #     self.carID_age_map[car_id].append(age)

    def get_slot_id(self, car_id: str) -> int:
        """ Returns slot_id for the given car_id """
        if car_id in self.parking_lot:
            return self.parking_lot.index(car_id)
        else:
            return -1

    def get_slots_by_age(self, age: int) -> List:
        """ Returns car_ids based on  available parking slot """
        return self.age_slot_map.get(age, [])

    def get_age_by_car_id(self, car_id: int) -> List:
        """ Returns car_ids based on  available parking slot """
        return self.carID_age_map.get(car_id)

    def get_available_slots_count(self) -> str:
        """ Returns unoccupied slots' count """
        count = self.parking_lot.count(None)
        return f'Available slots: {count}/{self.size}'
