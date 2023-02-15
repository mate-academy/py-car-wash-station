class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand

class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int, average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, list_cars: list):
        result = 0
        for car in list_cars:
            if car.clean_mark < self.clean_power:
                self.wash_single_car(car)
                result += self.calculate_washing_price(car)
        return result

    def calculate_washing_price(self, car: Car):
        price = (car.comfort_class * (self.clean_power - car.clean_mark) * self.average_rating / self.distance_from_city_center)
        return round(price)

    def wash_single_car(self, car: Car):
        car.clean_mark = self.clean_power

    def rate_service(self, rate: int):
        return round((self.average_rating * self.count_of_ratings + rate) / (self.count_of_ratings + 1), 1)