class Car:
    def __init__(self, comfort_class: int, clean_car: int, brand: str) -> None:
        self.cf_class = comfort_class
        self.clean_car = clean_car
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.dst_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.rating = average_rating
        self.count_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:

        price = (car.cf_class * (self.clean_power - car.clean_car)
                 * self.rating / self.dst_city_center)
        return round(price, 1)

    def serve_cars(self, cars: list) -> float:
        income = 0
        for car in cars:
            if car.clean_car < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return income

    def rate_service(self, new_rating: int) -> None:

        rate = ((self.rating * self.count_ratings + new_rating)
                / (self.count_ratings + 1))
        self.rating = round(rate, 1)
        self.count_ratings += 1

    def wash_single_car(self, car: Car) -> None:
        if car.clean_car < self.clean_power:
            car.clean_car = self.clean_power
