

class Car:
    def __init__(
            self,
            comfort_class: int | float,
            clean_mark: int | float,
            brand: str,
    ) -> None:

        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: int | float,
            clean_power: int,
            average_rating: int | float,
            count_of_ratings: int,
    ) -> None:

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0
        for car in cars:
            if self.clean_power >= car.clean_mark:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car: Car) -> float:
        diff_clean_power = self.clean_power - car.clean_mark
        washing_price = ((car.comfort_class
                          * diff_clean_power
                          * self.average_rating)
                         / self.distance_from_city_center)

        return round(washing_price, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark <= self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: int) -> None:
        self.average_rating = round(self.count_average_rating(rating), 1)
        self.count_of_ratings += 1

    def count_average_rating(self, rating: int) -> float:
        rating_overall = self.average_rating * self.count_of_ratings + rating
        average_rating_float = rating_overall / (self.count_of_ratings + 1)
        return average_rating_float
