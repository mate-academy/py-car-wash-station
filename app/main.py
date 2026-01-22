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
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0.0
        for i in range(len(cars)):
            if cars[i].clean_mark <= self.clean_power:
                income += self.calculate_washing_price(cars[i])
                self.wash_single_car(cars[i])
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        if self.distance_from_city_center == 0:
            return 0

        clean_diff = self.clean_power - car.clean_mark
        clean_eff = car.comfort_class * clean_diff * self.average_rating
        inc = clean_eff / self.distance_from_city_center
        return inc

    def wash_single_car(self, car: Car) -> Car:
        car.clean_mark = self.clean_power
        return car

    def rate_service(self, number: int) -> None:
        new_total_rating = self.average_rating * self.count_of_ratings + number
        new_rating = round(
            new_total_rating / (self.count_of_ratings + 1),
            1
        )
        self.average_rating = new_rating
        self.count_of_ratings += 1
