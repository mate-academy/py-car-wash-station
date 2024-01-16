class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str)\
            -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: int, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car_to_wash: Car) -> float:
        return round(car_to_wash.comfort_class
                     * (self.clean_power - car_to_wash.clean_mark)
                     * self.average_rating / self.distance_from_city_center, 1)

    def wash_single_car(self, car_to_wash: Car) -> float:
        price = 0
        if car_to_wash.clean_mark < self.clean_power:
            price = self.calculate_washing_price(car_to_wash)
            car_to_wash.clean_mark = self.clean_power
        return price

    def serve_cars(self, cars_to_wash: list) -> float:
        income = 0
        for car in cars_to_wash:
            income += self.wash_single_car(car)
        return income

    def rate_service(self, rating: float) -> None:
        self.average_rating = round(
            (self.count_of_ratings * self.average_rating + rating)
            / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
