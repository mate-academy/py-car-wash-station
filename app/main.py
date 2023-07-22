class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center, clean_power, average_rating, count_of_ratings):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, car_list):
        total_income = 0

        for car in car_list:
            if car.clean_mark < self.clean_power:
                cost = self.calculate_washing_price(car)
                total_income += cost
                self.wash_single_car(car)

        return round(total_income, 1)

    def calculate_washing_price(self, car):
        difference_clean_power_mark = self.clean_power - car.clean_mark
        remainder_rating_distance = self.average_rating / self.distance_from_city_center
        result_of_calculate_price = car.comfort_class * difference_clean_power_mark * remainder_rating_distance
        return round(result_of_calculate_price, 1)

    def wash_single_car(self, car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rating):
        if 1.0 <= rating <= 5.0:
            total_rating = self.average_rating * self.count_of_ratings
            self.count_of_ratings += 1
            total_rating += rating
            self.average_rating = total_rating / self.count_of_ratings
            self.average_rating = round(self.average_rating, 1)
            return self.average_rating
