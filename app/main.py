class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:
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

    def serve_cars(self, cars: list[Car]) -> float:
        washing_price = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                washing_price += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return washing_price

    def calculate_washing_price(self, car: Car) -> float:
        rate = self.average_rating
        distance = self.distance_from_city_center
        comfort = car.comfort_class

        difference_station_car = self.clean_power - car.clean_mark
        rate_divided_dist = rate / distance

        return round(comfort * difference_station_car * rate_divided_dist, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        sum_of_rate = self.average_rating * self.count_of_ratings + rate
        self.count_of_ratings += 1
        self.average_rating = round(sum_of_rate / self.count_of_ratings, 1)
