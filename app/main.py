class Car:
    def __init__(
            self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self, distance_from_city_center: float, clean_power: int,
            average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, list_of_cars: list) -> float:
        count = float()
        for car in list_of_cars:
            count += self.wash_single_car(car)
        return count

    def calculate_washing_price(self, car: Car) -> float:
        return round(
            (car.comfort_class * (self.clean_power - car.clean_mark)
             * self.average_rating / self.distance_from_city_center), 1
        )

    def wash_single_car(self, car: Car) -> float:
        count = float()
        if car.clean_mark < self.clean_power:
            count = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
        return count

    def rate_service(self, rate: int) -> None:
        self.average_rating = round(
            (rate + self.average_rating * self.count_of_ratings)
            / (self.count_of_ratings + 1), 1
        )
        self.count_of_ratings += 1
