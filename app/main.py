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
                 distance_from_city_center: int,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def calculate_washing_price(self, car: Car) -> float:
        cleanness_difference = self.clean_power - car.clean_mark
        price = (car.comfort_class
                 * cleanness_difference
                 * self.average_rating
                 / self.distance_from_city_center)
        return round(price, 1)

    def serve_cars(self, cars: list) -> float:
        total_price = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                total_price += self.calculate_washing_price(car)
                self.wash_single_car(car)
            else:
                pass
        return total_price

    def rate_service(self, rate: float) -> None:
        new_sum_rating = self.average_rating * self.count_of_ratings + rate
        self.count_of_ratings = self.count_of_ratings + 1
        self.average_rating = round(new_sum_rating / self.count_of_ratings, 1)
