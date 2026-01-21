class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power, average_rating: float, count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        return round((car.comfort_class * (self.clean_power - car.clean_mark)
                      * (self.average_rating / self.distance_from_city_center)), 1)

    def wash_single_car(self, car: Car) -> bool:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power
            return True
        return False

    def rate_service(self, rate: float):
        self.count_of_ratings += 1
        self.average_rating = ((self.average_rating * (self.count_of_ratings - 1)) + rate) / self.count_of_ratings
        self.average_rating = round(self.average_rating, 1)

    def serve_cars(self, car_list: list) -> float:
        income = 0
        for car in car_list:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return round(income, 1)
