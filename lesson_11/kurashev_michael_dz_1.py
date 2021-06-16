import datetime

class Date:
    def __init__(self, date):
        self.date = date
        try:
            datetime.datetime.strptime(date, '%d-%m-%Y')
        except ValueError as VE:
            print(VE)

    @classmethod
    def convert_string_to_numeric(cls, date):
        cls.date = date.split('-')
        list_number = []
        for i in cls.date:
            list_number.append(int(i))
        return list_number

    @staticmethod
    def date_validation(date):
        date = date.split('-')
        list_number = []
        for i in date:
            list_number.append(int(i))
        print(list_number)
        if list_number[0] > 31 or list_number[0] < 0:
            raise ValueError
        if list_number[1] > 12 or list_number[1] < 0:
            raise ValueError
        if list_number[2] < 0:
            raise ValueError



a = Date('01-01-2020')
print(Date.convert_string_to_numeric('01-01-2020'))
a.date_validation('31-12-2020')