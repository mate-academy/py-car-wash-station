class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center, clean_power,
                 average_rating, count_of_ratings):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars):
        result = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                result += self.calculate_washing_price(car)
                car.clean_mark = self.clean_power
        return result

    def calculate_washing_price(self, car):
        price = car.comfort_class * (self.clean_power - car.clean_mark)\
            * self.average_rating / self.distance_from_city_center
        return round(price, 1)

    def wash_single_car(self, car):
        if car.clean_mark < self.clean_power:
            return car.comfort_class * (self.clean_power - car.clean_mark)\
                * self.average_rating / self.distance_from_city_center

    def rate_service(self, rating):
        result = (self.average_rating * self.count_of_ratings + rating) /\
                 (self.count_of_ratings + 1)
        self.average_rating = round(result, 1)
        self.count_of_ratings += 1
        print(self.average_rating)
