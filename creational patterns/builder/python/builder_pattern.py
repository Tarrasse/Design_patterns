class Car :
    def __init__(self):
        self.wheels_number = 0
        self.doors_number = 0

    def __str__(self):
        return """this car has
- {} wheels
- {} doors""".format(self.wheels_number, self.doors_number)

    class Builder():
        def __init__(self):
            self.car = Car()


        def set_wheels_number(self, wheels_number):
            self.car.wheels_number = wheels_number
            return self
            

        def set_doors_number(self, doors_number):
            self.car.doors_number = doors_number
            return self


        def build(self):
            return self.car


car = Car.Builder().set_wheels_number(5).build()
print car





        
