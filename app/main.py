class Car:
    list_of_cars = []

    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand
        Car.list_of_cars.append(self)


class CarWashStation:
    def __init__(self, distance_from_city_center, clean_power,
                 average_rating, count_of_ratings):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car):
        first_action = car.comfort_class * (self.clean_power - car.clean_mark)
        second_action = self.average_rating / self.distance_from_city_center
        return round(first_action * second_action, 2)

    def serve_cars(self, list_of_cars):
        income = []
        for car in list_of_cars:
            if car.clean_mark < self.clean_power:
                income.append(self.calculate_washing_price(car))
                self.wash_single_car(car)
        return sum(income)

    def wash_single_car(self, car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power
        return car

    def rate_service(self, mark):
        first_action = self.average_rating * self.count_of_ratings + mark
        second_action = (self.count_of_ratings + 1)
        self.average_rating = round(first_action / second_action, 1)
        self.count_of_ratings += 1
