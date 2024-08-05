"""Demo Composition and Aggregation

Classes:
    Vehicle: device with wheels that can move
    Car: vehicle with engine and can be driven
    LicensePlate: the license required for driving the vehicle on the road
"""

from datetime import datetime, timedelta
import logging
logging.basicConfig(level=logging.DEBUG, format="#%(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)


class Vehicle:
    """device with wheels and can move"""
    @property
    def wheels(self) -> int:
        """int: number of wheels"""
        return self._wheels

    def __init__(self, wheels: int, heading: int = 0):
        """Construct a vehicle

        Args:
            wheels: number of wheels
            heading: where the vehicle is headed 0 degree is north, 90 is east
                -90 is west, 180 is south
        """
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.debug(".__init__()")
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
        import math
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

    def __init__(self, plate_number: str, expiry_date: str | None = None):
        """Construct License Plate object

        Args:
            plate_number: the license plate number
            expiry_date: one year from now if omitted
        """
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.debug(".__init__()")
        self._plate_number = plate_number
        self._valid = True
        self.renew(expiry_date)

    def isvalid(self) -> bool:
        """check if the license is valid, not-expired"""
        self.logger.debug(" -LicensePlate.isvalid()")
        return self._valid and datetime.now() < self._expiry_date

    def renew(self, expiry_date: str | None = None):
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
        self.logger.debug(" -LicensePlate.cancel(), "
                          f"cancelling {self._plate_number}.")
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
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.debug(".__init__()")
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
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.debug(".__init__()")
        super().__init__(4, 90)
        self.engine = Engine(type_, cylinders, displacement=displacement)
        self.license_plate = None
        self.logger.debug(f"Initialized a car with {self.wheels} wheels, "
                          f"and a {self.engine}")


def main():
    car_1 = Car("Audi", "A5", displacement=2.0)
    license_plate_1 = LicensePlate("ABC1234", "2099-12-31")
    car_1.license_plate = license_plate_1
    print(f"# {car_1.engine}, {car_1.license_plate.isvalid()=}")

    license_plate_1.cancel()
    print(f"# {car_1.license_plate._expiry_date.isoformat()=}, "
          f"{car_1.license_plate.isvalid()=}")


if __name__ == "__main__":
    main()

# DEBUG - Car(m9_2_2.py:143) - .__init__()
# DEBUG - Car(m9_2_2.py:31) - .__init__()
# DEBUG - Engine(m9_2_2.py:125) - .__init__()
# DEBUG - Car(m9_2_2.py:147) - Initialized a car with 4 wheels, and a a 2.0 liter 4 cylinder gasoline engine.
# DEBUG - LicensePlate(m9_2_2.py:79) - .__init__()
# DEBUG - LicensePlate(m9_2_2.py:87) -  -LicensePlate.isvalid()
# a 2.0 liter 4 cylinder gasoline engine., car_1.license_plate.isvalid()=True
# DEBUG - LicensePlate(m9_2_2.py:105) -  -LicensePlate.cancel(), cancelling ABC1234.
# DEBUG - LicensePlate(m9_2_2.py:87) -  -LicensePlate.isvalid()
# car_1.license_plate.isvalid()=False
