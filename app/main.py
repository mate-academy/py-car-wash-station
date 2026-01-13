class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, min_class: int, clear_power: int, average_rating: float, count_of_ratings: int):
        self.min_class = min_class
        self.clear_power = clear_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        total_income = 0.0
        for car in cars:
            if car.comfort_class >= self.min_class:
                price = self.wash_single_car(car)
                total_income += price
        return round(total_income, 1)

    def wash_single_car(self, car: Car) -> float:
        price = self.calculate_washing_price(car)
        if car.clean_mark < self.clear_power:
            car.clean_mark = self.clear_power
        return price

    def calculate_washing_price(self, car: Car) -> float:
        if car.clean_mark >= self.clear_power:
            return 0.0
        # Ціна = (clear_power - clean_mark) * 2
        return round((self.clear_power - car.clean_mark) * 2, 1)

    def rate_service(self, mark: int):
        total = self.average_rating * self.count_of_ratings + mark
        self.count_of_ratings += 1
        self.average_rating = round(total / self.count_of_ratings, 1)
