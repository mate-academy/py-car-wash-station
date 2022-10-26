class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: int,
                 clean_power: int, average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        cash = 0
        for car in cars:
            cash += self.wash_single_car(car)
        return round(cash, 1)

    def calculate_washing_price(self, car: Car) -> float:
        cc = car.comfort_class
        cp = self.clean_power
        cm = car.clean_mark
        ar = self.average_rating
        dfcc = self.distance_from_city_center
        price = cc * (cp - cm) * ar / dfcc
        return price

    def wash_single_car(self, car: Car) -> float:
        cash = 0
        if car.clean_mark < self.clean_power:
            cash += self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
        return round(cash, 1)

    def rate_service(self, rating: float) -> None:
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + rating)
            / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
