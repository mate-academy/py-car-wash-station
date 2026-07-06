class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand

class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int, average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        return round(
            (car.comfort_class
             * (self.clean_power - car.clean_mark)
             * self.average_rating)
            / self.distance_from_city_center,
            1
        )

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power
        return

# rate_service - method that adds a single rate to the wash station,
# and based on this single rate average_rating and count_of_ratings should be changed:

    def rate_service(self, rate: int) -> None:
        self.average_rating = round((self.average_rating * self.count_of_ratings + rate) / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1

    # serve_cars - method, that takes a list of Car's, washes only
    # cars with clean_mark < clean_power of wash station and returns income
    # of CarWashStation for serving this list of Car's, rounded to 1 decimal:

    def serve_cars(self, cars: list[Car]) -> float:
        filtered_cars = [car for car in cars if car.clean_mark < self.clean_power]
        income = 0.0
        for car in filtered_cars:
            self.wash_single_car(car)
            income += self.calculate_washing_price(car)
        return income