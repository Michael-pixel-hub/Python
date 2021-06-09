class Worker:
    the_salary = {"wage": 25, "bonus": 225}
    name = 'Гена'
    surname = 'Петров'
    position = 'Дизайнер'
    _income = the_salary
class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}')
    def get_total_income(self):
        print(self._income["wage"] + self._income["bonus"])

position = Position()
print(position.name)
print(position.surname)
print(position.position)
print(position._income)
position.get_full_name()
position.get_total_income()