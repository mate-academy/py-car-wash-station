class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = int(comfort_class)
        self.clean_mark = int(clean_mark)
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center, clean_power, average_rating, count_of_ratings):
        self.distance_from_city_center = float(distance_from_city_center)
        self.clean_power = int(clean_power)
        self.average_rating = float(average_rating)
        self.count_of_ratings = int(count_of_ratings)


    def serve_cars(self, cars):
        total_income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                price = self.calculate_washing_price(car)
                total_income += price
                self.wash_single_car(car)
        return round(total_income, 1)


    def calculate_washing_price(self, car):
        diff = self.clean_power - car.clean_mark
        if diff <= 0:
            return 0.0
        price = car.comfort_class * diff * self.average_rating / self.distance_from_city_center
        return round(price, 1)


    def wash_single_car(self, car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power


    def rate_service(self, new_rate):
        current_sum = self.average_rating * self.count_of_ratings
        new_sum = current_sum + float(new_rate)
        self.count_of_ratings += 1
        self.average_rating = round(new_sum / self.count_of_ratings, 1)
