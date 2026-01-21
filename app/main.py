from typing import List


class Car:
    def __init__(self, clean_mark: int, dirt_level: int, brand: str) -> None:
        self.clean_mark: int = clean_mark
        self.dirt_level: int = dirt_level
        self.brand: str = brand


class CarWashStation:
    def __init__(self, clean_power: int, max_cars: int, price_per_unit: float,
                 efficiency: int) -> None:
        self.clean_power: int = clean_power
        self.max_cars: int = max_cars
        self.price_per_unit: float = price_per_unit
        self.efficiency: int = efficiency

    def wash_single_car(self, car: Car) -> float:
        """
        Оновлює clean_mark машини і повертає вартість миття.
        """
        if car.clean_mark >= self.clean_power:
            return 0.0

        car.clean_mark = max(car.clean_mark, self.clean_power)
        return self.calculate_washing_price(car)

    def calculate_washing_price(self, car: Car) -> float:
        """
        Розраховує вартість миття машини.
        """
        return car.clean_mark * self.price_per_unit

    def serve_cars(self, cars: List[Car]) -> float:
        """
        Міє список машин і повертає загальний дохід.
        Максимум max_cars машин за раз.
        """
        total_income: float = 0.0
        for i, car in enumerate(cars):
            if i >= self.max_cars:
                break
            total_income += self.wash_single_car(car)
        return total_income
