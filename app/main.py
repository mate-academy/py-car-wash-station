class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power,
                 average_rating: float, count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, ls: list):
        income = 0
        for item in ls:
            if item.clean_mark < self.clean_power:
                income += self.calculate_washing_price(item)
                self.wash_single_car(item)
        return income

    def calculate_washing_price(self, car):
        x = car.comfort_class * (self.clean_power - car.clean_mark)
        y = self.average_rating / self.distance_from_city_center
        return round(x * y, 1)

    def rate_service(self, r):
        a = self.average_rating * self.count_of_ratings
        self.average_rating = round((a + r) / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1

    def wash_single_car(self, car):
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power
        else:
            car.clean_mark = car.clean_mark
