class Car:
    def __init__(self, comfort_class: int, clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: int, clean_power: int,
                 average_rating: int, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings
        self.income = 0

    def serve_cars(self, cars: list) -> int:
        for car in cars:
            if car.clean_mark < self.clean_power:
                self.income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        print(self.income)
        print("testtest")
        return self.income

    def calculate_washing_price(self, car: object) -> None:
        return round(car.comfort_class * (self.clean_power
                                          - car.clean_mark)
                     * self.average_rating
                     / self.distance_from_city_center, 1)

    def wash_single_car(self, car: list) -> None:
        car.clean_mark = self.clean_power

    def rate_service(self, rating: bool) -> None:
        total_score = self.average_rating * self.count_of_ratings + rating
        self.count_of_ratings += 1
        self.average_rating = round(total_score / self.count_of_ratings, 1)
