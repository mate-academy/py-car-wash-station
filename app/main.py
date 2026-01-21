class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        if not (1 <= comfort_class <= 7):
            raise ValueError("comfort_class must be from 1 to 7.")
        if not (1 <= clean_mark <= 10):
            raise ValueError("clean_mark must be from 1 to 10.")
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: float,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings
        if not (1 <= distance_from_city_center <= 10):
            raise ValueError("must be from 1.0 to 10.0.")
        if not (1 <= clean_power <= 10):
            raise ValueError("clean_power must be from 1 to 10.")
        if not (1.0 <= average_rating <= 5.0):
            raise ValueError("average_rating must be from 1.0 to 5.0.")
        if count_of_ratings < 0:
            raise ValueError("count_of_ratings can't be negative.")

    def serve_cars(self, cars: list[Car]) -> float:
        total_income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                total_income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(total_income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        price = (car.comfort_class * (self.clean_power - car.
                                      clean_mark) * self.average_rating / self.
                 distance_from_city_center)
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        self.count_of_ratings += 1
        total_ratings_sum = (
            self.average_rating * (self.count_of_ratings - 1) + rate
        )
        self.average_rating = round(
            total_ratings_sum / self.count_of_ratings, 1
        )
