"""Demo Observer pattern"""
from abc import ABC, abstractmethod
import logging
logging.basicConfig(level=logging.DEBUG, format="#%(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)
from m9_4_1 import DMV, Vehicle, LicensePlate, Engine


class Observer(ABC):
    """the abstract class for observer of something worth monitoring"""
    @abstractmethod
    def update_status(self, status):
        pass


class Notifier(ABC):
    """the abstract base class for the notifying observers of status changes """
    @property
    @abstractmethod
    def status(self):
        pass

    def __init__(self):
        """setup internal list of observers."""
        self._observers = []

    def attach(self, observer: Observer):
        """add an observer as a registered observer of this notifier"""
        self.logger.debug(f"attaching {observer} to {self}")
        self._observers.append(observer)

    def detach(self, observer: Observer):
        """del an observer from registered observer list"""
        self.logger.debug(f"detaching {observer} to {self}")
        self._observers.remove(observer)

    def notify(self):
        """the notification method, call all the registered observer's update"""
        for observer in self._observers:
            self.logger.debug(
                f"notifying {observer} that status changed to  {self.status}")
            observer.update_status(self.status)


class SmartLicensePlate(LicensePlate, Notifier):
    """adaptor for LicensePlate to inherit from Notifier"""

    def __init__(self, *args):
        """construct SmartLicensePlate by calling super(). then Notifer init"""
        super().__init__(*args)
        Notifier.__init__(self)

    @property
    def status(self):
        """override abstract property from Notifier as an alias to .isvalid()"""
        return self.isvalid()

    def cancel(self):
        """add notification after the LicensePlate.cancel()"""
        super().cancel()
        self.notify()

    def __repr__(self):
        return f"{self.__class__.__name__}('{self._plate_number}')"


class Car(Vehicle, Observer):
    """Inherit Vehicle, composition Engine, Aggregation LisensePlate"""

    def __init__(self, make: str, model: str, type_: str | None = None,
                 cylinders: int = 4, displacement: float = 0):
        """Construct a car by defining an Engine, and a license placeholder"""
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.debug(".__init__()")
        super().__init__(4, 90)
        self.make = make
        self.model = model
        self.engine = Engine(type_=type_, cylinders=cylinders,
                             displacement=displacement)
        self.license_plate = None
        self.valid_on_road = False
        self.logger.debug(f"Initialized a car with {self.wheels} wheels, "
                          f"and a {self.engine}")

    def register(self):
        """register the vehicle to obtain a license plate"""
        dmv = DMV()
        self.license_plate = SmartLicensePlate(dmv.issue())
        self.license_plate.attach(self)
        self.valid_on_road = True

    def update_status(self, status):
        """override abstract method from Observer, allow receiving info"""
        self.logger.debug(f"Observer method update_status called.")
        self.valid_on_road = status

    def __repr__(self):
        return (f"{self.__class__.__name__}('{self.make}', "
                f"'{self.model}', type_='{self.engine._type})")


class OwnershipCard(Observer):
    """The ownership card of the car registration"""

    def __init__(self, license_plate: SmartLicensePlate):
        """initialize ownership card aggregate with license_plate"""
        self.logger = logging.getLogger(self.__class__.__name__)
        self.is_valid = True
        self.license_plate = license_plate
        license_plate.attach(self)

    def update_status(self, status):
        """override abstract method from Observer, allow receiving info"""
        self.logger.debug(f"Observer method update_status called.")
        self.is_valid = status

    def __repr__(self):
        return (f"{self.__class__.__name__}(SmartLicensePlate("
                f"{self.license_plate._plate_number})")


def main():
    car_2 = Car("BMW", "i4", type_='Electric', cylinders=0)
    logger.info(f"before register: "
                f"{car_2.license_plate=}, {car_2.valid_on_road=}")
    car_2.register()
    logger.info(f"after registered as:{car_2.license_plate._plate_number}, "
                f"{car_2.valid_on_road=}, {car_2.license_plate.isvalid()=}")
    license_plate_2 = car_2.license_plate

    ownershipcard_2 = OwnershipCard(license_plate_2)
    logger.info(f"before canceling: {car_2.valid_on_road=}, "
                f"{ownershipcard_2.is_valid=}")

    license_plate_2.cancel()
    logger.info(f"car after cancellation:{car_2.license_plate._plate_number=}, "
                f"{car_2.license_plate.isvalid()=}")
    logger.info(f"observers after cancellation:"
                f"{car_2.valid_on_road=}, {ownershipcard_2.is_valid=}")


if __name__ == "__main__":
    main()

# DEBUG - Car(m9_4_5.py:75) - .__init__()
# DEBUG - Car(m9_2_2.py:32) - .__init__()
# DEBUG - Engine(m9_2_2.py:125) - .__init__()
# DEBUG - Car(m9_4_5.py:83) - Initialized a car with 4 wheels, and a a 0 liter 0 cylinder Electric engine.
# INFO - __main__(m9_4_5.py:125) - before register: car_2.license_plate=None, car_2.valid_on_road=False
# DEBUG - DMV(m9_4_1.py:41) - DMV initialized with ['000000'].
# DEBUG - DMV(m9_4_1.py:63) - issuing new plate: 000001
# DEBUG - SmartLicensePlate(m9_2_2.py:80) - .__init__()
# DEBUG - SmartLicensePlate(m9_4_5.py:30) - attaching Car('BMW', 'i4', type_='Electric) to SmartLicensePlate('000001')
# DEBUG - SmartLicensePlate(m9_2_2.py:87) -  -LicensePlate.isvalid()
# INFO - __main__(m9_4_5.py:128) - after registered as:000001, car_2.valid_on_road=True, car_2.license_plate.isvalid()=True
# DEBUG - SmartLicensePlate(m9_4_5.py:30) - attaching OwnershipCard(SmartLicensePlate(000001) to SmartLicensePlate('000001')
# INFO - __main__(m9_4_5.py:133) - before canceling: car_2.valid_on_road=True, ownershipcard_2.is_valid=True
# DEBUG - SmartLicensePlate(m9_2_2.py:105) -  -LicensePlate.cancel(), cancelling 000001.
# DEBUG - SmartLicensePlate(m9_2_2.py:87) -  -LicensePlate.isvalid()
# DEBUG - SmartLicensePlate(m9_4_5.py:41) - notifying Car('BMW', 'i4', type_='Electric) that status changed to  False
# DEBUG - SmartLicensePlate(m9_2_2.py:87) -  -LicensePlate.isvalid()
# DEBUG - Car(m9_4_5.py:95) - Observer method update_status called.
# DEBUG - SmartLicensePlate(m9_2_2.py:87) -  -LicensePlate.isvalid()
# DEBUG - SmartLicensePlate(m9_4_5.py:41) - notifying OwnershipCard(SmartLicensePlate(000001) that status changed to  False
# DEBUG - SmartLicensePlate(m9_2_2.py:87) -  -LicensePlate.isvalid()
# DEBUG - OwnershipCard(m9_4_5.py:115) - Observer method update_status called.
# DEBUG - SmartLicensePlate(m9_2_2.py:87) -  -LicensePlate.isvalid()
# INFO - __main__(m9_4_5.py:137) - car after cancellation:car_2.license_plate._plate_number='000001', car_2.license_plate.isvalid()=False
# INFO - __main__(m9_4_5.py:139) - observers after cancellation:car_2.valid_on_road=False, ownershipcard_2.is_valid=False
