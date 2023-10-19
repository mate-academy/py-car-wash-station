class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center, clean_power, average_rating, count_of_ratings):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings
        self.income = 0

    def calculate_washing_price(self, car: Car) -> int:
        washing_price = car.comfort_class * (self.clean_power - car.clean_mark) * \
                        (self.average_rating / self.distance_from_city_center)
        return washing_price

    def wash_single_car(self, car):
        car.clean_mark = self.clean_power

    def serve_cars(self, car_list):
        income = 0.0
        for car in car_list:
            if car.clean_mark < self.clean_power:
                income += CarWashStation.calculate_washing_price(self, car)
                CarWashStation.wash_single_car(self, car)
        self.income = income
        return round(income, 1)

    def rate_service(self, rating):
        total_rating = self.average_rating * self.count_of_ratings
        total_rating += rating
        self.count_of_ratings += 1
        self.average_rating = total_rating / self.count_of_ratings
        self.average_rating = round(self.average_rating, 1)
