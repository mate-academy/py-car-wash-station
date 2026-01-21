class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        if car.clean_mark >= self.clean_power:
            return 0.0
        difference = self.clean_power - car.clean_mark
        price = (
            car.comfort_class * difference * self.average_rating
        ) / self.distance_from_city_center
        return round(price, 1)

    # Глупый flak8 ругался то на длину рядка,
    # то на перенос, пришлось вывести в отдельную переменную.
    # А можно игронировать придупреждение flak8 когда на несколько
    # символов длина больше?
    # Просто какае-то глупость, ставить подобного рода костыль,
    # чтоб исправить это.
    # Он даже ругаеться на длину комента...
    # Как от этого у меня горит...
    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = min(self.clean_power, 10)

    def serve_cars(self, cars: list[Car]) -> float:
        total_income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                wash_cost = self.calculate_washing_price(car)
                self.wash_single_car(car)
                total_income += wash_cost
        return round(total_income, 1)

    def rate_service(self, new_rating: float) -> None:
        self.count_of_ratings += 1
        total_ratings = (
            self.average_rating * (self.count_of_ratings - 1) + new_rating
        )
        self.average_rating = round(total_ratings / self.count_of_ratings, 1)
