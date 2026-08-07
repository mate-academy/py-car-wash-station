class Car:
    def __init__(
            self, comfort_class: int, clean_mark: int, brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self, distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars_list: list) -> float:
        income = []
        for car in cars_list:
            if car.clean_mark < self.clean_power:
                income.append(self.calculate_washing_price(car))
                self.wash_single_car(car)
        return round(sum(income), 1)

    def calculate_washing_price(self, car: Car) -> float:
        clean_difference = self.clean_power - car.clean_mark
        coefficient = clean_difference * self.average_rating
        distance_rate = coefficient / self.distance_from_city_center
        income = round(car.comfort_class * distance_rate, 1)
        return income

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        sum_of_ratings = self.average_rating * self.count_of_ratings
        new_average = (sum_of_ratings + rate) / (self.count_of_ratings + 1)
        self.average_rating = round(new_average, 1)
        self.count_of_ratings = self.count_of_ratings + 1
