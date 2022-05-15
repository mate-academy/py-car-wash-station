class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand

    def __repr__(self):
        return f"{self.comfort_class, self.clean_mark, self.brand}"


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list):
        income = 0

        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def wash_single_car(self, car):
        car.clean_mark = self.clean_power

    def calculate_washing_price(self, car: Car):
        return round(
            (car.comfort_class * (self.clean_power - car.clean_mark
                                  ) * self.average_rating
             ) / self.distance_from_city_center, 1
        )

    def rate_service(self, rate):
        self.average_rating = round(
            ((self.average_rating * self.count_of_ratings) + rate
             ) / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1

    def __repr__(self):
        return f"{self.distance_from_city_center, self.clean_power}" \
               f"{ self.average_rating, self.count_of_ratings}"
