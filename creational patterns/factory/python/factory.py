class Shape:
    def __init__(self):
        pass

    @staticmethod
    def factory(instance_type):
        if instance_type == Circle.__name__:
            return Circle()
        elif instance_type == Square.__name__:
            return Square()


class Circle(Shape):
    def __init__(self):
        Shape.__init__(self)

    def draw(self):
        print "Circle.draw"

    def erase(self):
        print "Circle.erase"


class Square(Shape):
    def __init__(self):
        Shape.__init__(self)

    def draw(self):
        print "Square.draw"

    def erase(self):
        print "Square.erase"


def main():
    square = Shape.factory(Square.__name__)
    circle = Shape.factory(Circle.__name__)
    square.draw()
    square.erase()
    circle.draw()
    circle.erase()

if __name__ == '__main__':
    main()