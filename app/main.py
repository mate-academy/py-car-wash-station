class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    #  washes only cars with clean_mark < clean_power of wash station
    #  and returns income of CarWashStation for serving
    #  this list of Car's, rounded to 1 decimal
    def serve_cars(self, list_cars: list) -> float:
        income = 0
        for car in list_cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return income

    #  calculate cost of washing single car
    def calculate_washing_price(self, car: Car) -> float:
        cost = round(
            car.comfort_class * (self.clean_power - car.clean_mark)
            * self.average_rating / self.distance_from_city_center,
            1
        )
        return cost

    #  change car clean_mark after washing
    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    #  change average_rating and count_of_ratings after receiving
    #  new rate mark
    def rate_service(self, rate: int) -> None:
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + rate)
            / (self.count_of_ratings + 1),
            1
        )
        self.count_of_ratings += 1
