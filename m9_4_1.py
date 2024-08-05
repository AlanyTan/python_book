"""Demo Singleton using Car, Vehicle, LicensePlate and DMV

Classes:
    Vehicle: device with wheels that can move
    Car: vehicle with engine and can be driven
    LicensePlate: the license required for driving the vehicle on the road
    DMV: Department of Motor Vehicle - centralized 
"""
from m9_2_2 import Vehicle, LicensePlate, Engine
import logging
logging.basicConfig(level=logging.DEBUG, format="#%(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)


class DMV:
    """Department Motor Vehicle, a singleton for issuing license Plate"""
    _instance = None

    _allowed_license_chars = "01234567890ABCDEFGHJKLNPQRSTVWXYZ"

    def __new__(cls, *args, **kwargs):
        """ensure only one instance of DMV will ever exist"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, init_plate_number: str | None = None):
        """Construct DMV with list of issued plate numbers

        Checks if _initialized already exist, if so return without 
        doing anything, otherwise, initialize the issued_plate_numbers.
        """
        if hasattr(self, '_initialized'):
            self.logger.debug(f"DMV singleton was already initialized.")
            return
        self.logger = logging.getLogger(self.__class__.__name__)
        self.issued_plate_numbers = []
        self.issued_plate_numbers.append(init_plate_number if
                                         init_plate_number else '000000')
        self.logger.debug(f"DMV initialized with {self.issued_plate_numbers}.")
        self._initialized = True

    def issue(self):
        """issue a new plate number based on increment from last plate number"""
        def next_allowed_char(current_char):
            cur_idx = self._allowed_license_chars.index(current_char)
            if cur_idx + 1 >= len(self._allowed_license_chars):
                next_idx = 0
            else:
                next_idx = cur_idx + 1
            next_char = self._allowed_license_chars[next_idx]
            return next_char
        last_issued_plate_numbers = sorted(self.issued_plate_numbers)[-1]
        next_plate_number = last_issued_plate_numbers
        for i in reversed(range(len(last_issued_plate_numbers))):
            next_plate_number = (next_plate_number[0:i] +
                                 next_allowed_char(last_issued_plate_numbers[i]) +
                                 next_plate_number[i+1:])
            if next_plate_number[i] != '0':
                break
        self.issued_plate_numbers.append(next_plate_number)
        self.logger.debug(f"issuing new plate: {next_plate_number}")
        return next_plate_number


class Car(Vehicle):
    """Inherit Vehicle, composition Engine, Aggregation LisensePlate"""

    def __init__(self, make: str, model: str, type_: str | None = None,
                 cylinders: int = 4, displacement: float = 0):
        """Construct a car by defining an Engine, and a license placeholder"""
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.debug(".__init__()")
        super().__init__(4, 90)
        self.engine = Engine(type_=type_, cylinders=cylinders,
                             displacement=displacement)
        self.license_plate = None
        self.logger.debug(f"Initialized a car with {self.wheels} wheels, "
                          f"and a {self.engine}")

    def register(self):
        """register the vehicle to obtain a license plate"""
        dmv = DMV()
        self.license_plate = LicensePlate(dmv.issue())


def main():
    dmv1 = DMV("012ZZ9")
    dmv2 = DMV("210ALZ")
    print(f"# dmv1 and dmv2 are the same: {dmv1 is dmv2}, "
          f"DMV's current list of plate numbers{dmv2.issued_plate_numbers}")
    car_1 = Car("Audi", "A5", displacement=2.0)
    print(f"# created car with {car_1.engine}, current license plate is "
          f"{car_1.license_plate}")
    car_1.register()
    print(f"# car_1 registered as:{car_1.license_plate._plate_number}, "
          f"{car_1.license_plate.isvalid()=}")

    car_2 = Car("BMW", "i4", type_='Electric', cylinders=0)
    print(f"# created car with {car_2.engine}, current license plate is "
          f"{car_2.license_plate}")
    car_2.register()
    print(f"# car_2 registered as:{car_2.license_plate._plate_number}, "
          f"{car_2.license_plate.isvalid()=}")


if __name__ == "__main__":
    main()

# DEBUG - DMV(m9_4_1.py:41) - DMV initialized with ['012ZZ9'].
# DEBUG - DMV(m9_4_1.py:35) - DMV singleton was already initialized.
# dmv1 and dmv2 are the same: True, DMV's current list of plate numbers['012ZZ9']
# DEBUG - Car(m9_4_1.py:74) - .__init__()
# DEBUG - Car(m9_2_2.py:32) - .__init__()
# DEBUG - Engine(m9_2_2.py:125) - .__init__()
# DEBUG - Car(m9_4_1.py:79) - Initialized a car with 4 wheels, and a a 2.0 liter 4 cylinder None engine.
# created car with a 2.0 liter 4 cylinder None engine., current license plate is None
# DEBUG - DMV(m9_4_1.py:35) - DMV singleton was already initialized.
# DEBUG - DMV(m9_4_1.py:63) - issuing new plate: 013000
# DEBUG - LicensePlate(m9_2_2.py:80) - .__init__()
# DEBUG - LicensePlate(m9_2_2.py:87) -  -LicensePlate.isvalid()
# car_1 registered as:013000, car_1.license_plate.isvalid()=True
# DEBUG - Car(m9_4_1.py:74) - .__init__()
# DEBUG - Car(m9_2_2.py:32) - .__init__()
# DEBUG - Engine(m9_2_2.py:125) - .__init__()
# DEBUG - Car(m9_4_1.py:79) - Initialized a car with 4 wheels, and a a 0 liter 0 cylinder Electric engine.
# created car with a 0 liter 0 cylinder Electric engine., current license plate is None
# DEBUG - DMV(m9_4_1.py:35) - DMV singleton was already initialized.
# DEBUG - DMV(m9_4_1.py:63) - issuing new plate: 013001
# DEBUG - LicensePlate(m9_2_2.py:80) - .__init__()
# DEBUG - LicensePlate(m9_2_2.py:87) -  -LicensePlate.isvalid()
# car_2 registered as:013001, car_2.license_plate.isvalid()=True
