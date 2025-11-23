class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: float, average_rating: float, count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car):
        price = ((car.clean_power - car.clean_mark) * (1 + car.comfort_class / 10) * (car.average_rating)) / car.distance_from_city_center)
        return price

    def serve_cars(self, Cars: list):
        total_income = 0
        for car in Cars:
            if car.clean_mark < self.clean_power:
                total_income += self.calculate_wash_price(car)
                return round(total_income)

    def wash_single_car(self, car: car)
        if car.clean_mark < self.clean_power:
            car_clean_mark = self.clean_power

    def rate_service(self, rate: int):
        self.count_of_ratings += 1
        self.average_rating = (self.average_rating + rate) / self.count_of_rating
        return self.average_rating and self.count_of_ratings