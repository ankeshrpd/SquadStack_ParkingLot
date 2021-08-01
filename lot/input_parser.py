""" Handles input file parsing functionality """

from lot import parking_lot


class InputParser():
    """ Handles the input parsing and output writing functionality """
    @staticmethod
    def run(input_file, output_file):
        """ Takes in the input & output file paths, parses the input file
        and writes the output to the output file """
        with open(input_file) as infile:
            input_data = infile.read().splitlines()
            with open(output_file,"w") as outfile:
                for line in input_data:
                    if line.startswith('Create'):
                        num = int(line.split()[1])
                        lot = parking_lot.ParkingLot(num)
                        outfile.writelines(f'Created parking of {num} slots\n')

                    elif line.startswith('Park'):
                        car_id = line.split()[1]
                        age = line.split()[3]
                        slot = lot.allot(car_id, age)
                        outfile.writelines(f'{slot}\n')

                    elif line.startswith('Leave'):
                        slot_id = int(line.split()[1])
                        slot = lot.unallot(slot_id)
                        outfile.writelines(f'{slot}\n')

                    elif line.startswith('Slot_number_for_car_with_number'):
                        car_id = line.split()[1]
                        slot = lot.get_slot_id(car_id)
                        if slot == -1:
                            outfile.write(
                                f'Car with vehicle registration number '
                                f'"{car_id}" isn\'t parked in the parking lot\n'
                            )
                        else:
                            outfile.write(f'{slot + 1}\n')

                    elif line.startswith('Slot_numbers_for_driver_of_age'):
                        slots = lot.get_slots_by_age(line.split()[1])
                        slots = map(lambda x: x + 1, slots)
                        slots = map(str, slots)
                        slot_numbers = ','.join(slots)
                        outfile.write(f'{slot_numbers}\n')

                    elif line.startswith('Vehicle_registration_number_for_driver_of_age'):
                        age = line.split()[1]
                        car_ids = lot.get_car_ids_by_age(age)
                        car_ids = ','.join(car_ids)
                        outfile.write(f'{car_ids}\n')

                    else:
                        print('Invalid input!')
