"""Demo Composite pattern"""
from abc import ABC, abstractmethod
from logging import Logger
from m8_2_2 import get_logger, logging_context as log_to


class Academics(ABC):
    """Academics abstract class, have advance and graduate methods"""
    _logger: Logger | None = None

    @property
    def logger(self):
        """all class inherits Academics will have .logger property"""
        if not self.__class__._logger:
            self.__class__._logger = get_logger(
                self.__class__.__name__, "DEBUG")
        return self.__class__._logger

    @abstractmethod
    def advance(self):
        """advance to next grade level (school year)"""
        pass

    @abstractmethod
    def graduate(self):
        """graduate from school"""
        pass


class Student(Academics):
    """the individual class"""

    def __init__(self, name: str, grade: int = 1):
        """construct a student with name and entry grade"""
        self.name = name
        self.grade = grade
        self.graduated = False

    def advance(self):
        """advance to next school year, one higher grade level"""
        self.logger.debug("%r is advancing to next grade", self)
        self.grade += 1

    def graduate(self):
        """graduate from school, mark self.graduated to True"""
        self.graduated = True

    def __repr__(self) -> str:
        """return text representation of the Student object"""
        return f"{self.__class__.__name__}('{self.name}', {self.grade})"


class Composite(Academics):
    """the collection class of students, also implemented advance & graduate"""

    def __init__(self, *args) -> None:
        """construct Coposite class to be a container of children"""
        self.children = []
        if all([isinstance(x, Academics) for x in args]):
            self.children.extend(args)
        else:
            self.logger.error("%r has members that are not Academics", args)
            raise ValueError(f"{args} contain members are not Academics")

    def add(self, child: Academics) -> None:
        """adding childre that are derived from Academics to the list"""
        if isinstance(child, Academics):
            self.children.append(child)
        else:
            self.logger.error("%r is not Academics", child)
            raise ValueError(f"{child} is not Academics")

    def remove(self, child) -> None:
        """remove a student from the list, log warning if not found"""
        try:
            self.children.remove(child)
        except Exception as e:
            self.logger.warning(
                f"cannot remove {child}, it may not exist. {e}")

    def advance(self) -> None:
        """move all childre to next grade level by calling their advance()"""
        self.logger.debug("%r is advancing to next grade", self)
        for child in self.children:
            child.advance()

    def graduate(self) -> None:
        """set all children to graduated by calling their graduate()"""
        for child in self.children:
            child.graduate()

    def __repr__(self) -> str:
        """recursively use text to represent self"""
        return f"{self.__class__.__name__}({','.join([repr(c) for c
                                                      in self.children])})"


def main() -> None:
    """demo composite apply group actions"""
    student_1 = Student("Albert Einstein")
    student_2 = Student("Benjamin Franklin")
    student_3 = Student("Charles Darwin")
    famous_class = Composite(student_1, student_2)
    famous_class.add(student_3)

    school = Composite(famous_class, Composite(
        Student("David Smith", 5), Student("Edward Jones", 5)))
    unheard_class = school.children[1]

    print("#", school)
    school.advance()
    print("#", school)
    unheard_class.graduate()
    print(f"# {unheard_class.children[0].graduated=}, {student_1.graduated=}")


if __name__ == "__main__":
    with log_to("main", stream=False) as logger:
        main()

# Composite(Composite(Student('Albert Einstein', 1),Student('Benjamin Franklin', 1),Student('Charles Darwin', 1)),Composite(Student('David Smith', 5),Student('Edward Jones', 5)))
#    DEBUG - m9_4_4.py:83 Composite.advance() - Composite(Composite(Student('Albert Einstein', 1),Student('Benjamin Franklin', 1),Student('Charles Darwin', 1)),Composite(Student('David Smith', 5),Student('Edward Jones', 5))) is advancing to next grade
#    DEBUG - m9_4_4.py:83 Composite.advance() - Composite(Student('Albert Einstein', 1),Student('Benjamin Franklin', 1),Student('Charles Darwin', 1)) is advancing to next grade
#    DEBUG - m9_4_4.py:41 Student.advance() - Student('Albert Einstein', 1) is advancing to next grade
#    DEBUG - m9_4_4.py:41 Student.advance() - Student('Benjamin Franklin', 1) is advancing to next grade
#    DEBUG - m9_4_4.py:41 Student.advance() - Student('Charles Darwin', 1) is advancing to next grade
#    DEBUG - m9_4_4.py:83 Composite.advance() - Composite(Student('David Smith', 5),Student('Edward Jones', 5)) is advancing to next grade
#    DEBUG - m9_4_4.py:41 Student.advance() - Student('David Smith', 5) is advancing to next grade
#    DEBUG - m9_4_4.py:41 Student.advance() - Student('Edward Jones', 5) is advancing to next grade
# Composite(Composite(Student('Albert Einstein', 2),Student('Benjamin Franklin', 2),Student('Charles Darwin', 2)),Composite(Student('David Smith', 6),Student('Edward Jones', 6)))
# unheard_class.children[0].graduated=True, student_1.graduated=False
