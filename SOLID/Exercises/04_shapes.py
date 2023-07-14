from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def calculate_area(self) -> float:
        pass


class Rectangle(Shape):

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        return self.width * self.height


class Triangle(Shape):

    def __init__(self, side: float, height: float):
        self.side = side
        self.height = height

    def calculate_area(self) -> float:
        return self.side * self.height * 0.5


class AreaCalculator:

    def __init__(self, shapes: list):
        self.shapes = shapes
        
    @property
    def shapes(self):
        return self.__shapes
    
    @shapes.setter
    def shapes(self, value):
        if not isinstance(shapes, list):
            raise AssertionError(f"`shapes` should be of type `list`.")

        self.__shapes = value

    @property
    def total_area(self) -> float:

        total = 0

        for shape in self.shapes:
            total += shape.calculate_area()

        return total


shapes = [Rectangle(2, 3), Rectangle(1, 6)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)

shapes = [Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)
