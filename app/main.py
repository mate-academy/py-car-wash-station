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

    def serve_cars(self, cars):
        income = 0
        for i in range(len(cars)):
            if cars[i].clean_mark < self.clean_power:
                income += self.calculate_washing_price(cars[i])
                self.wash_single_car(cars[i])
        return round(income, 1)

    def rate_service(self, rate: int):
        self.average_rating = round((self.average_rating
                                     * self.count_of_ratings + rate)
                                    / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1

    def wash_single_car(self, car: Car):
        if car.clean_mark <= self.clean_power:
            car.clean_mark = self.clean_power

    def calculate_washing_price(self, car: Car):
        return round(((car.comfort_class
                       * (self.clean_power - car.clean_mark)
                       * self.average_rating)
                      / self.distance_from_city_center), 1)
