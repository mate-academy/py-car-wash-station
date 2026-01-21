class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:

    def __init__(self,
                 distance_from_city_center,
                 clean_power,
                 average_rating,
                 count_of_ratings):

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        cars_can_wash = [car for car in cars
                         if car.clean_mark < self.clean_power]
        income = [self.calculate_washing_price(car) for car in cars_can_wash]

        for car in cars_can_wash:
            self.wash_single_car(car)

        return sum(income)

    def calculate_washing_price(self, car: Car) -> float:
        station_coef = self.average_rating / self.distance_from_city_center
        clean_diff = self.clean_power - car.clean_mark
        cost = car.comfort_class * clean_diff * station_coef
        return round(cost, 1)

    def wash_single_car(self, car: Car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, add_rate: int):
        total_rates = self.average_rating * self.count_of_ratings
        new_avg_rate = (total_rates + add_rate) / (self.count_of_ratings + 1)
        self.average_rating = round(new_avg_rate, 1)
        self.count_of_ratings += 1
