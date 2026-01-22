class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, clear_power: int, max_class: int,
                 average_rating: float, count_of_ratings: int) -> None:
        self.clear_power = clear_power
        self.max_class = max_class
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        if car.comfort_class > self.max_class:
            return 0.0
        if car.clean_mark >= self.clear_power:
            return 0.0
        return (self.clear_power - car.clean_mark) * 2

    def wash_single_car(self, car: Car) -> float:
        if car.comfort_class > self.max_class:
            return 0.0
        if car.clean_mark < self.clear_power:
            cost = (self.clear_power - car.clean_mark) * 2
            car.clean_mark = self.clear_power
            return cost
        return 0.0

    def serve_cars(self, cars: list[Car]) -> float:
        total_income = 0.0
        for car in cars:
            if car.comfort_class <= self.max_class and car.clean_mark < self.clear_power:
                total_income += (self.clear_power - car.clean_mark) * 2
                car.clean_mark = self.clear_power
        return total_income

    def rate_service(self, mark: int) -> None:
        total_score = self.average_rating * self.count_of_ratings + mark
        self.count_of_ratings += 1
        self.average_rating = total_score / self.count_of_ratings
