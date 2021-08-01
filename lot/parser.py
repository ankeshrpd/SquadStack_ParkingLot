# Handles input parsing
from lot import parking


class InputParser():
    
    @staticmethod
    def run(file_name):
        with open(file_name) as f:
            input_data = f.read().splitlines()


            file1 = open("output.txt","w")    
            for line in input_data:
                if line.startswith('Create'):                    
                    num = int((line.split(' ')[1]))
                    lot = parking.ParkingLot(num)
                elif line.startswith('Park'):
                    slot = lot.allot(line.split(' ')[1],line.split(' ')[3])
                    file1.writelines(slot+ '\n')
                elif line.startswith('Leave'):
                    slot = lot.deallot(int(line.split(' ')[1]))
                    file1.writelines(slot+ '\n')
                elif line.startswith('Slot_number_for_car_with_number'):
                    slot = lot.get_slot_id((line.split(' ')[1])) 
                    file1.write(f"{slot+1}\n")
                elif line.startswith('Slot_numbers_for_driver_of_age'):
                    slot = lot.get_slots_by_age((line.split(' ')[1]))
                    slot = map(lambda x: x+1, slot)
                    slot = map(str, slot)
                    slot_numbers = ','.join(slot)
                    file1.write(slot_numbers+ '\n')
            file1.close()