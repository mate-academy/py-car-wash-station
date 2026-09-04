def min_max(
    value: float, min_value: float = 1,
    max_value: float = 10
) -> int | float:

    min_max_value = min(max(min_value, value), max_value)
    return (
        round_1(min_max_value)
        if isinstance(min_max_value, float)
        else min_max_value
    )


def round_1(value: int | float) -> int | float:
    return round(value, 1)


class Car:
    def __init__(
        self, comfort_class: int, clean_mark: int, brand: "str"
    ) -> None:
        self.comfort_class = min_max(comfort_class, max_value=7)
        self.clean_mark = min_max(clean_mark)
        self.brand = brand


class CarWashStation:
    def __init__(
        self, distance_from_city_center: float, clean_power: int,
        average_rating: float, count_of_rating: int
    ) -> None:
        self.distance_from_city_center = min_max(distance_from_city_center)
        self.clean_power = min_max(clean_power)
        self.average_rating = min_max(average_rating, max_value=5)
        self.count_of_rating = count_of_rating

    def serve_cars(self, car_list: list[Car]) -> float:
        income = 0
        income += sum(
                self.calculate_washing_price(car) for car in car_list
                )
        return round_1(income)

    def calculate_washing_price(self, car: Car,) -> float:
        return (
            car.comfort_class * (self.clean_power - car.clean_mark)
            * self.average_rating / self.distance_from_city_center
        ) if self.clean_power > car.clean_mark else 0

    def wash_single_car(self, car: Car) -> None:
            car.clean_mark = self.clean_power