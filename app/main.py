class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: int,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, other: Car):
        if isinstance(other, Car):
            return other.comfort_class * (self.clean_power - other.clean_mark) \
                   * self.average_rating / self.distance_from_city_center
        else:
            raise TypeError(f"'{type(other)}' not supported for this method. Requires 'Car'")

    def wash_single_car(self, other: Car):
        if isinstance(other, Car):
            other.clean_mark = self.clean_power
        else:
            raise TypeError(f"{type(other)} type not supported. Requires 'Car'")

    def serve_cars(self, cars: list):
        if isinstance(cars, list):
            income = 0
            for car in cars:
                if self.clean_power > car.clean_mark:
                    income += self.calculate_washing_price(car)
                    self.wash_single_car(car)
            return round(income, 1)
        else:
            raise TypeError(f"{type(cars)} type not supported. Requires list")

    def rate_service(self, score):
        if isinstance(score, (int, float)):
            if 1 <= score <= 5:
                self.average_rating = round((self.average_rating * self.count_of_ratings + score) /
                                            (self.count_of_ratings + 1), 1)
                self.count_of_ratings += 1

            else:
                raise ValueError(f"The score should be from 1 to 5")
        else:
            raise TypeError(f"{type(score)} type not supported. Requires int or float")
