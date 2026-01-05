class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
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

    def calculate_washing_price(self, car: Car) -> float:
        diff = self.clean_power - car.clean_mark
        cost = car.comfort_class * diff * self.average_rating
        cost = cost / self.distance_from_city_center
        cost = round(cost, 1)
        return cost

    def wash_single_car(self, single_car: Car) -> None:
        if single_car.clean_mark < self.clean_power:
            single_car.clean_mark = self.clean_power

    def rate_service(self, rating: int) -> None:
        total = self.count_of_ratings * self.average_rating + rating
        self.count_of_ratings += 1
        self.average_rating = round(total / self.count_of_ratings , 1)

    def serve_cars(self, cars: list) -> float:
        total_cost = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                total_cost += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(total_cost, 1)
