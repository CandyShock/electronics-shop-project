import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int, ) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> int:
        """
        Применяет установленную скидку для конкретного товара.
        """
        return int(self.price * self.pay_rate)

    def name_add(self):
        return self.all.append(self.__name)

    def display(self):
        return f'{self.__name}'

    @property
    def getter_name(self):
        return f"{self.__name}"

    @getter_name.setter
    def getter_name(self, name):
        self.__name = name
        if len(self.__name) < 10:
            self.__name = name
        else:
            print('Длина наименования товара превышает 10 символов')

    @classmethod
    def instantiate_from_csv(cls, csv_str):

        for name, price, quantity in csv_str:
            cls.all.append(cls(name, price, quantity))

        return cls.all

    @staticmethod
    def string_to_number(random_str):
        random_str = float(random_str)
        random_str = round(int(random_str))
        return random_str


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"


    def __str__(self):
        return f"{self.__name}"



#print(Item.string_to_number('5.7'))
#emp_1 = Item("Смартфон", 10000, 20)
#print(repr(emp_1))
