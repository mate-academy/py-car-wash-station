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
    def __init__(
            self,
            distance_from_city_center: int,
            clean_power: int,
            average_rating: int,
            count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        if car.clean_mark == self.clean_power:
            return 0
        cleanliness_increase = self.clean_power - car.clean_mark
        price = (
            (
                car.comfort_class * cleanliness_increase * self.average_rating
            ) / self.distance_from_city_center
        )
        return round(price, 1)

    def wash_single_car(self, car: Car) -> float:
        if car.clean_mark < self.clean_power:
            wash_price = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return wash_price
        return 0

    def serve_cars(self, cars: list) -> float:
        total_income = 0
        for car in cars:
            total_income += self.wash_single_car(car)
        return round(total_income, 1)

    def rate_service(self, new_rating: float) -> None:
        total_rating = (
            self.average_rating * self.count_of_ratings
        ) + new_rating
        self.count_of_ratings += 1
        self.average_rating = round(total_rating / self.count_of_ratings, 1)
