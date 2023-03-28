class Car:

    def __init__(self, comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:

    def __init__(
            self, distance_from_city_center: (int or float), clean_power: int,
            average_rating: float, count_of_ratings: int
    ) -> None:

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        cost = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                cost += self.calculate_washing_price(car)
                car.clean_mark = self.wash_single_car(car)
        return round(cost, 1)

    def calculate_washing_price(self, car: object) -> float:

        return (car.comfort_class
                * (self.clean_power - car.clean_mark)
                * self.average_rating
                / self.distance_from_city_center)

    def wash_single_car(self, car: object) -> object:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power
        return car.clean_mark

    def rate_service(self, single_rate: int) -> None:

        new_sum_of_rate = (self.average_rating
                           * self.count_of_ratings
                           + single_rate)
        self.count_of_ratings += 1
        self.average_rating = round(new_sum_of_rate / self.count_of_ratings, 1)
