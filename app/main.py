class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        total_rating = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        total_rating += rate
        self.average_rating = round(total_rating / self.count_of_ratings, 1)

    def calculate_washing_price(self, car: Car) -> float:
        clean_diff = self.clean_power - car.clean_mark
        return round(car.comfort_class * clean_diff * self.average_rating
                     / self.distance_from_city_center, 1)

    def serve_cars(self, cars: list) -> float:
        total_cost = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                total_cost += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return total_cost
