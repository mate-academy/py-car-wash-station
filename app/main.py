class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        income = []
        for car in cars:
            income.append(self.wash_single_car(car))
        return sum(income)

    def calculate_washing_price(self, car: list) -> float:
        price = (car.comfort_class
                 * (self.clean_power - car.clean_mark)
                 * self.average_rating
                 / self.distance_from_city_center)
        return round(price, 1)

    def wash_single_car(self, car: list) -> float:
        single_car_price = 0
        if car.clean_mark < self.clean_power:
            single_car_price = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
        return single_car_price

    def rate_service(self, rate: int):
        self.average_rating = (round((self.count_of_ratings
                                      / (self.count_of_ratings + 1)
                                      * self.average_rating + 1
                                      / (self.count_of_ratings + 1) * rate)
                                     , 1))
        self.count_of_ratings += 1
