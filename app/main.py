class Car:
    def __init__(self, comfort: int, mark: int, brand: str) -> None:
        self.comfort_class = comfort
        self.clean_mark = mark
        self.brand = brand


class CarWashStation:
    def __init__(self, dist: float, pwr: int, rate: float, count: int) -> None:
        self.distance_from_city_center = dist
        self.clean_power = pwr
        self.average_rating = rate
        self.count_of_ratings = count

    def serve_cars(self, cars: list) -> float:
        income = 0
        for car in cars:
            if self.clean_power > car.clean_mark:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car: Car) -> float:
        wash = car.comfort_class * (self.clean_power - car.clean_mark)
        for_count = wash * self.average_rating
        washing_price = for_count / self.distance_from_city_center
        return round(washing_price, 1)

    def wash_single_car(self, car: Car) -> Car:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power
            return car

    def rate_service(self, mark: int) -> None:
        self.count_of_ratings += 1
        self.average_rating = round(
            (((self.average_rating * (self.count_of_ratings - 1)) + mark)
             / self.count_of_ratings), 1)
