class Car:
    def __init__(self, comfort_class: int, clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class          # value from 1 to 7
        self.clean_mark = clean_mark                # value from 1 to 10
        self.brand = brand                          # brand name


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        # value from 1.0 to 10.0
        self.clean_power = clean_power              # value from 1 to 10
        self.average_rating = average_rating        # value from 1.0 to 5.0
        self.count_of_ratings = count_of_ratings    # integer count of ratings

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car: Car) -> float:
        return round(car.comfort_class * (self.clean_power - car.clean_mark)
                     * self.average_rating / self.distance_from_city_center, 1)

    def wash_single_car(self, car: Car) -> float:
        income = self.calculate_washing_price(car)
        car.clean_mark = self.clean_power
        return income

    def rate_service(self, rate: int) -> None:
        rating = self.average_rating * self.count_of_ratings + rate
        self.count_of_ratings += 1
        self.average_rating = round(rating / self.count_of_ratings, 1)
