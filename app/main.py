class Car:
    # write your code here
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand
    # def serve_cars(self):
class CarWashStation:
    # write your code here
    def __init__(self, distance_from_city_center: int, clean_power: int, average_rating: int, count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings
    def serve_cars(self, cars):
        total_wash = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                self.wash_single_car(car)
                total_wash += self.calculate_washing_price(car)
        return total_wash
    def calculate_washing_price(self, car):
        if self.clean_power > car.clean_mark:
            return round(car.comfort_class * (
                    self.clean_power - car.clean_mark) * self.average_rating / self.distance_from_city_center,
                         1)
    def wash_single_car(self, car: Car):
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power
            # return car.clean_mark
    def rate_service(self, car: Car):
        if car.clean_mark < self.clean_power:
            self.average_rating += 1
            self.count_of_ratings += 1
            # return self.average_rating, self.count_of_ratings

