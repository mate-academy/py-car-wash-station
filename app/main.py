class Car:
    # write your code here
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    # write your code here
    def __init__(self, distance_from_city_center: float,
                 clean_power: int, average_rating: float,
                 count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars):
        sum_price = 0
        for car in cars:
            if self.clean_power > car.clean_mark:
                sum_price += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return sum_price

    def calculate_washing_price(self, car):
        dif = self.clean_power - car.clean_mark
        class_rating = car.comfort_class * self.average_rating
        calc_wash_price = class_rating * dif / self.distance_from_city_center
        return round(calc_wash_price, 1)

    def wash_single_car(self, car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rate):
        new_rate = self.average_rating * self.count_of_ratings + rate
        self.count_of_ratings += 1
        self.average_rating = round(new_rate / self.count_of_ratings, 1)
