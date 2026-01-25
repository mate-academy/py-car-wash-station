class Car:
    def __init__(
        self,
        comfort_class: int,
        clean_mark: int,
        brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        incomes = []
        for car in cars:
            incomes.append(self.wash_single_car(car))
        return round(sum(incomes), 1)

    def wash_single_car(self, car: Car) -> float:
        if car.clean_mark < self.clean_power:
            washing_price = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return washing_price
        return 0.0

    def calculate_washing_price(self, car: Car) -> float:
        center_variable = self.average_rating / self.distance_from_city_center
        car_variable = car.comfort_class * (self.clean_power - car.clean_mark)
        return round(car_variable * center_variable, 1)

    def rate_service(self, new_rating: float) -> None:
        total_rating = self.average_rating * self.count_of_ratings
        total_rating += new_rating
        self.count_of_ratings += 1
        self.average_rating = round(total_rating / self.count_of_ratings, 1)
