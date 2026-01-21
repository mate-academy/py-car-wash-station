class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:

        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float,
                 clean_power: int, average_rating: float,
                 count_of_ratings: int) -> None:

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        result = 0
        for car in cars:
            result += self.calculate_washing_price(car)
            self.wash_single_car(car)
        return result

    def calculate_washing_price(self, car: Car) -> float:
        if car.clean_mark >= self.clean_power:
            return 0
        result = (car.comfort_class * (self.clean_power - car.clean_mark)
                  * self.average_rating
                  / self.distance_from_city_center)
        result = round(result, 1)
        return result

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: float) -> None:
        self.average_rating = ((self.average_rating * self.count_of_ratings
                                + rate)
                               / (self.count_of_ratings + 1))
        self.count_of_ratings = self.count_of_ratings + 1
        self.average_rating = round(self.average_rating, 1)
