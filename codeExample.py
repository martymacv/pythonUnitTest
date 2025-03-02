class Receipt:
    """Класс для создания чека и наполнения его данными о покупках"""
    __instance = None
    __receipt_id = 0

    def __new__(cls, *args, **kwargs):
        cls.__instance = super().__new__(cls)
        cls.__receipt_id += 1
        return cls.__instance

    def __init__(self, name, surname, patronymic, date, time, total):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.date = date
        self.time = time
        self.total = total
        self.items = []

    def __len__(self):
        return len(self.items)

    @classmethod
    def get_receipt_id(cls):
        return cls.__receipt_id

    @property
    def id(self):
        return self.get_receipt_id()

    def add_item(self, item):
        self.items.append(item)

    def print_receipt(self):
        print("Чек №", self.id)
        print("Покупатель:", self.name, self.surname, self.patronymic)
        print("Дата:", self.date)
        print("Время:", self.time)
        print("Итого:", self.total)
        for item in self.items:
            print(item.name, item.price, item.quantity)


class Item:
    """Класс для создания товара, его цены за штуку или вес и количество"""
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


if __name__ == "__main__":
    receipt = Receipt("Иван", "Иванов", "Иванович", "12.12.2020", "12:00", 100)
    receipt.add_item(Item("Молоко", 50, 2))
    receipt.add_item(Item("Хлеб", 30, 1))
    receipt.print_receipt()
    receipt2 = Receipt("Петр", "Петров", "Петрович", "12.12.2020", "12:00", 100)
    receipt2.add_item(Item("Молоко", 50, 2))
    receipt2.add_item(Item("Хлеб", 30, 1))
    receipt2.print_receipt()
