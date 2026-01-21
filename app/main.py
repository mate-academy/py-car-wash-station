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
    def serve_cars(self, cars):
        profit_from_washing = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                profit_from_washing += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(profit_from_washing, 1)
    def calculate_washing_price(self, car):
        price_of_washing = (car.comfort_class * (self.clean_power - car.clean_mark) * self.average_rating/ self.distance_from_city_center)
        return round(price_of_washing, 1)
    def wash_single_car(self, car):
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power
    def rate_service(self, new_rating):
        new_rating = self.average_rating * self.count_of_ratings + new_rating
        self.count_of_ratings += 1
        self.average_rating = round (new_rating / self.count_of_ratings, 1)
