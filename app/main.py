class Car:
    def __init__(self, comfort_class: int, clean_mark: int,
                 brand: str) -> None:
        self.brand = brand
        if comfort_class not in range(1, 8):
            raise ValueError("Car comfort class must be an int from 1 to 7")
        self.comfort_class = comfort_class
        if clean_mark not in range(1, 11):
            raise ValueError("Car cleanness mark must be an int from 1 to 10")
        self.clean_mark = clean_mark


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        if not 1.0 <= distance_from_city_center <= 10.0:
            raise ValueError("Distance from city center must be from 1 to 10")
        self.distance_from_city_center = distance_from_city_center
        if clean_power not in range(1, 11):
            raise ValueError("Station power must be an int from 1 to 10")
        self.clean_power = clean_power
        if not 1.0 <= average_rating <= 5.0:
            raise ValueError("An average rating must be from 1 to 5")
        self.average_rating = average_rating
        if not count_of_ratings >= 0:
            raise ValueError("The amount of rating cannot be negative")
        self.count_of_ratings = count_of_ratings

    def serve_single_car(self, car: Car) -> float:
        price = self.calculate_washing_price(car)
        self.wash_single_car(car)
        return price

    def serve_cars(self, cars: list) -> float:
        return round(sum([
            self.serve_single_car(car)
            for car in cars
            if car.clean_mark < self.clean_power
        ]), 1)

    def calculate_washing_price(self, car: Car) -> float:
        return round(round(
            car.comfort_class * (self.clean_power - car.clean_mark)
            * self.average_rating / self.distance_from_city_center, 10), 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        self.average_rating = round(round(
            (self.average_rating * self.count_of_ratings + rate)
            / (self.count_of_ratings + 1), 10), 1)
        self.count_of_ratings += 1
