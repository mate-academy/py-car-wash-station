class Car:

    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand

class CarWashStation:

    def __init__(self, distance_from_city_center: float, clean_power: int,
        average_raiting: float, count_of_raitings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_raiting = round(average_raiting, 1)
        self.count_of_raitings = count_of_raitings

    def serve_cars(self, cars: list) -> int:
        result = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                result += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return result

    def rate_service(self, num):
        self.average_raiting = (round(((self.average_raiting * 
        self.count_of_raitings) + num) / (self.count_of_raitings +1)))

    def calculate_washing_price(self, car: Car) -> float:
        price = (car.comfort_class * (self.clean_power - car.clean_mark) *
                (self.average_raiting / self.distance_from_city_center))
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power
