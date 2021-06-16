class Warehouse:
    list_of_companies_in_stock = {}  # создаем словарь с компаниями и склад с продуктами в этих компаниях ({'': {}})
    products = {}  # создаем склад продуктов

    def __init__(self, warehouse_name, *company_name):
        self.warehouse_name = warehouse_name  # создаем название склада
        for i in company_name:
            self.list_of_companies_in_stock[i] = self.products  # добавляем компании в словарь и место для товаров


class Office_equipment(Warehouse):

    def __init__(self, model, warehouse_name, *company_name):
        super().__init__(warehouse_name, *company_name)
        self.model = model

    def equipment_in_stock(self, company_name, product_name, quantity):
        try:  # если есть в словаре product_name
            a = self.list_of_companies_in_stock.setdefault(company_name)
            # создаем переменную, где храним значение (продукты) компании (склад)
            b = a
            b[product_name] = b[product_name] + quantity
            # добавляем в переменную значение (кол-во) продукта на складе
            self.list_of_companies_in_stock[company_name] = a
            # создаем склад
        except KeyError:  # срабатывает, когда список продуктов пуст или в словаре нет данного продукта, но есть другие
            a = self.list_of_companies_in_stock.setdefault(company_name)
            if not a:  # срабатывает, если словарь пуст
                b = {}
                b[product_name] = quantity
                self.list_of_companies_in_stock[company_name] = b
            else:  # срабатывает, если в словаре нет данного продукта, но есть другие
                a[product_name] = quantity
                self.list_of_companies_in_stock[company_name] = a
        return self.list_of_companies_in_stock


class Printer(Office_equipment):
    def __init__(self, printing_technology, model, warehouse_name, *company_name):
        super().__init__(model, warehouse_name, *company_name)
        self.printing_technology = printing_technology


class Scanner(Office_equipment):
    def __init__(self, scanner_type, model, warehouse_name, *company_name):
        super().__init__(model, warehouse_name, *company_name)
        self.scanner_type = scanner_type


class Xerox(Office_equipment):
    def __init__(self, print_resolution, model, warehouse_name, *company_name):
        super().__init__(model, warehouse_name, *company_name)
        self.print_resolution = print_resolution


technika = Xerox('1280/720', 'Модель №1', 'Склад №1', 'Компания №1', 'Компания №2', 'Компания №3')
technika.equipment_in_stock('Компания №1','Модель №1', 55)
print(technika.list_of_companies_in_stock)
technika.equipment_in_stock('Компания №1','Модель №1', 60)
print(technika.list_of_companies_in_stock)
technika.equipment_in_stock('Компания №2','Модель №2', 44)
print(technika.list_of_companies_in_stock)