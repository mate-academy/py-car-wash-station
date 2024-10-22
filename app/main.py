class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power= clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings


    def serve_cars(self, cars: list) -> list:
        served_cars = []
        for car in cars:
            if car.clean_mark < self.clean_power:
                served_cars.append(car)
        for car in served_cars:
            self.wash_single_car(car)
        return served_cars
    def wash_single_car(self, car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def calculate_washing_price(self, cars: list) -> float:
        price = []
        served_cars = self.serve_cars(cars)
        if served_cars:
            for car in served_cars:
               washing_price = round(car.comfort_class * (self.clean_power - (car.clean_mark * self.average_rating / self.distance_from_city_center)), 1)
               price.append(washing_price)
            income = round((sum(list(price))), 1)
            return income
        else:
            return 0

    def rate_service(self, rate: float):
        sum_of_rates = self.count_of_ratings * self.average_rating
        self.count_of_ratings += 1
        self.average_rating = round(((sum_of_rates + rate) / self.count_of_ratings), 1)

