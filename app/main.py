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

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0

        cars = [car for car in cars if car.clean_mark < self.clean_power]

        for car in cars:
            income += self.calculate_washing_price(car)
            self.wash_single_car(car)

        return round(income, 2)

    def calculate_washing_price(self, car: Car) -> float:
        clean_diff = (self.clean_power - car.clean_mark)
        comfort = car.comfort_class
        rating = self.average_rating
        income = comfort * clean_diff * rating / self.distance_from_city_center
        return round(income, 2)

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        rating = self.average_rating
        count = self.count_of_ratings
        self.average_rating = round((rating * count + rate) / (count + 1), 1)
        self.count_of_ratings += 1
