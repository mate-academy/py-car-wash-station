class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> str:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: int, clean_power: int,
                 average_rating: int, count_of_ratings: int) -> str:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: str) -> str:
        total_income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                cost = self.calculate_washing_price(car)
                total_income += cost
                self.wash_single_car(car)
        return round(total_income, 1)

    def calculate_washing_price(self, car: str) -> str:
        return round(
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating / self.distance_from_city_center,
            1
        )

    def wash_single_car(self, car: str) -> str:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: int) -> str:
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + rating)
            / (self.count_of_ratings + 1),
            1
        )
        self.count_of_ratings += 1
