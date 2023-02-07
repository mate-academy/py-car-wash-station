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
            clean_power: float,
            average_rating: float,
            count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        profit = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                profit += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return round(profit, 1)

    def calculate_washing_price(self, car: Car) -> float:
        differ_power = self.clean_power - car.clean_mark
        main_contain = car.comfort_class * differ_power * self.average_rating
        final_profit = main_contain / self.distance_from_city_center

        return final_profit

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        self.count_of_ratings += 1
        rate_before = self.average_rating * (self.count_of_ratings - 1)
        rating = (rate_before + rate) / self.count_of_ratings

        self.average_rating = round(rating, 1)
