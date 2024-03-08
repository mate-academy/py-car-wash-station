class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        #  comfort class of a car, from 1 to 7
        self.comfort_class = comfort_class
        # car cleanness mark, from very dirty - 1 to absolutely clean - 10
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        # how far station from the city center, from 1.0 to 10.0
        self.dist_to_center = distance_from_city_center \
            if distance_from_city_center != 0 else 0.00000000001
        # clean_mark to which this car wash station washes
        self.clean_power = clean_power
        # average rating of the station, from 1.0 to 5.0, rounded to 1 decimal
        self.average_rating = average_rating
        # number of people who rated
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        return round(car.comfort_class
                     * (self.clean_power - car.clean_mark)
                     * self.average_rating / self.dist_to_center, 1)

    def serve_cars(self, cars: list) -> float:
        return sum([self.wash_single_car(car) for car in cars])

    def wash_single_car(self, car: Car) -> float:
        if car.clean_mark < self.clean_power:
            res = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return res
        return 0.0

    def rate_service(self, rate: int) -> None:
        self.average_rating = round((self.average_rating
                                     * self.count_of_ratings + rate)
                                    / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
