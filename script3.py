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

    def calculate_washing_price(self, car):
        cost = car.comfort_class * (
                    self.clean_power - car.clean_mark) / self.distance_from_city_center * self.average_rating
        return round(cost, 1)


    def wash_single_car(self, car):
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars):
        total_inner = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                wash_cost = self.calculate_washing_price(car)
                total_inner += wash_cost
                self.wash_single_car(car)
        return round(total_inner, 1)

    def rate_service(self, new_raiting):
        new_average_rating = (self.average_rating * self.count_of_ratings) + new_raiting
        denominater = self.count_of_ratings + 1
        self.average_rating = round(new_average_rating / denominater, 1)
        self.count_of_ratings += 1
