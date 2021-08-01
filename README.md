# Parking Lot

## Contents
- [Getting Started](#getting-started)
- [Class Description](#class-description)
  - [ParkingLot](#1-parkinglot)
  - [Car](#2-car)
  - [InputParser](#3-inputparser)

## Getting Started
Start by cloning the repository using: `git clone https://github.com/IamRaviTejaG/fampay-assignment.git` followed by `cd parking_lot`.

To run the program, type:
```bash
python3 -m main <input_file_path> <output_file_path>
```

**NOTE**: Please replace `<input_file_path>` with the complete path to `input.txt` and replace `<output_file_path>` with the complete path to `output.txt`.
<br />

## Class Description
<br />

### 1. `ParkingLot`
This class contains all the core functionality.

*Methods:*
- `allot`: Allots the slot to the car.
- `unallot`: Unallots the slot for the given car_id.
- `car_id_exists`: Checks if car_id exists in the parking lot.
- `get_lowest_parking_slot`: Returns the nearest available parking slot.
- `get_slot_id`: Returns slot_id for the given car_id.
- `get_slots_by_age`: Returns slot_ids occupied by drivers of certain age.
- `get_available_slots_count`: Returns unoccupied slots' count.
- `get_car_ids_by_age`: Returns registration numbers of all cars by driver age.
- `map_age_and_slot`: Maps age to slot.

### 2. `Car`
This class contains the Car object with all its properties.

*Methods:*
- `__str__`: Returns the car_id as the string representation of the object, making it easy to search by car_id inside Car objects.

### 3. `InputParser`
This class contains methods to parse the input and write the output to a file.

*Methods:*
- `run`: Runs the input file parser and invokes the `ParkingLot` functionality, and writes the output to a file.

