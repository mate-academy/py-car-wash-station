class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation(Car):
    def __init__(self,
                 distance_from_city_center,
                 clean_power,
                 average_rating,
                 count_of_ratings
                 ):
        self.distance = float(distance_from_city_center)
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars):
        income = 0
        for i in cars:
            if i.clean_mark < self.clean_power:
                income += self.calculate_washing_price(i)
                self.wash_single_car(i)
        return round(income, 1)

    def calculate_washing_price(self, car):
        cars_difference = self.clean_power - car.clean_mark
        comfort_minus_difference = car.comfort_class * cars_difference
        price = comfort_minus_difference * self.average_rating
        return round(price / self.distance, 1)

    def wash_single_car(self, car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power
        return car

    def rate_service(self, rating):
        self.count_of_ratings += 1
        full_rating = self.average_rating * (self.count_of_ratings - 1)
        average_rating = full_rating + rating
        self.average_rating = round(
            average_rating / self.count_of_ratings, 1
        )
