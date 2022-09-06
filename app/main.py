class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str
                 ):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int
                 ):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list):
        total_cost = 0
        for car in cars:
            if self.clean_power > car.clean_mark:
                total_cost += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(total_cost, 1)

    def calculate_washing_price(self, car):
        dif = self.clean_power - car.clean_mark
        div = self.average_rating / self.distance_from_city_center
        single_car_cost = car.comfort_class * dif * div
        return round(single_car_cost, 1)

    def wash_single_car(self, car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, mark):
        multiply = (self.count_of_ratings * self.average_rating + mark)
        self.average_rating = round(multiply / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
