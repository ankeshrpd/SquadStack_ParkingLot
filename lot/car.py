""" Contains the car class and its relevant functionality """

class Car:
    """ Contains all the attributes for a Car """

    def __init__(self, car_id: str, driver_age: int):
        """ Initializes a new car object """
        self.car_id = car_id
        self.driver_age = driver_age
        self.slot = None

    def __str__(self) -> str:
        """ Custom __str__ function to make it easy for
        it to be searchable """
        return self.car_id
