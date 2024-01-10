class Car:

    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:

    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int
                 ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars_to_serve: list) -> float:
        """Washes cars and collecting money"""

        income = 0
        for car in cars_to_serve:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        """Calculate price for washing single car"""

        price = (car.comfort_class
                 * (self.clean_power - car.clean_mark)
                 * self.average_rating
                 / self.distance_from_city_center)

        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        """Washes a single car"""

        car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        """Adds a single rate and change average_rating and count_of_ratings"""

        new_average_rating = (self.average_rating * self.count_of_ratings + rate) / (self.count_of_ratings + 1)
        self.count_of_ratings += 1
        self.average_rating = round(new_average_rating, 1)
