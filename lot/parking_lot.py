""" Handles the core parking lot functionality """

from typing import Any, List

from . import car


class ParkingLot():
    """ Packs the core parking lot functionality """

    def __init__(self, size: int) -> None:
        """ Initializes the parking lot """
        self.parking_lot = [None] * size
        self.size = size
        self.age_slot_map = {}
        self.car_ids = set()

    def allot(self, car_id: str, age: int) -> Any:
        """ Allots the slot to the car """
        allot_statement = ''
        slot = self.get_lowest_parking_slot()

        if slot == -1:
            allot_statement = 'The parking slot is currently full!'
        else:
            if self.car_id_exists(car_id):
                allot_statement = 'Car already exists!'
            else:
                new_car = car.Car(car_id, age)
                new_car.slot = slot
                self.car_ids.add(car_id)
                self.parking_lot[slot] = new_car
                self.map_age_and_slot(age, slot)
                allot_statement = f'Car with vehicle registration number '\
                                  f'"{car_id}" has been parked at slot number '\
                                  f'{slot + 1}'

        return allot_statement

    def unallot(self, slot: int) -> str:
        """ Unallots the slot for the given car_id """
        unallot_statement = ''

        if slot > self.size - 1:
            unallot_statement = 'Invalid slot!'
        else:
            car_object = self.parking_lot[slot - 1]  # Get the car object
            car_object.slot = None  # Remove slot ID from the car object
            age = car_object.driver_age  # Get the driver age
            self.age_slot_map[age].remove(slot - 1)  # Remove slot from the age_slot_map
            self.parking_lot[slot - 1] = None  # Remove the car object from parking_lot
            self.car_ids.discard(car_object.car_id)  # Remove the car_id from the car_ids set
            unallot_statement = f'Slot number {slot} vacated, the car with vehicle '\
                                f'registration number "{car_object.car_id}" left the space, '\
                                f'the driver of the car was of age {car_object.driver_age}'

        return unallot_statement

    def car_id_exists(self, car_id: str) -> bool:
        """ Checks if car_id exists in the parking lot """
        return car_id in self.car_ids

    def get_lowest_parking_slot(self) -> int:
        """ Returns the nearest available parking slot """
        return self.parking_lot.index(None) if None in self.parking_lot else -1

    def get_slot_id(self, car_id: str) -> int:
        """ Returns slot_id for the given car_id """
        string_parking_lot = list(map(str, self.parking_lot))

        return string_parking_lot.index(car_id) if car_id in string_parking_lot else -1

    def get_slots_by_age(self, age: int) -> List:
        """ Returns slot_ids occupied by drivers of certain age """
        return self.age_slot_map.get(age, [])

    def get_available_slots_count(self) -> str:
        """ Returns unoccupied slots' count """
        count = self.parking_lot.count(None)
        return f'Available slots: {count}/{self.size}'

    def get_car_ids_by_age(self, age: int) -> List:
        """ Returns registration numbers of all cars by driver age """
        slots = self.get_slots_by_age(age)
        car_ids = []

        for slot in slots:
            car_object = self.parking_lot[slot]
            car_ids.append(car_object.car_id)

        return car_ids

    def map_age_and_slot(self, age: int, slot: int) -> None:
        """ Maps age to slot """
        if self.age_slot_map.get(age) is None:
            self.age_slot_map[age] = [slot]
        else:
            self.age_slot_map[age].append(slot)
