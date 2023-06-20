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

    def serve_cars(self, cars: list[Car]) -> int:
        return sum(self.wash_single_car(car) for car in cars)

    def calculate_washing_price(self, car: Car) -> float:
        difference = self.clean_power - car.clean_mark
        rating_distance = self.average_rating / self.distance_from_city_center
        return car.comfort_class * difference * rating_distance

    def wash_single_car(self, car: Car) -> int | float:
        serve_car_income = 0
        if car.clean_mark < self.clean_power:
            serve_car_income += self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
        return round(serve_car_income, 1)

    def rate_service(self, new_rate: int | float) -> None:
        current_rite, ratings_count = self.average_rating, self.count_of_ratings
        new_average = ((current_rite * ratings_count) + new_rate) / (ratings_count + 1)
        self.average_rating = round(new_average, 1)
        self.count_of_ratings += 1
