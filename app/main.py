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

    def calculate_washing_price(self, car) -> float:
        difference = (self.clean_power - car.clean_mark) * (self.average_rating / self.distance_from_city_center)
        cost = car.comfort_class * difference
        return round(cost, 1)

    def wash_single_car(self, car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def rate_service(self, rating) -> None:
        total = (self.average_rating * self.count_of_ratings) + rating
        self.count_of_ratings += 1
        self.average_rating = round(total / self.count_of_ratings, 1)
