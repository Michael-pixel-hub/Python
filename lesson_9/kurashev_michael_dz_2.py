class Road:
    _length = 5
    _width = 10
    def __init__(self, mass, blade_thickness):
        mass_of_asf = Road._length*Road._width*mass*blade_thickness
        print(f'{Road._length} м * {Road._width} м * {mass} кг * {blade_thickness} см = {mass_of_asf}')

road = Road(3,4)