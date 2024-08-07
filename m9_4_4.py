"""Demo Composite pattern"""
from abc import ABC, abstractmethod
import logging
logging.basicConfig(level=logging.INFO, format="#%(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")


class Academics(ABC):
    """Academics abstract class, have advance and graduate methods"""
    @property
    def logger(self):
        """all class inherits Academics will have .logger property"""
        return logging.getLogger(self.__class__.__name__)

    @abstractmethod
    def advance(self):
        """advance to next grade level (school year)"""
        pass

    @abstractmethod
    def graduate(self):
        """graduate from school"""
        pass


class Student(Academics):
    def __init__(self, name: str, grade: int = 1):
        """construct a student with name and entry grade"""
        self.name = name
        self.grade = grade
        self.graduated = False

    def advance(self):
        """advance to next school year, one higher grade level"""
        self.grade += 1

    def graduate(self):
        """graduate from school, mark self.graduated to True"""
        self.graduated = True

    def __repr__(self) -> str:
        """return text representation of the Student object"""
        return f"{self.__class__.__name__}('{self.name}', {self.grade})"


class Composite(Academics):
    """The collection class that will call advance and graduate for all children"""

    def __init__(self, *args):
        """construct Coposite class to be a container of children"""
        self.children = []
        self.children.extend(args)

    def add(self, child: Academics):
        """adding childre that are derived from Academics to the list"""
        self.children.append(child)

    def remove(self, child):
        """remove a student from the list, log warning if not found"""
        try:
            self.children.remove(child)
        except Exception as e:
            self.logger.warning(
                f"cannot remove {child}, it may not exist. {e}")

    def advance(self):
        """move all childre to next grade level by calling their advance()"""
        for child in self.children:
            child.advance()

    def graduate(self):
        """set all children to graduated by calling their graduate()"""
        for child in self.children:
            child.graduate()

    def __repr__(self):
        """recursively use text to represent self"""
        results = []
        for child in self.children:
            results.append(f"{repr(child)}")
        return f"{self.__class__.__name__}({','.join(results)})"


def main():
    student_1 = Student("Albert Einstein")
    student_2 = Student("Benjamin Franklin")
    student_3 = Student("Charles Darwin")
    famous_class = Composite()
    famous_class.add(student_1)
    famous_class.add(student_2)
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
    main()

# Composite(Composite(Student('Albert Einstein', 1),Student('Benjamin Franklin', 1),Student('Charles Darwin', 1)),Composite(Student('David Smith', 5),Student('Edward Jones', 5)))
# Composite(Composite(Student('Albert Einstein', 2),Student('Benjamin Franklin', 2),Student('Charles Darwin', 2)),Composite(Student('David Smith', 6),Student('Edward Jones', 6)))
# unheard_class.children[0].graduated=True, student_1.graduated=False
