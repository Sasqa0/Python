import doctest
class Car:
    def __init__(self, seats: int, weight: float):
        """
        Создание и подготовка к работе объекта "Машина"
        :param seats: количество мест в машине
        :param weight: вес машины
        """
        if not isinstance(seats, (int)):
            raise TypeError("Количество мест в машине должно быть типа int")
        if seats <= 1:
            raise ValueError("Количество мест в машине не может быть меньше 1")
        self.seats = seats

        if not isinstance(weight, (int, float)):
            raise TypeError("вес машины должен быть int или float")
        if weight < 0:
            raise ValueError("вес машины не может быть отрицательным числом")
        self.weight = weight

    def type_of_car(self) -> str:
        """
        Функция которая проверяет тип машины
        :return: тип машины
         Пример:
        >>> car_1 = Car(4, 1000)
        >>> car_1.type_of_car()
        """
        ...

    def people_in_car(self, people: int) -> None:
        """
        Количество людей в машине.
        :param people: Количество добавляемых людей
        :raise ValueError: Если количество добавляемых людей превышает свободное место в квартире, то вызываем ошибку
        """
        if not isinstance(people, (int)):
            raise TypeError("Люди должны быть типа int")
        if people < 0:
            raise ValueError("Людей должно быть =>0")
        ...

class Gun:
    def __init__(self, store_magazine: int, weight: float):
        """
        Создание и подготовка к работе объекта "Оружие"
        :param store_magazine: вместительность магазина
        :param weight: вес оружия
        """
        if not isinstance(store_magazine, (int)):
            raise TypeError("вместительность магазина должна быть типа int")
        if store_magazine <= 0:
            raise ValueError("вместительность магазина не может быть меньше 0")
        self.store_magazine = store_magazine

        if not isinstance(weight, (int, float)):
            raise TypeError("вес оружия должен быть float")
        if weight == 0:
            raise ValueError("вес не может быть нулевым")
        self.weight = weight

    def is_big_gun(self) -> str:
        """
        Функция которая проверяет,тяжелое ли оружие
        :return: Является ли оружие тяжелым
         Пример:
        >>> gun = Gun(30, 3900)
        >>> gun.is_big_gun()
        """
        ...

    def type_of_gun(self) -> str:
        """
       Функция которая проверяет тип оружия
        :return тип оружия
        """

class Sofa:
    def __init__(self, material: str, sofa_legs: int):
        """
        Создание и подготовка к работе объекта "диван"
        :param material: материал дивана
        :param sofa_legs: количество ножек дивана
        """
        if not isinstance(material, (str)):
            raise TypeError("Материал обивки дивана должеж быть типа str")
        if len(material) == 0:
            raise ValueError("Материал обивки дивана не может быть пустым")
        materials = ["хлопок", "экокожа", "замша"]
        if material not in materials:
            print(f"'{material}' - редкий материал обивки дивана")
        self.material = material

        if not isinstance(sofa_legs, (int)):
            raise TypeError("Количество ножек у дивана должно быть int")
        if sofa_legs <= 1:
            raise ValueError("Количество ножек у дивана не может быть меньше 2")
        self.sofa_legs = sofa_legs

    def is_sofa_is_for_house(self) -> bool:
        """
        Функция которая проверяет подходит ли диван для дома
        :return: Является ли диван подходящим для дома
         Пример:
        >>> sofa = Sofa("экокожа", 3)
        >>> sofa.is_sofa_is_for_house()
        """
        ...

    def type_of_sofa(self) -> str:

        """
        Определение типа дивана по параметрам
        :return тип диван в зависимости от характеристик
        Пример:
        >>> sofa_1 = Sofa("хлопок", 3)
        >>> sofa_1.type_of_sofa()
        """

if __name__ == "__main__":
    doctest.testmod(verbose=True)