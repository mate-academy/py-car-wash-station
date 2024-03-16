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
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        return round(sum([self.wash_single_car(car) for car in cars if
                          (car.clean_mark < self.clean_power)]), 1)

    def calculate_washing_price(self, car: Car) -> float:
        # method, that calculates cost for a single car wash
        return round(car.comfort_class
                     * (self.clean_power - car.clean_mark)
                     * self.average_rating
                     / self.distance_from_city_center, 1)

    def wash_single_car(self, car: Car) -> float:
        cost = self.calculate_washing_price(car)
        car.clean_mark = self.clean_power
        print(f"{car.brand} cleaned and clean mark is: {car.clean_mark}")
        return cost

    def rate_service(self, score: int) -> None:
        sum_rating = (self.average_rating * self.count_of_ratings) + score
        self.count_of_ratings += 1
        self.average_rating = round(sum_rating / self.count_of_ratings, 1)
        print(f"Our rating changed on {self.average_rating}")
