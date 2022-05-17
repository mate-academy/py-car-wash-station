class Car:
    comfort_class: int
    clean_mark: int
    brand: str

    def __init__(self, c_class: int, c_mark: int, car_brand: str):
        self.comfort_class = c_class
        self.clean_mark = c_mark
        self.brand = car_brand


class CarWashStation:
    distance_from_city_center: float
    clean_power: int
    average_rating: float
    count_of_ratings: int

    def __init__(self, distance: float, c_power: int,
                 rating: float, count_of_votes: int):
        self.distance_from_city_center = distance
        self.clean_power = c_power
        self.average_rating = rating
        self.count_of_ratings = count_of_votes

    def serve_cars(self, washes: list) -> float:
        def calculation(car):
            result = self.calculate_washing_price(car)
            self.wash_single_car(car)
            return result

        return sum(calculation(car) for car in washes
                   if self.clean_power > car.clean_mark)

    def calculate_washing_price(self, car: Car):
        return round(car.comfort_class * (
                     self.clean_power - car.clean_mark) * (
                     self.average_rating / self.distance_from_city_center), 1)

    def wash_single_car(self, car: Car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power
        return car

    def rate_service(self, vote: int):
        vt = round((self.average_rating * self.count_of_ratings + vote
                    ) / (self.count_of_ratings + 1), 1)
        self.average_rating = round(vt, 1)
        self.count_of_ratings += 1
