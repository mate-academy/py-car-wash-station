class Car:
    def __init__(self, comfort: int, clean: int, brand: str) -> None:
        self.comfort_class = comfort
        self.clean_mark = clean
        self.brand = brand


class CarWashStation:
    def __init__(self, dist: int, power: int, mark: float, count: int) -> None:
        self.distance_from_city_center = dist
        self.clean_power = power
        self.average_rating = mark
        self.count_of_ratings = count

    def calculate_washing_price(self, car: Car) -> float:
        if self.distance_from_city_center != 0:
            first = car.comfort_class * (self.clean_power - car.clean_mark)
            second = self.distance_from_city_center
            return round(first * self.average_rating / second, 1)
        else:
            return 0.0

    def serve_cars(self, cars: list) -> float:
        res = []
        for car in cars:
            if car.clean_mark < self.clean_power:
                res.append(self.calculate_washing_price(car))
                self.wash_single_car(car)

        return sum(res)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, mark: int) -> None:
        first = (self.average_rating * self.count_of_ratings + mark)
        second = (self.count_of_ratings + 1)
        new_mark = round(first / second, 1)
        self.average_rating = new_mark
        self.count_of_ratings += 1
