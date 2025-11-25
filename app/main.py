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
                 count_of_ratings
                 ):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def wash_single_car(self, car):
        if not isinstance(car, Car):
            return None
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power
            return True

    def calculate_washing_price(self, car):
        if self.clean_power <= car.clean_mark:
            return 0.0
        diff = self.clean_power - car.clean_mark
        raw = car.comfort_class * diff * self.average_rating
        price = raw / self.distance_from_city_center
        return round(price, 1)

    def serve_cars(self, cars):
        total = 0.0
        for car in cars:
            if isinstance(car, Car) and car.clean_mark < self.clean_power:
                price = self.calculate_washing_price(car)
                self.wash_single_car(car)
                total += price
        return round(total, 1)

    def rate_service(self, mark):
        old_count = self.count_of_ratings
        new_count = old_count + 1
        new_average_rating = ((self.average_rating * old_count + mark)
                              / new_count)
        self.count_of_ratings = new_count
        self.average_rating = round(new_average_rating, 1)
