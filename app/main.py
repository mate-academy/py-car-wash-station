class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center,
                 clean_power,
                 average_rating, count_of_ratings):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car):
        difference = self.clean_power - car.clean_mark
        division = (self.average_rating / self.distance_from_city_center)
        income = car.comfort_class * difference * division
        return round(income, 1)

    def serve_cars(self, cars_list):
        result = 0
        for car in cars_list:
            if car.clean_mark < self.clean_power:
                result += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(result, 1)

    def wash_single_car(self, car):
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, service_rating):
        rating = (self.average_rating * self.count_of_ratings) + service_rating
        self.average_rating = round(rating / (self.count_of_ratings + 1), 1)
        self.count_of_ratings = self.count_of_ratings + 1
