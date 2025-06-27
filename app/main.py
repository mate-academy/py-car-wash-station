class Car:
    def __init__(self, comfort_class: int, clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    income = 0
    rating = 0
    count_of_rates = 0

    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, list_of_cars: list) -> float:
        for car in list_of_cars:
            if self.can_wash(car):
                self.wash_single_car(car)
        return self.income

    def calculate_washing_price(self, car: Car) -> float:
        return round((car.comfort_class
                      * (self.clean_power - car.clean_mark)
                      * self.average_rating
                      / self.distance_from_city_center), 1)

    def wash_single_car(self, car: Car) -> None:
        if self.can_wash(car):
            self.income += self.calculate_washing_price(car)
            car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        rating = (self.average_rating
                  * self.count_of_ratings + rate) / (self.count_of_ratings + 1)
        self.average_rating = round(rating, 1)
        self.count_of_ratings += 1

    def can_wash(self, car: Car) -> bool:
        return self.clean_power > car.clean_mark
