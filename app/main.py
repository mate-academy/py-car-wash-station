class Car:
    def __init__(
        self,
        comfort_class: str,
        clean_mark: str,
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
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: str) -> float:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                price = self.calculate_washing_price(car)
                income += price
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: str) -> float:
        diff = self.clean_power - car.clean_mark
        if diff <= 0:
            return 0.0
        delta = self.average_rating / self.distance_from_city_center
        price = car.comfort_class * (self.clean_power - car.clean_mark) * delta
        return round(price, 1)

    def wash_single_car(self, car: str) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, new_rating : int) -> float:
        total = self.average_rating * self.count_of_ratings + new_rating
        self.count_of_ratings += 1
        self.average_rating = round(total / self.count_of_ratings, 1)
