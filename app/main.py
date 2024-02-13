class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        self.distance_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        total_cost = 0
        for car in cars:
            total_cost += self.calculate_washing_price(car)
            self.wash_single_car(car)
        return total_cost

    def calculate_washing_price(self, car: Car) -> float:
        income = 0
        if self.clean_power > car.clean_mark:
            income = round(car.comfort_class
                           * (self.clean_power - car.clean_mark)
                           * self.average_rating / self.distance_center, 1)
        return income

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, number: float) -> None:
        if number > 5 or number < 1:
            print("need number from 1 to 5")
        self.average_rating = round(((self.average_rating
                                    * self.count_of_ratings) + number)
                                    / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
