class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def rate_service(self, new_rate: int) -> None:
        new_average = (self.average_rating
                       * self.count_of_ratings
                       + new_rate) / (self.count_of_ratings + 1)
        self.count_of_ratings += 1
        self.average_rating = round(new_average, 1)

    def wash_single_car(self, car: Car) -> int:
        result = 0
        if car.clean_mark < self.clean_power:
            result += self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return round(result, 1)

    def calculate_washing_price(self, car: Car) -> int:
        return round(car.comfort_class
                     * (self.clean_power - car.clean_mark)
                     * self.average_rating
                     / self.distance_from_city_center, 1)

    def serve_cars(self, car_list: list):
        income = 0
        for car in car_list:
            result = self.wash_single_car(car)
            if result is not None:
                income += result
        return round(income, 1)
