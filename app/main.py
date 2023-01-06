class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int,
                 brand: str
                 ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: int,
                 clean_power: int,
                 average_rating: int,
                 count_of_ratings: int
                 ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        income = 0
        for i in cars:
            if i.clean_mark < self.clean_power:
                income += round(self.calculate_washing_price(i), 1)
                i.clean_mark = self.wash_single_car(i)
        return income

    def calculate_washing_price(self, car: Car) -> float:
        count = (car.comfort_class * (self.clean_power - car.clean_mark)
                 * self.average_rating) / self.distance_from_city_center
        return count

    def wash_single_car(self, car: Car) -> float:
        return self.clean_power

    def rate_service(self, rate: float) -> float:
        self.count_of_ratings = self.count_of_ratings + 1
        changed_count_of_rating = self.count_of_ratings + 1
        self.average_rating = round((self.count_of_ratings
                                     * self.average_rating
                                     + rate) / changed_count_of_rating, 1)
        return self.count_of_ratings, self.average_rating
