class Car:
    def __init__(self, comfort_class : int, clean_mark: int, brand: str):
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

    def serve_cars(self, cars_list):
        total_cost = 0
        for car in cars_list:
            if car.clean_mark < self.clean_power:
                total_cost += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return total_cost

    def calculate_washing_price(self, car):
        diff = self.clean_power - car.clean_mark
        mult = car.comfort_class * self.average_rating
        price = mult * diff / self.distance_from_city_center
        return round(price, 1)

    def wash_single_car(self, car):
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, mark):
        marks = self.average_rating * self.count_of_ratings + mark
        self.average_rating = round(marks / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
