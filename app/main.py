class Car:
    def __init__(self, klass, clean, brand):
        self.comfort_class = klass
        self.clean_mark = clean
        self.brand = brand


class CarWashStation:
    def __init__(self, distance, clean, rating, count):
        self.distance_from_city_center = distance
        self.clean_power = clean
        self.average_rating = rating
        self.count_of_ratings = count

    def calculate_washing_price(self, car):
        dif_cl = self.clean_power - car.clean_mark
        part_of_calc = car.comfort_class * dif_cl * self.average_rating
        calc = part_of_calc / self.distance_from_city_center
        return round(calc, 1)

    def serve_cars(self, cars: list):
        cost = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                cost += self.calculate_washing_price(car)
                car.clean_mark = self.clean_power
        return cost

    def wash_single_car(self, car):
        pass

    def rate_service(self, rate):
        sum_of_rates = self.average_rating * self.count_of_ratings + rate
        self.count_of_ratings += 1
        self.average_rating = round(sum_of_rates / self.count_of_ratings, 1)
