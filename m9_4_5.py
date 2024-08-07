"""Demo Observer pattern"""
from abc import ABC, abstractmethod
import logging
logging.basicConfig(level=logging.INFO, format="#%(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
from m9_4_1 import DMV, Vehicle, LicensePlate, Engine


class Observer(ABC):
    @abstractmethod
    def update_status(self, status):
        pass


class Notifier(ABC):
    @property
    @abstractmethod
    def status(self):
        pass

    def __init__(self):
        """setup internal list of observers."""
        self._observers = []

    def attach(self, observer: Observer):
        """add an observer as a registered observer of this notifier"""
        self._observers.append(observer)

    def detach(self, observer: Observer):
        """del an observer from registered observer list"""
        self._observers.remove(observer)

    def notify(self):
        """the notification method, call all the registered observer's update"""
        for observer in self._observers:
            observer.update_status(self.status)


class Car(Vehicle, Observer):
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
        self.valid_on_road = status


class OwnershipCard(Observer):
    """The ownership card of the car registration"""

    def __init__(self):
        """initialize ownership card aggregate with license_plate"""
        self.is_valid = True
        self.license_plate = None

    def update_status(self, status):
        """override abstract method from Observer, allow receiving info"""
        self.is_valid = status


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


def main():
    car_2 = Car("BMW", "i4", type_='Electric', cylinders=0)
    print(f"# created car with {car_2.engine}")
    print(f"# current licenseplate: "
          "{car_2.license_plate}, {car_2.valid_on_road}")
    car_2.register()
    print(f"# car_2 registered as:{car_2.license_plate._plate_number}, "
          f"{car_2.valid_on_road=}, {car_2.license_plate.isvalid()=}")

    ownershipcard_2 = OwnershipCard()
    ownershipcard_2.license_plate = car_2.license_plate
    ownershipcard_2.license_plate.attach(ownershipcard_2)
    print(f"# {car_2.valid_on_road=}, {ownershipcard_2.is_valid=}")

    car_2.license_plate.cancel()
    print(f"# car_2 registered as:{car_2.license_plate._plate_number}, "
          f"{car_2.license_plate.isvalid()=}")
    print(f"# {car_2.valid_on_road=}, {ownershipcard_2.is_valid=}")


if __name__ == "__main__":
    main()
