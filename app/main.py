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
            distance_from_city_center: float,
            clean_power: int,
            average_rating: int,
            count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> int:
        price_calculation_1 = self.clean_power - car.clean_mark
        price_calculation_2 = car.comfort_class * price_calculation_1
        price_calculation_3 = price_calculation_2 * self.average_rating
        total_price = price_calculation_3 / self.distance_from_city_center
        return round(total_price, 1)

    def wash_single_car(self, car: Car) -> int:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list) -> int:
        total_income = 0

        for car in cars:
            if car.clean_mark < self.clean_power:
                price = self.calculate_washing_price(car)
                total_income += price
                self.wash_single_car(car)
        return round(total_income, 1)

    def rate_service(self, rate: float) -> float:
        total_rating = self.average_rating * self.count_of_ratings
        total_rating += rate
        self.count_of_ratings += 1
        self.average_rating = round(total_rating / self.count_of_ratings, 1)
