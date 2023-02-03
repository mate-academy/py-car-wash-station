

class Car:
    def __init__(self, comfort_class: int, clean_mark: int,
                 brand: str) -> None:

        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center : int, clean_power: int,
                 average_rating: int, count_of_ratings: int) -> None:

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        income = 0
        for car in cars:
            if car.clean_mark <= self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car: Car) -> float:
        diff_clean_power = self.clean_power - car.clean_mark
        wash_price_wo_city_center = (car.comfort_class
                                     * diff_clean_power
                                     * self.average_rating)
        washing_price_with_cc = (wash_price_wo_city_center
                                 / self.distance_from_city_center)
        return round(washing_price_with_cc, 1)

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def rate_service(self, rating: int) -> None:
        self.average_rating = round(self.count_average_rating(rating), 1)
        self.count_of_ratings += 1

    def count_average_rating(self, rating: int) -> float:
        rating_overall = self.average_rating * self.count_of_ratings + rating
        average_rating_float = rating_overall / (self.count_of_ratings + 1)
        return average_rating_float
