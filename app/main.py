class Car:

    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
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

    def serve_cars(self, cars: list):
        suma = round(sum([self.calculate_washing_price(car)
                          for car in cars
                          if car.clean_mark < self.clean_power]), 1)
        for car in cars:
            if car.clean_mark <= self.clean_power:
                self.wash_single_car(car)
        return suma

    def calculate_washing_price(self, car):
        class_clean = car.comfort_class * (self.clean_power - car.clean_mark)
        rate_daistance = self.average_rating / self.distance_from_city_center
        return round(class_clean * rate_daistance, 1)

    def wash_single_car(self, car):
        if car.clean_mark <= self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rate):
        rate_change = self.average_rating * self.count_of_ratings + rate
        self.count_of_ratings += 1
        self.average_rating = round(rate_change / self.count_of_ratings, 1)
