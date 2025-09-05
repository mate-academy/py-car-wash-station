class Car:
    # write your code here
<<<<<<< HEAD
    pass
=======
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand
>>>>>>> f1b8e53de428f5f6ac6f56e72fbe58c8645d251c


class CarWashStation:
    # write your code here
<<<<<<< HEAD
    pass
=======
    def __init__(self, distance_from_city_center: float, clean_power: int, average_rating: float, count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        total_income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                total_income += self.wash_single_car(car)
        return round(total_income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        return round(car.comfort_class * (self.clean_power - car.clean_mark) * self.average_rating / self.distance_from_city_center, 1)

    def wash_single_car(self, car: Car) -> float:
        price = self.calculate_washing_price(car)
        car.clean_mark = self.clean_power
        return price

    def rate_service(self, new: float) -> None:
        self.average_rating = round((self.average_rating * self.count_of_ratings + new) / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
>>>>>>> f1b8e53de428f5f6ac6f56e72fbe58c8645d251c
