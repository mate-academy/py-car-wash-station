class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand

class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int, average_rating: int, count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, auto: Car) -> float:
        diff = self.clean_power - auto.clean_mark
        price = auto.comfort_class * diff * self.average_rating / self.distance_from_city_center
        return round(price, 1)

    def wash_single_car(self, auto: Car) -> None:
        auto.clean_mark = self.clean_power

    def rate_service(self, rating: int) -> None:
        new_rating = (self.average_rating * self.count_of_ratings + rating)/ (self.count_of_ratings + 1)
        self.average_rating = round(new_rating, 1)
        self.count_of_ratings += 1

    def serve_cars(self, cars: list) -> float:
        income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return income
