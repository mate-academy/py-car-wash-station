class Car:
    def __init__(self,
                 comfort_class: str,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: int,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        washed_cars = []
        income = 0

        for car in cars:
            if car.clean_mark < self.clean_power:
                washed_cars.append(car)
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return round(income, 1)

    def calculate_washing_price(self, car: str) -> float:
        car_points = car.comfort_class * (self.clean_power - car.clean_mark)
        car_rate = self.average_rating / self.distance_from_city_center
        return round(car_points * car_rate, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: int) -> None:
        self.count_of_ratings += 1
        new_average = (self.average_rating
                       * (self.count_of_ratings - 1)
                       + rating) / self.count_of_ratings
        self.average_rating = round(new_average, 1)
