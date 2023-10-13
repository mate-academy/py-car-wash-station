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
        clean_car = self.clean_power - car.clean_mark
        distance_to_rating_ratio = \
            self.average_rating / self.distance_from_city_center
        return round(
            car.comfort_class * clean_car * distance_to_rating_ratio,
            1
        )

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power >= car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: float) -> None:
        if rating > 5 or rating < 1:
            print("You must rate from 1 to 5")
        else:
            self.count_of_ratings += 1
            total_rating = self.average_rating * (self.count_of_ratings - 1)
            new_rating = (total_rating + rating) / self.count_of_ratings
            self.average_rating = round(new_rating, 1)

    def serve_cars(self, cars: list) -> float:
        income = 0
        for car in cars:
            if car.clean_mark <= self.clean_power:
                washing_price = self.calculate_washing_price(car)
                income += round(washing_price, 1)
                self.wash_single_car(car)
        return income
