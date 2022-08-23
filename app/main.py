class Car:

    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center,
                 clean_power, average_rating,
                 count_of_ratings):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car):
        rating_distance = self.average_rating / self.distance_from_city_center
        clean_power_and_mark = self.clean_power - car.clean_mark
        price = car.comfort_class * clean_power_and_mark * rating_distance
        return price

    def serve_cars(self, cars_to_wash: list):
        price = []
        for car in cars_to_wash:
            if car.clean_mark < self.clean_power:
                price.append(self.calculate_washing_price(car))
                self.wash_single_car(car)
        return round(sum(price), 1)

    def wash_single_car(self, car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, mark):
        total = self.average_rating * self.count_of_ratings + mark
        self.average_rating = round(total / (self.count_of_ratings + 1), 1)
        self.count_of_ratings = self.count_of_ratings + 1
