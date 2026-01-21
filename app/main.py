class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: int,
                 clean_power: int, average_rating: int,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        cars_washed = []
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                cars_washed.append(car)
        for car_washed in cars_washed:
            income += self.calculate_washing_price(car_washed)
            self.wash_single_car(car_washed)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        return round(
            (car.comfort_class * (self.clean_power - car.clean_mark)
             * self.average_rating / self.distance_from_city_center),
            1)

    def wash_single_car(self, car: Car) -> int:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power
            return car.clean_mark

    def rate_service(self, num: int) -> None:
        self.average_rating = round(
            (((self.average_rating * self.count_of_ratings) + num)
             / (self.count_of_ratings + 1)), 1)
        self.count_of_ratings += 1
