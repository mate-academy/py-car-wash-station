class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
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

    def serve_cars(self, list_of_cars: list) -> float:
        total_income = 0
        for car in list_of_cars:
            if car.clean_mark < self.clean_power:
                current_income = self.calculate_washing_price(car)
                self.wash_single_car(car)
                total_income += current_income
        return total_income

    def calculate_washing_price(self, car: Car) -> float:
        washing_price = (car.comfort_class
                         * (self.clean_power - car.clean_mark)
                         * self.average_rating
                         / self.distance_from_city_center)
        return round(washing_price, 1)

    def wash_single_car(self, car: Car) -> int:
        car.clean_mark = self.clean_power
        return car.clean_mark

    def rate_service(self, rate: int) -> float:
        new_rate = ((self.average_rating
                     * self.count_of_ratings + rate)
                    / (self.count_of_ratings + 1))
        self.average_rating = round(new_rate, 1)
        self.count_of_ratings += 1
        return self.average_rating
