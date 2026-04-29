class Car:
    def __init__(
        self,
        comfort_class: int,
        clean_mark: int,
        brand: str,
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int, average_rating: float,
        count_of_ratings: int,
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        result = 0

        for car in cars:
            result += self.wash_single_car(car)

        return result

    def calculate_washing_price(self, car: Car) -> float:

        difference = self.clean_power - car.clean_mark
        multiplier_1 = car.comfort_class * difference
        multiplier_2 = multiplier_1 * self.average_rating

        income = round((multiplier_2 / self.distance_from_city_center), 1)

        return income

    def wash_single_car(self, car: Car) -> float:
        if car.clean_mark < self.clean_power:
            price = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return price

        return 0

    def rate_service(self, new_rating: int) -> float:

        sum_of_ratings = self.average_rating * self.count_of_ratings
        divider_1 = sum_of_ratings + new_rating

        self.count_of_ratings += 1
        self.average_rating = round(divider_1 / self.count_of_ratings, 1)

        return self.average_rating
