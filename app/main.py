class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        if all([1 <= comfort_class <= 7, 1 <= clean_mark <= 10]):
            self.comfort_class = comfort_class
            self.clean_mark = clean_mark
            self.brand = brand


class CarWashStation:
    def __init__(self, distance_of_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        if all([1 <= distance_of_city_center <= 10,
                1 <= clean_power <= 10,
                1 <= average_rating <= 5]):
            self.distance_of_city_center = distance_of_city_center
            self.clean_power = clean_power
            self.average_rating = round(average_rating, 1)
            self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car: Car) -> float:
        return round(car.comfort_class
                     * (self.clean_power - car.clean_mark)
                     * self.average_rating
                     / self.distance_of_city_center, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        sum_of_rates = self.count_of_ratings * self.average_rating + rate
        self.count_of_ratings += 1
        self.average_rating = round(sum_of_rates / self.count_of_ratings, 1)
