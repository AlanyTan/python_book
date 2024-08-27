"""Demo Observer pattern"""
from abc import ABC, abstractmethod
from m8_2_2 import get_logger, logging_context as log_to
from m9_4_1 import DMV, Vehicle, LicensePlate, Engine


class Observer(ABC):
    """the abstract class for observer of something worth monitoring"""
    @abstractmethod
    def be_notified(self, status) -> None:
        """abstract method, Observer must implement be_notified"""
        pass


class Notifier(ABC):
    """the abstract base class for the notifying observers of status changes """
    @property
    @abstractmethod
    def status(self) -> bool:
        """abstract property, My status that Observers need to be notified"""
        pass

    def __init__(self) -> None:
        """setup internal list of observers."""
        self.logger = get_logger(self.__class__.__name__, "DEBUG")
        self._observers = []

    def attach(self, observer: Observer) -> None:
        """add an observer as a registered observer of this notifier"""
        self.logger.debug("attaching %r to %r as observer", observer, self)
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """del an observer from registered observer list"""
        self.logger.debug("detaching %r from %r", observer, self)
        self._observers.remove(observer)

    def notify(self):
        """the notification method, call all the registered observer's update"""
        for observer in self._observers:
            self.logger.debug("notifying %r that my status changed to %s",
                              observer, self.status)
            observer.be_notified(self.status)


class SmartLicensePlate(Notifier):
    """adaptor for LicensePlate to inherit from Notifier"""

    def __init__(self, *args) -> None:
        """construct SmartLicensePlate by calling super(). then Notifer init"""
        super().__init__()
        self.actual_plate = LicensePlate(*args)

    @property
    def status(self) -> bool:
        """override abstract property from Notifier as an alias to .isvalid()"""
        return self.actual_plate.isvalid()

    def cancel(self) -> None:
        """add notification after the LicensePlate.cancel()"""
        self.actual_plate.cancel()
        self.notify()

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}("
                f"'{self.actual_plate._plate_number}')")


class Car(Vehicle, Observer):
    """Inherit Vehicle, composition Engine, Aggregation LisensePlate"""

    def __init__(self, make: str, model: str, type_: str | None = None,
                 cylinders: int = 4, displacement: float = 0) -> None:
        """Construct a car by defining an Engine, and a license placeholder"""
        super().__init__(4, 90)
        self.make = make
        self.model = model
        self.engine = Engine(type_=type_, cylinders=cylinders,
                             displacement=displacement)
        self.license_plate = None
        self.valid_on_road = False
        self.logger.debug("Initialized a car with %s wheels, and a %r",
                          self.wheels, self.engine)

    def register(self) -> None:
        """register the vehicle to obtain a license plate"""
        dmv = DMV()
        self.license_plate = SmartLicensePlate(dmv.issue())
        self.license_plate.attach(self)
        self.valid_on_road = True

    def be_notified(self, status) -> None:
        """override abstract method from Observer, allow receiving info"""
        self.logger.debug("Observer method is called.")
        self.valid_on_road = status

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}('{self.make}', "
                f"'{self.model}', type_='{self.engine._type})")


class OwnershipCard(Observer):
    """The ownership card of the car registration"""

    def __init__(self, license_plate: SmartLicensePlate):
        """initialize ownership card aggregate with license_plate"""
        self.logger = get_logger(self.__class__.__name__, "DEBUG")
        self.is_valid = True
        self.license_plate = license_plate
        license_plate.attach(self)

    def be_notified(self, status):
        """override abstract method from Observer, allow receiving info"""
        self.logger.debug("Observer method called.")
        self.is_valid = status

    def __repr__(self):
        return (f"{self.__class__.__name__}(SmartLicensePlate("
                f"{self.license_plate.actual_plate._plate_number})")


def main() -> None:
    """"demo Observer - Notifier pattern"""
    car_2 = Car("BMW", "i4", type_='Electric', cylinders=0)
    logger.info("before register: LicensePlate=%r; valid_on_road=%r",
                car_2.license_plate, car_2.valid_on_road)
    car_2.register()
    logger.info("after registered as: %r, valid_on_road=%s, plate_valid=%s",
                car_2.license_plate, car_2.valid_on_road,
                car_2.license_plate.status)
    license_plate_2 = car_2.license_plate

    ownershipcard_2 = OwnershipCard(license_plate_2)
    logger.info("before canceling: car is valid_on_road=%s, ownershipcard "
                "is_valid=%s", car_2.valid_on_road, ownershipcard_2.is_valid)

    license_plate_2.cancel()
    logger.info("after cancellation: car is valid_on_road=%s, ownershipcard "
                "is_valid=%s", car_2.valid_on_road, ownershipcard_2.is_valid)


if __name__ == "__main__":
    with log_to("main", stream="DEBUG") as logger:
        main()

#    DEBUG - m9_2_2.py:31 Car.__init__() - constructing a Vehicle
#    DEBUG - m9_2_2.py:133 Engine.__init__() - construct an Engine
#    DEBUG - m9_4_5.py:82 Car.__init__() - Initialized a car with 4 wheels, and a a 0 liter 0 cylinder Electric engine.
#     INFO - m9_4_5.py:125 main.main() - before register: LicensePlate=None; valid_on_road=False
#    DEBUG - m9_4_1.py:52 DMV.__init__() - DMV initialized with ['000000'].
#    DEBUG - m9_4_1.py:71 DMV.issue() - issuing new plate: 000001
#    DEBUG - m9_2_2.py:89 LicensePlate.__init__() - construct a License Plate
#    DEBUG - m9_4_5.py:30 SmartLicensePlate.attach() - attaching Car('BMW', 'i4', type_='Electric) to SmartLicensePlate('000001') as observer
#    DEBUG - m9_2_2.py:96 LicensePlate.isvalid() -  checking the validity of 000001
#     INFO - m9_4_5.py:128 main.main() - after registered as: SmartLicensePlate('000001'), valid_on_road=True, plate_valid=True
#    DEBUG - m9_4_5.py:30 SmartLicensePlate.attach() - attaching OwnershipCard(SmartLicensePlate(000001) to SmartLicensePlate('000001') as observer
#     INFO - m9_4_5.py:134 main.main() - before canceling: car is valid_on_road=True, ownershipcard is_valid=True
#    DEBUG - m9_2_2.py:114 LicensePlate.cancel() - cancelling '000001'
#    DEBUG - m9_2_2.py:96 LicensePlate.isvalid() -  checking the validity of 000001
#    DEBUG - m9_4_5.py:41 SmartLicensePlate.notify() - notifying Car('BMW', 'i4', type_='Electric) that my status changed to False
#    DEBUG - m9_2_2.py:96 LicensePlate.isvalid() -  checking the validity of 000001
#    DEBUG - m9_4_5.py:94 Car.be_notified() - Observer method is called.
#    DEBUG - m9_2_2.py:96 LicensePlate.isvalid() -  checking the validity of 000001
#    DEBUG - m9_4_5.py:41 SmartLicensePlate.notify() - notifying OwnershipCard(SmartLicensePlate(000001) that my status changed to False
#    DEBUG - m9_2_2.py:96 LicensePlate.isvalid() -  checking the validity of 000001
#    DEBUG - m9_4_5.py:114 OwnershipCard.be_notified() - Observer method called.
#     INFO - m9_4_5.py:138 main.main() - after cancellation: car is valid_on_road=False, ownershipcard is_valid=False
#     INFO - m8_2_2.py:67 main.logging_context() - shutting down the logging facility...
