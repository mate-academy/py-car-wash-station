class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: int,
                 clean_power: int,
                 average_rating: int,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> int:
        income = 0
        for car in cars:
            income += self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car: Car) -> float:
        washing_price = (car.comfort_class
                         * (self.clean_power
                             - car.clean_mark)
                         * (self.average_rating
                             / self.distance_from_city_center))
        return round(washing_price, 1)

    def wash_single_car(self, car: Car) -> float:
        if self.clean_power >= car.clean_mark:
            price = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return price
        else:
            return 0

    def rate_service(self, mark: int) -> None:
        future_average_rating = (((self.average_rating
                                  * self.count_of_ratings)
                                 + mark)
                                 / (self.count_of_ratings
                                    + 1))
        self.count_of_ratings = self.count_of_ratings + 1
        self.average_rating = round(future_average_rating, 1)
