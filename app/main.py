class Car:

    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:

    def __init__(self, distance_from_city_center, clean_power, average_rating,
                 count_of_ratings):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]):
        total_income = 0

        for car in cars:
            if self.clean_power > car.clean_mark:
                total_income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return total_income

    def calculate_washing_price(self, car: Car):
        suitable_cars = self.clean_power - car.clean_mark
        wash_parameters = self.average_rating / self.distance_from_city_center
        cost_one_wash = car.comfort_class * suitable_cars * wash_parameters
        return round(cost_one_wash, 1)

    def wash_single_car(self, car: Car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, single_rate):
        sum_rating = self.count_of_ratings * self.average_rating
        sum_rating += single_rate
        self.count_of_ratings += 1
        self.average_rating = round(sum_rating / self.count_of_ratings, 1)
