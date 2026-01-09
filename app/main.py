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

    def serve_cars(self, cars) -> float:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.wash_single_car(car)
        return income


    def calculate_washing_price(self, car) -> float:
        return round(car.comfort_class * (self.clean_power - car.clean_mark) * self.average_rating / self.distance_from_city_center, 1)


    def wash_single_car(self, car) -> float:
        income = self.calculate_washing_price(car)
        car.clean_mark = self.clean_power
        return income


    def rate_service(self, rating: int) -> None:
        total_ratings = (self.average_rating * self.count_of_ratings) + rating
        self.count_of_ratings += 1
        self.average_rating = round(total_ratings / self.count_of_ratings, 1)

