class Car:
    def __init__(self,
                 comfort_class: int = 1,
                 clean_mark: int = 1,
                 brand: str = None) -> None:
        if not (1 <= comfort_class <= 7):
            raise ValueError("Comfort class must be between 1 and 7")
        if not (1 <= clean_mark <= 10):
            raise ValueError("Clean mark must be between 1 and 10")
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:

    def __init__(self,
                 distance_from_city_center: float = 1.0,
                 clean_power: int = None,
                 average_rating: float = 1.0,
                 count_of_ratings: int = None) -> None:
        if not (1.0 <= distance_from_city_center <= 10.0):
            raise ValueError("Comfort class must be between 1 and 7")
        if not (1.0 <= average_rating <= 5.0):
            raise ValueError("Clean mark must be between 1 and 10")
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        income = 0
        for single_car in cars:
            if single_car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(single_car)
                self.wash_single_car(single_car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        return round(((car.comfort_class
                       * (self.clean_power
                          - car.clean_mark)
                       * self.average_rating)
                      / self.distance_from_city_center), 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        total_rating = ((self.average_rating
                         * self.count_of_ratings)
                        + rate)
        self.count_of_ratings += 1
        self.average_rating = round(total_rating / self.count_of_ratings, 1)
