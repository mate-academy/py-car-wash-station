class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int
                 ):
        self.count_of_ratings = count_of_ratings
        self.average_rating = average_rating
        self.clean_power = clean_power
        self.distance_from_city_center = distance_from_city_center

    def serve_cars(self, cars):
        total_cost = []
        for car in cars:
            if car.clean_mark < self.clean_power:
                total_cost.append(self.calculate_washing_price(car))
                self.wash_single_car(car)
        return sum(total_cost)

    def calculate_washing_price(self, car):
        return round((car.comfort_class * (
            self.clean_power - car.clean_mark
        )) * (self.average_rating / self.distance_from_city_center), 1)

    def wash_single_car(self, car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rate):
        recount_all = self.average_rating * self.count_of_ratings + rate
        self.count_of_ratings += 1
        self.average_rating = round(recount_all / self.count_of_ratings, 1)
