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
                 distance_from_city_center: float,
                 clean_power: int, average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def wash_single_car(self, car: Car, clean_power: int) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power
        else:
            print("Wash station clean power is less or equals Car clean mark")

    def rate_service(self, rating: int) -> None:
        if rating not in range(1, 6):
            print("Rating should be between 1 and 5")
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + rating)
            / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1

    def calculate_washing_price(self, car: Car) -> float:
        price = 0
        if car.clean_mark < self.clean_power:
            price = (car.comfort_class
                     * (self.clean_power - car.clean_mark)
                     * self.average_rating
                     / self.distance_from_city_center)
        return price

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0
        for car in cars:
            car_price = self.calculate_washing_price(car)
            if car_price > 0:
                self.wash_single_car(car, self.clean_power)
                income += car_price
        return round(income, 1)
