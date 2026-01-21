class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center,
        clean_power,
        average_rating,
        count_of_ratings
    ):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car):
        base_price = car.comfort_class * 10
        dirty_multiplier = 1 + (10 - car.clean_mark) / 10
        distance_price = self.distance_from_city_center * 0.5
        power_discount = min(self.clean_power / 100, 0.2)
        price = base_price * dirty_multiplier * (1 - power_discount)
        price += distance_price
        return round(price, 2)

    def wash_single_car(self, car):
        price = self.calculate_washing_price(car)
        car.clean_mark = 10
        return price

    def serve_cars(self, cars):
        total = 0
        for car in cars:
            total += self.wash_single_car(car)
        return round(total, 2)

    def rate_service(self, new_rating):
        total = self.average_rating * self.count_of_ratings
        total += new_rating
        self.count_of_ratings += 1
        self.average_rating = total / self.count_of_ratings
        return round(self.average_rating, 2)
