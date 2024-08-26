"""Demo Composition and Aggregation

Classes:
    Vehicle: device with wheels that can move
    Car: vehicle with engine and can be driven
    LicensePlate: the license required for driving the vehicle on the road
"""

from datetime import datetime, timedelta
import math
from m8_2_2 import get_logger, logging_context as log_to


class Vehicle:
    """device with wheels and can move"""

    @property
    def wheels(self) -> int:
        """int: number of wheels"""
        return self._wheels

    def __init__(self, wheels: int, heading: int = 0) -> None:
        """Construct a vehicle

        Args:
            wheels: number of wheels
            heading: where the vehicle is headed 0 degree is north, 90 is east
                -90 is west, 180 is south
        """
        self.logger = get_logger(self.__class__.__name__, stream='DEBUG')
        self.logger.debug("constructing a Vehicle")
        self._wheels = wheels
        self._heading = heading
        self._pos_x = 0
        self._pos_y = 0

    def move(self, distance: float = 0) -> tuple:
        """move forward/backward according to current heading

        Args:
            distance: m, can be negative indicating move backwards
                      default is 0, will return current location

        Returns:
            tuple: coordinates of new location after the move
        """
        heading_radian = math.radians(self._heading)
        self._pos_x += math.cos(heading_radian) * distance
        self._pos_y += math.sin(heading_radian) * distance
        return (self._pos_x, self._pos_y)

    def steer(self, degrees: float = 0) -> float:
        """steer the vehicle towards new heading

        Args:
            degrees: how many degrees to turn, positive turns counter-clockwise
                     default 0, will return current heading

        Returns:
            float: the new heading direction between -180 and 179.99999
                   0 means facing right (east) 
        """
        self._heading = (self._heading + degrees) % 360 - 180
        return self._heading


class LicensePlate:
    """License Plate, has a unique plate number and an expiry date"""

    @property
    def plate_number(self) -> str:
        """readonly property  plate number"""
        return self._plate_number

    @property
    def expiry_date(self) -> datetime:
        """readonly property expiry date """
        return self._expiry_date

    def __init__(self, plate_number: str,
                 expiry_date: str | None = None) -> None:
        """Construct License Plate object

        Args:
            plate_number: the license plate number
            expiry_date: one year from now if omitted
        """
        self.logger = get_logger(self.__class__.__name__, stream='DEBUG')
        self.logger.debug("construct a License Plate")
        self._plate_number = plate_number
        self._valid = True
        self.renew(expiry_date)

    def isvalid(self) -> bool:
        """check if the license is valid, not-expired"""
        self.logger.debug(" checking the validity of %s", self._plate_number)
        return self._valid and datetime.now() < self._expiry_date

    def renew(self, expiry_date: str | None = None) -> None:
        """ renew a license plate

        Args:
            expiry_date: new expiry_date, if omitted, will be 1 year from today
        """
        if expiry_date is None:
            valid_for = timedelta(days=365)
            self._expiry_date = datetime.now() + valid_for
        else:
            self._expiry_date = datetime.fromisoformat(expiry_date)
        self._valid = True

    def cancel(self):
        """cancel a license plate immediately """
        self.logger.debug("cancelling %r", self._plate_number)
        self._valid = False


class Engine:
    """Engine of a Car"""

    def __init__(self, type_: str | None = None, cylinders: int = 4,
                 displacement: float = 0, hp: float = 0, torq: float = 0):
        """Construct an Engine

        Args:
            type_: one of 'gasoline', 'diesel', 'hybrid', 'electric'
            cylinders: if fossile fuel engien, number of cylinders
            displacement: total volume of cylinders in L
            hp: peak horsepower
            torq: peak torque n/m
        """
        self.logger = get_logger(self.__class__.__name__, stream='DEBUG')
        self.logger.debug("construct an Engine")
        self._type = type_
        self._cylinders = cylinders
        self._displacement = displacement
        self._hp = hp
        self._torq = torq

    def __repr__(self) -> str:
        return (f"a {self._displacement} liter {self._cylinders} cylinder "
                f"{self._type} engine.")


class Car(Vehicle):
    """Inherit Vehicle, composition Engine, Aggregation LisensePlate"""

    def __init__(self, make: str, model: str,
                 type_: str | None = None, cylinders: int = 4,
                 displacement: float = 0):
        """Construct a car by defining an Engine, and a license placeholder"""
        super().__init__(4, 90)
        self.logger.debug("construct a Car")
        self.make = make
        self.model = model
        self.engine = Engine(type_, cylinders, displacement=displacement)
        self.license_plate: LicensePlate | None = None
        self.logger.debug("Initialized a car with %s wheels, and a %s ",
                          self.wheels, self.engine)


def main() -> None:
    """demo composition and aggregation"""
    car_1 = Car("Audi", "A5", displacement=2.0)
    license_plate_1 = LicensePlate("ABC1234", "2099-12-31")
    car_1.license_plate = license_plate_1
    print(f"# {car_1.engine}, {car_1.license_plate.isvalid()=}")

    license_plate_1.cancel()
    print(f"# {car_1.license_plate.expiry_date.isoformat()=}, "
          f"{car_1.license_plate.isvalid()=}")


if __name__ == "__main__":
    with log_to("main", stream=False) as logger:
        main()

#    DEBUG - m9_2_2.py:31 Car.__init__() - constructing a Vehicle
#    DEBUG - m9_2_2.py:153 Car.__init__() - construct a Car
#    DEBUG - m9_2_2.py:133 Engine.__init__() - construct an Engine
#    DEBUG - m9_2_2.py:158 Car.__init__() - Initialized a car with 4 wheels, and a a 2.0 liter 4 cylinder None engine.
#    DEBUG - m9_2_2.py:89 LicensePlate.__init__() - construct a License Plate
#    DEBUG - m9_2_2.py:96 LicensePlate.isvalid() -  checking the validity of ABC1234
# a 2.0 liter 4 cylinder None engine., car_1.license_plate.isvalid()=True
#    DEBUG - m9_2_2.py:114 LicensePlate.cancel() - cancelling 'ABC1234'
#    DEBUG - m9_2_2.py:96 LicensePlate.isvalid() -  checking the validity of ABC1234
# car_1.license_plate.expiry_date.isoformat()='2099-12-31T00:00:00', car_1.license_plate.isvalid()=False
