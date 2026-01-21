class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self, distance_from_city_center,
        clean_power, average_rating, count_of_ratings
    ):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car):
        count_clean = self.clean_power - car.clean_mark
        count_distance = self.average_rating / self.distance_from_city_center
        income_ammount = (car.comfort_class * count_clean * count_distance)
        return round(income_ammount, 1)

    def wash_single_car(self, car):
        car.clean_mark = self.clean_power

    def serve_cars(self, car):
        income_ammount = 0
        for car_checker in car:
            if car_checker.clean_mark <= self.clean_power:
                income_ammount += self.calculate_washing_price(car_checker)
                self.wash_single_car(car_checker)
        return income_ammount

    def rate_service(self, voice):
        previous_rating = self.average_rating * self.count_of_ratings
        self.count_of_ratings = self.count_of_ratings + 1
        count_rating = (previous_rating + voice) / self.count_of_ratings
        self.average_rating = round(count_rating, 1)
