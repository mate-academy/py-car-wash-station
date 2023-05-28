class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str
                 ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int
                 ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> int:

        income_calculator = 0

        for car in cars:
            if car.clean_mark < self.clean_power:
                income_calculator += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return round(income_calculator, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def calculate_washing_price(self, car: Car) -> float:

        cleanliness = self.clean_power - car.clean_mark
        prestige = self.average_rating / self.distance_from_city_center

        return car.comfort_class * cleanliness * prestige

    def rate_service(self, rate: int) -> None:

        sum_of_old_rating = self.average_rating * self.count_of_ratings
        sum_of_new_rating = sum_of_old_rating + rate

        self.count_of_ratings += 1

        self.average_rating = round(
            sum_of_new_rating / self.count_of_ratings, 1
        )
