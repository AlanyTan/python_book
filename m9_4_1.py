"""Demo Singleton using Car, Vehicle, LicensePlate and DMV

Classes:
    DMV: the singleton class for regulator of Motor Vehicle
    Car: enhanced with .register() method
    Vehicle: needed because Car inherited from Vehicle
    Engine: needed because Car has a composition attribute of engine 
"""
from logging import Logger
from m8_2_2 import get_logger, logging_context as log_to
from m9_2_2 import Vehicle, LicensePlate, Engine


class DMV:
    """Department Motor Vehicle, a singleton for issuing license Plate"""
    _instance = None

    _logger: Logger | None = None

    _allowed_license_chars = "0123456789ABCDEFGHJKLNPQRSTVWXYZ"

    @property
    def logger(self) -> Logger:
        """logger: regular property return a logger named after the class"""
        if self.__class__._logger is None:
            self.__class__._logger = get_logger(self.__class__.__name__,
                                                stream="DEBUG")
        return self.__class__._logger

    def __new__(cls, *args, **kwargs):
        """ensure only one instance of DMV will ever exist"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, init_plate_number: str | None = None) -> None:
        """Construct DMV with list of issued plate numbers

        Checks if _initialized already exist, if so return without 
        doing anything, otherwise, initialize the issued_plate_numbers.
        """
        if hasattr(self, '_initialized'):
            self.logger.debug("DMV singleton was already initialized.")
            return
        if init_plate_number and any([c for c in init_plate_number if c not in
                                      self._allowed_license_chars]):
            self.logger.error("%s contain invalid characters for a plate",
                              init_plate_number)
            raise ValueError(f"{init_plate_number} contain invalid characters")
        self.issued_plate_numbers = [init_plate_number if init_plate_number
                                     else self._allowed_license_chars[0] * 6]
        self.logger.debug(f"DMV initialized with {self.issued_plate_numbers}.")
        self._initialized = True

    def issue(self) -> str:
        """issue a new plate number by incrementing previous one"""
        last_issued_plate_number = sorted(self.issued_plate_numbers)[-1]
        incr = 1
        license_plate_char_list = []
        for char in reversed(last_issued_plate_number):
            if incr and char == self._allowed_license_chars[-1]:
                char = self._allowed_license_chars[0]
            elif incr:
                char = self._allowed_license_chars[
                    self._allowed_license_chars.index(char) + 1]
                incr = 0
            license_plate_char_list.append(char)

        next_plate_number = "".join(reversed(license_plate_char_list))
        self.issued_plate_numbers.append(next_plate_number)
        self.logger.debug(f"issuing new plate: {next_plate_number}")
        return next_plate_number


class Car(Vehicle):
    """Inherit Vehicle, added register() method"""

    def __init__(self, make: str, model: str, type_: str | None = None,
                 cylinders: int = 4, displacement: float = 0):
        """Construct a car by defining an Engine, and a license placeholder"""
        super().__init__(4, 90)
        self.logger.debug(".__init__()")
        self.make = make
        self.model = model
        self.engine = Engine(type_=type_, cylinders=cylinders,
                             displacement=displacement)
        self.license_plate = None
        self.logger.debug("Initialized a car with %s wheels, and a %s ",
                          self.wheels, self.engine)

    def register(self) -> None:
        """register the vehicle to obtain a license plate"""
        dmv = DMV()
        self.license_plate = LicensePlate(dmv.issue())


def main() -> None:
    """demo singleton design pattern"""
    try:
        dmv1 = DMV("012ZZO")
    except ValueError as e:
        logger.error("Cannot initialize DMV, received %r", e)

    dmv1 = DMV("012ZZ9")
    dmv2 = DMV("210ALO")
    print(f"# dmv1 and dmv2 are the same: {dmv1 is dmv2}, "
          f"DMV's current list of plate numbers{dmv2.issued_plate_numbers}")
    car_1 = Car("Audi", "A5", displacement=2.0)
    print(f"# created car with {car_1.engine}, current license plate is "
          f"{car_1.license_plate}")
    car_1.register()
    print(f"# car_1 registered as:{car_1.license_plate.plate_number}, "
          f"{car_1.license_plate.isvalid()=}")

    car_2 = Car("BMW", "i4", type_='Electric', cylinders=0)
    print(f"# created car with {car_2.engine}, current license plate is "
          f"{car_2.license_plate}")
    car_2.register()
    print(f"# car_2 registered as:{car_2.license_plate.plate_number}, "
          f"{car_2.license_plate.isvalid()=}")


if __name__ == "__main__":
    with log_to("main", stream="DEBUG") as logger:
        main()

#    ERROR - m9_4_1.py:47 DMV.__init__() - 012ZZO contain invalid characters for a plate
#    ERROR - m9_4_1.py:102 main.main() - Cannot initialize DMV, received ValueError('012ZZO contain invalid characters')
#    DEBUG - m9_4_1.py:52 DMV.__init__() - DMV initialized with ['012ZZ9'].
#    DEBUG - m9_4_1.py:43 DMV.__init__() - DMV singleton was already initialized.
# dmv1 and dmv2 are the same: True, DMV's current list of plate numbers['012ZZ9']
#    DEBUG - m9_2_2.py:31 Car.__init__() - constructing a Vehicle
#    DEBUG - m9_4_1.py:82 Car.__init__() - .__init__()
#    DEBUG - m9_2_2.py:133 Engine.__init__() - construct an Engine
#    DEBUG - m9_4_1.py:88 Car.__init__() - Initialized a car with 4 wheels, and a a 2.0 liter 4 cylinder None engine.
# created car with a 2.0 liter 4 cylinder None engine., current license plate is None
#    DEBUG - m9_4_1.py:43 DMV.__init__() - DMV singleton was already initialized.
#    DEBUG - m9_4_1.py:71 DMV.issue() - issuing new plate: 012ZZA
#    DEBUG - m9_2_2.py:89 LicensePlate.__init__() - construct a License Plate
#    DEBUG - m9_2_2.py:96 LicensePlate.isvalid() -  checking the validity of 012ZZA
# car_1 registered as:012ZZA, car_1.license_plate.isvalid()=True
#    DEBUG - m9_2_2.py:31 Car.__init__() - constructing a Vehicle
#    DEBUG - m9_4_1.py:82 Car.__init__() - .__init__()
#    DEBUG - m9_2_2.py:133 Engine.__init__() - construct an Engine
#    DEBUG - m9_4_1.py:88 Car.__init__() - Initialized a car with 4 wheels, and a a 0 liter 0 cylinder Electric engine.
# created car with a 0 liter 0 cylinder Electric engine., current license plate is None
#    DEBUG - m9_4_1.py:43 DMV.__init__() - DMV singleton was already initialized.
#    DEBUG - m9_4_1.py:71 DMV.issue() - issuing new plate: 012ZZB
#    DEBUG - m9_2_2.py:89 LicensePlate.__init__() - construct a License Plate
#    DEBUG - m9_2_2.py:96 LicensePlate.isvalid() -  checking the validity of 012ZZB
# car_2 registered as:012ZZB, car_2.license_plate.isvalid()=True
#     INFO - m8_2_2.py:67 main.logging_context() - shutting down the logging facility...
